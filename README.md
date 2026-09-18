# Claude Product Engineering Skills

Skills pessoais e reutilizáveis para compreender um produto, orientar sua arquitetura e avaliar prontidão para lançamento no Claude Code.

## Skills

| Skill | Use quando | Resultado principal |
|---|---|---|
| [`high-level-engineering`](high-level-engineering/MANUAL.md) | A necessidade de Produto precisa virar arquitetura, contratos e direção de implementação. | Contexto técnico atual, decisão arquitetural, impactos e validação. |
| [`product-as-is`](product-as-is/MANUAL.md) | É necessário mapear o Produto que existe hoje antes de iniciar uma frente. | Inventário completo, jornadas, regras, evidências, cobertura e handoff. |
| [`prd-from-discovery`](prd-from-discovery/MANUAL.md) | Discovery e decisões precisam virar um contrato de Produto verificável. | PRD no template definido, rastreabilidade, aceite e questões pendentes. |
| [`product-engineering-readiness`](product-engineering-readiness/MANUAL.md) | Uma release, piloto ou expansão precisa de decisão de prontidão. | Veredito rastreável e lotes de ações prontos para aprovação. |
| [`architecture-readiness`](architecture-readiness/MANUAL.md) | O diagnóstico de Readiness precisa virar arquitetura e ações de Engenharia para aprovação. | Snapshot datado, ARCH AS-IS/TO-BE, relatório de mudanças e matriz Produto ↔ Engenharia. |
| [`roadmap-executor-pre-check-deps`](roadmap-executor-pre-check-deps/SKILL.md) | PRD e Roadmap estão aprovados e é preciso fechar pré-requisitos antes da implementação. | Scan em Plan mode, refinamento por perguntas e relatório verificável de prontidão e checkpoints. |
| [`roadmap-executor`](roadmap-executor/SKILL.md) | O trecho do Roadmap está preparado e autorizado para executar. | TaskPlan por fase, implementação iterativa, revisão e validação do produto em execução. |
| [`valeti-jira-delivery`](valeti-jira-delivery/SKILL.md) | Uma entrega de código da Valeti será iniciada, retomada ou encerrada. | ROADMAP → Task pai → TASKPLAN → Subtasks via Rovo MCP, branch do pai e sincronização dos cards do usuário. |

## Instalação no Claude Code

As pastas deste repositório são a fonte versionada. Para disponibilizá-las em todos os projetos da máquina, crie links na pasta pessoal do Claude Code:

```bash
mkdir -p ~/.claude/skills
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/high-level-engineering ~/.claude/skills/high-level-engineering
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/product-as-is ~/.claude/skills/product-as-is
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/prd-from-discovery ~/.claude/skills/prd-from-discovery
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/product-engineering-readiness ~/.claude/skills/product-engineering-readiness
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/architecture-readiness ~/.claude/skills/architecture-readiness
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/roadmap-executor-pre-check-deps ~/.claude/skills/roadmap-executor-pre-check-deps
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/roadmap-executor ~/.claude/skills/roadmap-executor
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/valeti-jira-delivery ~/.claude/skills/valeti-jira-delivery
```

Antes de criar um link, confira se o destino já existe. Preserve ou remova conscientemente uma instalação anterior; `ln` não deve ser usado para sobrescrever uma pasta sem revisar seu conteúdo.

O comando de cada skill vem do nome de sua pasta:

```text
/high-level-engineering
/product-as-is
/prd-from-discovery
/product-engineering-readiness
/architecture-readiness
/roadmap-executor-pre-check-deps
/roadmap-executor
/valeti-jira-delivery
```

O Claude também pode carregar uma skill automaticamente quando a solicitação corresponder à descrição do `SKILL.md`. A invocação explícita torna a intenção inequívoca.

## Fluxo recomendado

As skills podem ser usadas isoladamente. Para uma iniciativa completa, a sequência típica é:

1. `/product-as-is` para estabelecer o Produto existente com evidências.
2. `/prd-from-discovery` para transformar o Discovery e decisões em requisitos e aceite de Produto.
3. `/high-level-engineering` para desenhar ou revisar a direção técnica da mudança.
4. `/product-engineering-readiness` para confrontar o lançamento pretendido com Produto, Software e evidências atuais.
5. `/architecture-readiness` como etapa pós-diagnóstico do Readiness: mapear a base avaliada, desenhar o destino completo e apresentar mudanças/ações rastreáveis para aprovação.
6. `/roadmap-executor-pre-check-deps` em Plan mode para inspecionar cada entrega do trecho aprovado, resolver pendências e registrar o relatório de preparação.
7. `/roadmap-executor` para implementar o trecho liberado, criando o TaskPlan de cada fase na hora de executá-la, com revisão e validação real.
8. Nova avaliação de Readiness após implementação, com novo snapshot de arquitetura.

Os primeiros handoffs são opcionais. `architecture-readiness` depende de PRD e avaliação Readiness identificáveis; a versão do Readiness neste repositório chama essa etapa antes de apresentar os pacotes para aprovação, quando disponível e dentro do recorte solicitado. Cada skill revalida contexto e não trata a conclusão de outro agente como prova atual automática. Para usar a integração, mantenha ambas as instalações atualizadas a partir das pastas versionadas.

## Preparação e execução do Roadmap

Inicie o Claude Code em Plan mode (`claude --permission-mode plan`) e use o [prompt de pre-check do Roadmap completo](roadmap-executor-pre-check-deps/PROMPT.md), preenchendo os caminhos do PRD, Roadmap e demais fontes aprovadas. A skill lê código, contratos e condições de ambiente, prefere `AskUserQuestion` para refinar decisões e mantém pendências abertas até haver evidência de fechamento. Saneamento que exige escrita é preparado para execução autorizada fora do Plan mode; um plano de correção não conta como correção concluída. O relatório pode ficar no arquivo de plano permitido pelo runtime até ser exportado ao projeto.

O relatório distingue pré-requisitos (`PRONTO`, `PENDENTE`, `INCONCLUSIVO`) e continuidade (`CONTÍNUA NO TRECHO` ou `COM CHECKPOINTS`). Recursos que o próprio Roadmap construirá são dependências internas; PR/merge/deploy humanos são checkpoints explícitos. Nenhum relatório promete ausência de imprevistos. Com o relatório PRONTO, use o [prompt de execução do Roadmap completo](roadmap-executor/PROMPT.md), passando o mesmo trecho e o caminho do relatório. O executor reutiliza decisões e evidências e confere apenas a validade da base e condições voláteis antes de implementar.

Uma futura `roadmap-executor-outage` permanece condicionada à validação de uma retomada real e de seu resultado final; ela ainda não faz parte das skills implementadas.

## Código da Valeti: Jira antes da branch

As skills que executam código aplicam [valeti-jira-delivery](valeti-jira-delivery/SKILL.md), inclusive lotes aprovados de Readiness, saneamento do pre-check e protótipos/correções autorizados durante engenharia. Instale essa pasta junto das skills chamadoras, como pasta irmã; os links relativos dependem dessa estrutura. Em Codex, use a mesma estrutura em `~/.codex/skills`. Atualize cópias instaladas ou use links para a fonte versionada.

1. Leia/crie o ROADMAP no escopo autorizado. O nome de cada item torna-se o summary de uma Task pai no Jira via Rovo MCP; pesquise e reutilize cards existentes.
2. Depois, leia/crie o TASKPLAN atual. Cada item de trabalho torna-se uma Subtask do pai correspondente.
3. Antes de código, confirme os cards e use `<prefixo>/<CHAVE-DA-TASK-PAI>`, por exemplo `feature/VWAD-1234`. Preserve o prefixo confirmado do Bitbucket; não use a chave da Subtask ou descrições no nome. Todos os itens do mesmo pai podem compartilhar a branch e PR por repositório.
4. Um agente identificado sincroniza status/coluna conforme evidências e gates, relendo o responsável antes de cada escrita e alterando **somente os cards mapeados atribuídos ao usuário confirmado**. Desenvolvimento concluído com review/merge obrigatório pendente continua em revisão, não DONE.

PRD, arquitetura e auditoria não criam cards por si só. Plan mode apenas prepara o mapeamento; criação de cards e branches ocorre na execução autorizada. O protocolo preserva a fila interna de Agent Teams e não transforma `docs/TASKS.md` em fila.

## Compactação de contexto

Nas skills que incluem `CONTEXT-COMPACTION.md`, o arquivo contém dois prompts:

1. persistir e reconciliar o estado importante antes da compactação;
2. executar `/compact` preservando apenas o contexto operacional que não pode ser recuperado das fontes canônicas.

Use os dois passos nesta ordem. Aguarde a confirmação de que a sessão está segura para compactar antes de enviar o segundo prompt.

O pre-check mantém seu relatório/artefato de plano atualizado entre rodadas; o executor mantém o estado canônico em checkpoints de execução. Ao retomar, reconcilie esses registros com as evidências e o Git.

## Manutenção

- Edite a cópia versionada neste repositório.
- Mantenha decisões duráveis nos documentos canônicos do projeto analisado.
- Não inclua segredos, dados pessoais, snapshots de produto ou relatórios de projetos específicos neste repositório de skills.
- Valide o frontmatter e os links depois de alterar uma skill.
