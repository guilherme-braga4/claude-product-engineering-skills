# Manual — Product AS-IS

## Quando invocar

Use antes de iniciar uma frente quando for necessário compreender o Produto existente por inteiro: produtos, usuários, jornadas, capacidades, regras, dados, dependências, disponibilidade e lacunas. A skill cria um retrato verificável e incremental do estado atual.

Ela mapeia o que existe. Para decidir a arquitetura de uma mudança, use `high-level-engineering`. Para avaliar uma release contra critérios de lançamento, use `product-engineering-readiness`.

## Invocação mínima

Abra o Claude Code na raiz do repositório e envie:

```text
/product-as-is
Mapeie o Produto existente neste repositório e produza o handoff para a próxima frente.
```

## Entrada recomendada

```text
/product-as-is

Objetivo do mapeamento:
[por que o AS-IS será usado]

Escopo conhecido:
[repositórios, produtos ou limites; deixe em branco para descoberta]

Fontes adicionais:
[documentos, ambientes, chats ou serviços acessíveis]

Restrições:
[operações proibidas, fontes inacessíveis ou prazo]
```

A skill inventaria toda a base acessível, inclusive arquivos relevantes ocultos ou ignorados. Projetos grandes são processados por unidades e checkpoints, sem trocar completude por amostragem silenciosa.

## O que esperar

Na convenção padrão, os artefatos ficam em `docs/product-as-is/`:

- `AS-IS.md`: retrato completo por produto ou domínio.
- `HANDOFF.md`: contexto autossuficiente para a próxima frente.
- `EVOLUTION.md`: alterações desde a base anterior.
- `INVENTORY.md`, `COVERAGE.md` e `EVIDENCE.md`: rastreabilidade e limites.
- Snapshots de unidades e `CHECKPOINT.md` quando o volume exigir.

A auditoria escreve somente seus próprios artefatos. Bugs, specs antigas e oportunidades aparecem como achados; não são corrigidos por esta skill.

## Antes de compactar

Use os prompts de [CONTEXT-COMPACTION.md](CONTEXT-COMPACTION.md) para persistir descobertas ainda não consolidadas e reduzir o contexto sem perder a retomada.

