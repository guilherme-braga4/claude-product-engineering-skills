import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_prd.py"
spec = importlib.util.spec_from_file_location("validate_prd", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

# Exemplo sintético para testar o verificador, não uma especificação aprovada.
VALID = """# PRD: Confirmação de presença

## 1. PROBLEMA & CONTEXTO
- **O que estamos resolvendo:** participantes precisam saber se a confirmação foi recebida.
- **Motivação:** evitar dúvidas sobre participação.
- **Contexto do Legado:** o participante já pode consultar o encontro.
- **Impacto do Sucesso:** confirmação compreensível ao participante.

## 2. ATORES
| Ator | Tipo (humano/sistema/hardware) | Como interage |
|------|-------------------------------|---------------|
| Participante | humano | Confirma presença |

## 3. REGRAS DE NEGÓCIO (BUSINESS RULES)
### Confirmação
- **RN01:** Somente o participante convidado pode confirmar sua presença.
  - **Escopo:** confirmação de encontro para o qual recebeu convite.
  - **Teste mínimo:** convidado confirma; não convidado não confirma.

## 4. CASOS DE USO DE PRODUTO
### UC01: Confirmar presença
- **Ator:** Participante.
- **Pré-condições:** convite válido.
- **Fluxo Principal (Happy Path):**
  1. Participante consulta convite.
  2. Participante confirma presença.
- **Fluxos Alternativos:** participante consulta a confirmação já realizada.
- **Fluxos de Exceção:** sem convite, nenhuma confirmação é registrada.
- **Pós-condições:** participante consegue observar sua confirmação.
- **Telemetria mínima:** confirmação ou recusa identificável pelo responsável do encontro.
- **Teste de integração mínimo:** convidado confirma e consulta o resultado; não convidado permanece sem confirmação.

## 5. REQUISITOS FUNCIONAIS (RF)
- **RF01 — MUST — [NOVO]:** Permitir confirmar presença no encontro.
  - **Critério de aceite:** convidado consegue observar a presença confirmada após solicitar confirmação.
  - **Dependências:** convite e participante.
  - **Notas:** escopo deste encontro.

## 6. QUALIDADES ESPERADAS DO PRODUTO
### 6.1 Clareza
O participante entende se sua presença foi confirmada sem precisar de auxílio.

## 7. MUDANÇAS (TO BE)
### 7.1 Visão Geral
- **Total de alterações:** 1
- **Classificação:** 1 Nova funcionalidade
- **Estratégia de execução:** Sequencial.
| # | Alteração | Tipo | Prioridade | Impacto (UC/RN/RF/Qualidade) | Risco |
|---|-----------|------|------------|-----------------------------|-------|
| 1 | Confirmação | Criação | MUST | UC01, RN01, RF01, §6.1 | Médio |
### 7.2 Alterações Detalhadas
#### Alteração 1 — MUST — Confirmação de presença
**Classificação:** Novo RF.
**Tipo:** Criação.
**Dependências:** nenhuma.
##### Descrição:
Permitir ao convidado confirmar presença e observar o resultado.
##### Impacto:
**UCs Impactados:** UC01.
**RNs Impactadas:** RN01.
**RFs Impactados:** RF01.
**Qualidades Impactadas:** §6.1.
##### O Que Precisa Ser Feito:
**Implementação:** permitir confirmação pelo participante convidado.
**Testes:** RN01: convite autoriza confirmação; UC01: confirmar e consultar; qualidade: verificar clareza do resultado.
**Infraestrutura/Observabilidade:** confirmação e recusa identificáveis.
##### Critérios de Aceite:
- [ ] Convidado confirma e consulta o resultado.
- [ ] Não convidado não confirma.
##### Gestão de Risco:
**Risco:** Médio.
**O que pode dar errado:** participante acreditar que confirmou sem confirmação registrada.
**Como mitigar:** informar o resultado real da solicitação.
**Rollback:** suspender novas confirmações preservando as existentes se houver registros inconsistentes.
##### APROVAÇÃO:
- [ ] Aprovado
- [ ] Aprovado com Ressalvas
- [ ] Rejeitado
- [x] Pendente: decisão do responsável de Produto e releitura posterior.

## 8. PERGUNTAS EM ABERTO
Não se aplica: recorte sem decisão adicional identificada no exemplo.

## Checklist de Validação Final
- [ ] Conteúdo de Produto revisado.
- [ ] Releitura feita após dormir uma noite.
"""


class ValidatorTests(unittest.TestCase):
    def codes(self, text, **kwargs):
        return {i["code"] for i in validator.validate(text, **kwargs)}

    def test_valid_structure_and_natural_acceptance(self):
        self.assertEqual([], validator.validate(VALID))

    def test_missing_section_is_not_silently_accepted(self):
        self.assertIn("section", self.codes(VALID.replace("## 2. ATORES", "## Atores")))

    def test_omission_requires_reason_and_preserves_numbering(self):
        omitted = VALID.replace(
            "## 8. PERGUNTAS EM ABERTO\nNão se aplica: recorte sem decisão adicional identificada no exemplo.",
            "Seção 8 não se aplica: recorte sem decisão adicional identificada no exemplo.")
        self.assertEqual([], validator.validate(omitted))

    def test_duplicate_active_rule(self):
        extra = "- **RN01:** Outra regra.\n  - **Escopo:** outro.\n  - **Teste mínimo:** sim ou não.\n"
        self.assertIn("id-duplicate", self.codes(VALID.replace(
            "## 4. CASOS DE USO DE PRODUTO", extra + "\n## 4. CASOS DE USO DE PRODUTO")))

    def test_empty_field_does_not_consume_next_field_label(self):
        broken = VALID.replace("**Escopo:** confirmação de encontro para o qual recebeu convite.", "**Escopo:**")
        self.assertIn("field", self.codes(broken))

    def test_quality_rejects_technical_target(self):
        changed = VALID.replace("sem precisar de auxílio.", "em 200 ms, com HTTP 200.")
        self.assertIn("quality-engineering", self.codes(changed))

    def test_structural_quality_id_and_business_number_are_allowed(self):
        changed = VALID.replace("convite válido.", "convite válido para até 3 acompanhantes.")
        self.assertNotIn("quality-engineering", self.codes(changed))

    def test_no_fake_priority_or_migration_tag(self):
        self.assertIn("priority", self.codes(VALID.replace("RF01 — MUST", "RF01 — urgente")))
        self.assertIn("migration-tag", self.codes(VALID.replace("[NOVO]", "")))

    def test_unresolved_placeholder(self):
        self.assertIn("placeholder", self.codes(VALID.replace("convite válido.", "[definir convite]")))

    def test_links_are_not_placeholders_or_implementation_paths(self):
        self.assertNotIn("placeholder", self.codes(VALID.replace(
            "convite válido.", "convite válido conforme [Discovery](../discovery.md).")))

    def test_missing_reference_is_flagged_for_contextual_review(self):
        issues = validator.validate(VALID.replace("UC01, RN01, RF01, §6.1", "UC01, RN01, RF09, §6.9"))
        self.assertTrue(any(i["code"] == "id-reference" and i["severity"] == "warning" for i in issues))
        self.assertTrue(any(i["code"] == "quality-reference" for i in issues))

    def test_same_rule_id_changed_is_not_declared_semantically_safe(self):
        revised = VALID.replace("Somente o participante convidado", "Qualquer participante")
        issues = validator.validate(revised, baseline=VALID)
        self.assertTrue(any(i["code"] == "rn-changed" for i in issues))

    def test_new_rule_id_does_not_rewrite_old_id(self):
        revised = VALID.replace("RN01", "RN02").replace(
            "Somente o participante convidado", "Qualquer participante")
        self.assertNotIn("rn-changed", self.codes(revised, baseline=VALID))

    def test_migration_only_one_change_and_counts_match(self):
        revised = VALID.replace("## 8. PERGUNTAS EM ABERTO",
                                "#### Alteração 2 — MUST — Outra\n\n## 8. PERGUNTAS EM ABERTO")
        codes = self.codes(revised, migration_only=True)
        self.assertIn("migration-only", codes)
        self.assertIn("change-count", codes)

    def test_code_fence_is_not_product_requirement(self):
        self.assertIn("code-fence", self.codes(VALID + "\n~~~python\nprint(1)\n~~~\n"))


if __name__ == "__main__":
    unittest.main()
