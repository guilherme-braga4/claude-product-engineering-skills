#!/usr/bin/env python3
"""Verificação estrutural somente leitura; não aprova requisitos ou decisões."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata


TITLES = {
    1: "PROBLEMA & CONTEXTO", 2: "ATORES",
    3: "REGRAS DE NEGÓCIO (BUSINESS RULES)",
    4: "CASOS DE USO DE PRODUTO", 5: "REQUISITOS FUNCIONAIS (RF)",
    6: "QUALIDADES ESPERADAS DO PRODUTO", 7: "MUDANÇAS (TO BE)",
    8: "PERGUNTAS EM ABERTO",
}


def normalized(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text)
                   if not unicodedata.combining(c)).casefold()


def sections(text):
    headers = list(re.finditer(r"(?m)^##\s+(.+)$", text))
    result = {}
    for i, header in enumerate(headers):
        number = re.match(r"(\d+)\.\s*(.*)", header[1])
        if number:
            end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
            result.setdefault(int(number[1]), []).append(
                (number[2], text[header.end():end]))
    return result


def entries(section, prefix):
    pattern = (r"(?m)^###\s+(UC\d+)\b[^\n]*" if prefix == "UC" else
               r"(?m)^-\s+\*\*(" + prefix + r"\d+)(?=[:\s*—-])[^\n]*")
    matches = list(re.finditer(pattern, section))
    return [(m[1], section[m.start():matches[i + 1].start()
             if i + 1 < len(matches) else len(section)])
            for i, m in enumerate(matches)]


def validate(text, baseline=None, migration_only=False):
    issues = []

    def issue(code, message, severity="error"):
        issues.append({"severity": severity, "code": code, "message": message})

    groups = sections(text)
    bodies = {n: rows[0][1] for n, rows in groups.items()}
    if not re.search(r"(?m)^# PRD:\s*\S", text):
        issue("title", "Título esperado: # PRD: nome da iniciativa.")
    for n, title in TITLES.items():
        if n not in groups:
            note = r"Seção\s+" + str(n) + r"\s+não se aplica\s*[:—-]\s*\S.+"
            if not re.search(note, text, re.I):
                issue("section", "Falta seção %s ou nota de não aplicabilidade com motivo." % n)
        else:
            if len(groups[n]) != 1:
                issue("section-duplicate", "Seção %s duplicada." % n)
            if normalized(groups[n][0][0].strip()) != normalized(title):
                issue("section-title", "Título da seção %s difere do template." % n)
    numbers = [int(m[1]) for m in re.finditer(r"(?m)^##\s+(\d+)\.", text)]
    if numbers != sorted(numbers):
        issue("section-order", "Seções numeradas fora de ordem.")
    if not re.search(r"(?m)^## Checklist de Validação Final\s*$", text):
        issue("checklist", "Falta o Checklist de Validação Final.")

    required = {
        "RN": ["Escopo", "Teste mínimo"],
        "UC": ["Ator", "Pré-condições", "Fluxo Principal", "Fluxos Alternativos",
               "Fluxos de Exceção", "Pós-condições", "Telemetria mínima",
               "Teste de integração mínimo"],
        "RF": ["Critério de aceite", "Dependências", "Notas"],
    }
    by_prefix = {}
    for prefix, n in [("RN", 3), ("UC", 4), ("RF", 5)]:
        found = entries(bodies.get(n, ""), prefix)
        by_prefix[prefix] = found
        for ident, count in Counter(item[0] for item in found).items():
            if count > 1:
                issue("id-duplicate", "%s tem %s definições ativas." % (ident, count))
        section_body = bodies.get(n, "")
        if n in bodies and not found and not re.search(
                r"não se aplica\s*[:—-]\s*\S.+", section_body, re.I):
            issue("empty-section", "Seção %s sem definições ou justificativa." % n)
        for ident, block in found:
            for field in required[prefix]:
                # Exige um campo rotulado com valor, não apenas menção em prosa.
                pattern = r"(?:^|\n)\s*-?\s*\*\*" + re.escape(field)
                pattern += r"(?:\s*\([^\n]*?\))?\s*:\*\*[ \t]*([^\n]*)"
                match = re.search(pattern, block, re.I)
                value = match[1].strip() if match else ""
                if match and not value:
                    following = [line.strip() for line in block[match.end():].splitlines() if line.strip()]
                    if following and not re.match(r"(?:[-*]\s*)?\*\*[^*]+:\*\*|^#", following[0]):
                        value = following[0]
                if not value:
                    issue("field", "%s: campo ausente/vazio: %s." % (ident, field))
            if prefix == "RF":
                first = block.splitlines()[0]
                if not re.search(r"\b(?:MUST|SHOULD|COULD|WON'T)\b", first):
                    issue("priority", "%s sem prioridade MoSCoW." % ident)
                if not re.search(r"\[(?:MANTIDO|EVOLUÍDO|NOVO)\]", first):
                    issue("migration-tag", "%s sem tag MANTIDO/EVOLUÍDO/NOVO." % ident)

    quality = bodies.get(6, "")
    quality_ids = re.findall(r"(?m)^###\s+(6\.\d+)\b", quality)
    for ident, count in Counter(quality_ids).items():
        if count > 1:
            issue("quality-duplicate", "Qualidade %s duplicada." % ident)
    if 6 in bodies and not quality_ids and not re.search(
            r"não se aplica\s*[:—-]\s*\S.+", quality, re.I):
        issue("empty-quality", "Seção 6 sem qualidades ou justificativa.")
    # IDs estruturais e destinos de hyperlinks não representam métricas.
    prose = re.sub(r"(?m)^###\s+6\.\d+\s*", "", quality)
    prose = re.sub(r"§\s*6\.\d+", "", prose)
    prose = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", prose)
    if re.search(r"\d|%|\b(?:ms|mb|gb|json|http|sql|rps|p95|p99)\b", prose, re.I):
        issue("quality-engineering", "Seção 6 contém número, métrica ou formato técnico; revisar ARCH §9.")
    # Em todo o PRD, links e tags válidas não são placeholders.
    plain = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    allowed = {"", "x", "mantido", "evoluído", "novo", "must", "should", "could", "won't"}
    for match in re.finditer(r"\[([^\]\n]+)\]", plain):
        if match[1].strip().casefold() not in allowed:
            issue("placeholder", "Possível placeholder não preenchido: " + match[0])
    if re.search(r"(?m)^\s*(?:`{3}|~{3})", text):
        issue("code-fence", "Bloco de código no PRD; detalhes de engenharia devem ficar fora.")
    if re.search(r"\b(?:HTTP|JSON|SQL|endpoint|npm|pip)\b|\b(?:src|lib|packages)/", plain):
        issue("engineering-leak", "Possível detalhe técnico fora do ARCH; revisar contexto.", "warning")

    defined = {ident for found in by_prefix.values() for ident, _ in found}
    for ident in sorted(set(re.findall(r"\b(?:RN|UC|RF)\d+\b", text)) - defined):
        issue("id-reference", "%s citado sem definição ativa; conferir histórico/escopo." % ident, "warning")
    for ident in sorted(set(re.findall(r"§\s*(6\.\d+)\b", text)) - set(quality_ids)):
        issue("quality-reference", "Referência §%s sem qualidade definida." % ident, "warning")
    changes = re.findall(r"(?m)^####\s+Alteração\s+(\d+)\b", bodies.get(7, ""))
    for ident, count in Counter(changes).items():
        if count > 1:
            issue("change-duplicate", "Alteração %s duplicada." % ident)
    total = re.search(r"\*\*Total de alterações:\*\*\s*(\d+)", bodies.get(7, ""))
    if total and int(total[1]) != len(changes):
        issue("change-count", "Total de alterações difere do número de detalhamentos.")
    if migration_only and len(changes) != 1:
        issue("migration-only", "Migração sem mudança de Produto exige uma única alteração em §7.")

    if baseline is not None:
        previous = sections(baseline)
        old = dict(entries(previous.get(3, [("", "")])[0][1], "RN"))
        for ident, block in by_prefix["RN"]:
            if ident in old and re.sub(r"\s+", " ", block).strip() != re.sub(
                    r"\s+", " ", old[ident]).strip():
                issue("rn-changed", "%s mudou de texto: revisar semântica e necessidade de novo ID." % ident, "warning")
        # Remoções não liberam IDs; histórico completo deve ser revisado pelo autor.
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prd", type=Path)
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--migration-only", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        issues = validate(args.prd.read_text(encoding="utf-8"),
                          args.baseline.read_text(encoding="utf-8") if args.baseline else None,
                          args.migration_only)
    except OSError as exc:
        parser.error(str(exc))
    errors = sum(i["severity"] == "error" for i in issues)
    if args.json:
        print(json.dumps({"errors": errors, "issues": issues,
                          "human_review_required": True}, ensure_ascii=False, indent=2))
    else:
        for i in issues:
            print("%s [%s] %s" % (i["severity"].upper(), i["code"], i["message"]))
        print("%s erro(s) estrutural(is). Revisão semântica e aprovação humana continuam necessárias." % errors)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
