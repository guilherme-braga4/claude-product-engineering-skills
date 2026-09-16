# Manual — Architecture Readiness

Use depois de uma avaliação de `product-engineering-readiness` para transformar os achados em arquitetura e ações de Engenharia para aprovação.

```text
/architecture-readiness
Use o PRD vigente e a execução de Readiness desta conversa.
Mapeie a arquitetura da base avaliada, atualize os ARCHs existentes
e prepare o TO-BE, o relatório de mudanças e a matriz para eu aprovar o desenvolvimento.
```

Se houver várias iniciativas ou avaliações, informe o PRD e o caminho da execução desejada. A skill descobre o restante no projeto. Pode ser usada com artefatos equivalentes de outra auditoria, desde que base, critérios, achados e evidências sejam identificáveis.

## Ciclo de trabalho

1. Readiness identifica prontidão, achados e lotes.
2. Architecture Readiness registra o AS-IS pré-remediação e propõe o TO-BE completo necessário para atender ao PRD.
3. Você resolve conflitos documentais em Plan mode, uma pergunta por vez, pela ferramenta `AskUserQuestion` (AskUserQuestions).
4. A skill entrega o delta, a matriz e os pacotes concretos para sua aprovação.
5. O fluxo de execução do Readiness implementa os pacotes que você aprovar e valida seus aceites.
6. A nova avaliação gera outro snapshot, preservando a história.

O TO-BE é o destino para atender à prontidão. Sua aprovação não afirma que a implementação ou a operação já estão prontas. Testes planejados continuam pendentes até serem executados.

## O que é criado ou atualizado

Sem convenção própria, os canônicos ficam em `docs/architecture/ARCH-AS-IS.md` e `ARCH-TO-BE.md`. Se já houver ARCHs canônicos em outros caminhos, eles são atualizados ali; suas versões anteriores são preservadas.

Cada execução tem uma pasta em:

```text
docs/architecture/snapshots/<data-hora>-<readiness-id>-<sufixo>/
```

Ela reúne os dois ARCHs, `RELATORIO.md`, `MATRIZ-PRODUTO-ENGENHARIA.md`, `INCONSISTENCIAS.md`, manifesto, checkpoint e bases documentais. `docs/architecture/INDEX.md` liga avaliações, snapshots e canônicos. Retomar uma execução em andamento não cria duplicatas; uma finalizada não é sobrescrita.

Os [modelos anexados](assets/ARCH-AS-IS-TEMPLATE.md) e o [modelo TO-BE](assets/ARCH-TO-BE-TEMPLATE.md) são preservados como recursos originais da skill. Exemplos de tecnologia não impõem stack. O relatório segue o [modelo de leitura para aprovação](assets/RELATORIO-TEMPLATE.md).

## Como ler e aprovar

Comece por `RELATORIO.md` §1–2: resultado para Produto e comparação antes/depois. Consulte ações e pacotes (§3–4), cobertura (§5) e decisões (§6). A matriz permite sair de qualquer requisito até ação e validação, e voltar de cada ação à sua justificativa de Produto.

Use os IDs/revisões efetivamente apresentados. Exemplo ilustrativo:

```text
Aprovo o desenvolvimento do pacote <readiness-id>/L-01/r1
e do pacote <snapshot-id>/ARCH-L-02/r1, nos escopos apresentados.
```

“Aprovo o TO-BE” aprova o desenho. Para autorizar implementação, identifique os pacotes de desenvolvimento. Uma autorização inequívoca já recebida não será pedida novamente para o mesmo escopo.

Conflitos PRD ↔ ARCH não são corrigidos silenciosamente. A skill registra evidências, alternativas e consequências, entra em Plan mode quando a ferramenta permite e percorre cada Q. Em ambientes sem essa capacidade, informa a limitação e solicita a ativação do modo ou um fallback explícito; não simula perguntas ou decisões.

## Integração e limites

A versão de `product-engineering-readiness` deste repositório inclui a etapa de arquitetura antes de entregar lotes para aprovação. Ambas as skills precisam estar disponíveis na instalação usada; não há cron, hook de sistema ou habilitação automática de plugins. Um pedido explícito de auditoria sem arquitetura, sem escrita ou com outro recorte continua tendo prioridade.

Sem PRD/base suficiente, a entrega fica parcial com a entrada faltante identificada. Readiness negativo é uma entrada normal; evidência inacessível não é inventada. Sem delta necessário, o snapshot documenta a arquitetura mantida, sem criar refatorações artificiais.

## Compactação

Use [CONTEXT-COMPACTION.md](CONTEXT-COMPACTION.md) para persistir execução, questões, decisões, base e sincronização antes de compactar.
