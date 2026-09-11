# Manual — Product Engineering Readiness

## Quando invocar

Use para decidir se um produto, piloto, release ou expansão está pronto para o ambiente e o público pretendidos. A skill cruza requisitos de Produto, jornadas, regras, arquitetura, código, testes, fluxogramas e evidências operacionais.

Ela pode consumir resultados de `product-as-is`, `high-level-engineering` e outros chats, mas funciona sem eles e revalida o que afetar o veredito.

## Invocação mínima

Abra o Claude Code na raiz do projeto e envie:

```text
/product-engineering-readiness
Avalie se esta release está pronta para produção.
```

## Entrada recomendada

```text
/product-engineering-readiness

Objetivo e tipo de lançamento:
[piloto, lançamento ou expansão]

Produto, release e repositórios:
[versão candidata e escopo]

Ambiente e público-alvo:
[onde e para quem será disponibilizado]

Critérios obrigatórios:
[PRD ou condições de go-live]

Contexto complementar:
[chats, handoffs, AS-IS, arquitetura e fluxogramas]

Restrições de execução:
[ambientes ou operações disponíveis]
```

A skill descobre o que já estiver no projeto. Sem definição suficiente do lançamento, ela continua o diagnóstico e aponta a decisão faltante, mas não emite prontidão positiva.

## O que esperar

A resposta principal traz:

1. prontidão e cobertura separadas;
2. motivos determinantes e limitações;
3. lotes relacionados por causa, resultado ou dependência;
4. uma instrução curta para aprovação.

Exemplo:

```text
Aprovo L-01 r1 e L-03 r1 da execução 2026-09-11-release-x.
```

Cada lote informa impacto, proposta, alcance, riscos, dependências, efeitos autorizáveis e critérios de aceite. Aprovar um lote autoriza somente sua revisão apresentada. Publicação, PR, merge, migração e deploy precisam estar expressamente incluídos.

Depois da aprovação, continue na mesma conversa. A skill confere a base, executa os lotes autorizados, valida os critérios e atualiza o veredito. Se o escopo mudar materialmente, ela apresenta uma nova revisão do lote.

## Agent Team

O modo individual e o Agent Team usam o mesmo contrato de evidência e entrega. Uma missão com Agent Team exige PRD com objetivo, escopo e critérios de aceite antes da decomposição. O PRD genérico da skill não substitui o PRD da revisão do produto.

Agent Teams precisam estar disponíveis na sessão interativa do Claude Code. A skill não habilita configurações experimentais automaticamente.

## Artefatos

Na ausência de convenção do projeto, a revisão fica em:

```text
docs/product-engineering-readiness/
  INDEX.md
  runs/<run-id>/
    REVIEW.md
    COVERAGE.md
    ACTIONS.md
    CHECKPOINT.md
```

## Antes de compactar

Use [CONTEXT-COMPACTION.md](CONTEXT-COMPACTION.md) durante revisões longas e antes de executar `/compact`. O checkpoint deve refletir lotes aprovados, concluídos e pendentes sem transformar registros documentais em novas autorizações.

