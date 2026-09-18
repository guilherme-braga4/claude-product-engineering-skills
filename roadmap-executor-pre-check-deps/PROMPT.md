# Prompt — pre-check do Roadmap completo

Abra uma sessão nova do Claude Code em Plan Mode e substitua os caminhos entre colchetes antes de enviar:

```text
/roadmap-executor-pre-check-deps

Faça o pre-check de dependências de 100% do Roadmap em @[CAMINHO_DO_ROADMAP].

Use como fontes aprovadas:
- PRD: @[CAMINHO_DO_PRD]
- Arquitetura e decisões técnicas, quando existirem: @[CAMINHO_DA_ARQUITETURA_OU_DAS_DECISOES]
- Demais documentos aplicáveis: @[CAMINHOS_ADICIONAIS]

Percorra todas as fases e entregas do Roadmap, incluindo seus critérios de aceite e a integração final. Inspecione os repositórios, pontos de código, contratos entre sistemas, infraestrutura, banco de dados, migrações, serviços externos, credenciais e acessos necessários, ambientes, dados de teste, execução local, testes automatizados, validações por UI/API/DB, estratégia de branches e worktrees, revisão, integração, publicação e comprovação dos gates.

Classifique cada dependência como pré-requisito externo, entrega interna do próprio Roadmap, checkpoint humano/externo ou item fora do escopo justificado. Uma entrega que será construída por uma fase anterior do Roadmap não deve bloquear o início; registre sua ordem, produtor, consumidor e critério de disponibilidade.

Use AskUserQuestion para fechar comigo todas as decisões necessárias, agrupando perguntas independentes e apresentando opções, consequências e uma recomendação. Não me pergunte fatos que possam ser verificados no código ou no ambiente. Depois de cada resposta, investigue novamente as áreas afetadas e continue refinando até não existir decisão necessária em aberto.

Não implemente funcionalidades nem altere código, infraestrutura, banco ou configuração global durante esta etapa. Quando uma pendência exigir escrita, prepare a ação exata, registre responsável e evidência esperada, e somente considere a condição resolvida depois que a ação autorizada for executada e verificada.

Na Valeti, consulte /valeti-jira-delivery e verifique por leitura o Rovo MCP, minha identidade, projeto/Board, tipos de cards, vínculos existentes e prefixos do Bitbucket. Prepare o fluxo ROADMAP → Task pai → TASKPLAN → Subtasks, com branch <prefixo>/<CHAVE-DA-TASK-PAI> e agente de sincronização somente dos meus cards. Não crie cards/branches nem TASKPLANs futuros em Plan mode. Registre a criação de cards faltantes como trabalho sequenciado obrigatório antes de código, inclusive para saneamentos autorizados fora do Plan mode; falta de acesso necessário continua sendo pendência externa.

Produza e mantenha um relatório persistente usando o template da Skill. Identifique a base analisada por versões dos documentos, commits, branches/worktrees e diffs relevantes. Registre evidências, decisões, autorizações, dependências internas, checkpoints, procedimentos de validação e o caminho do relatório para a retomada em outra sessão.

Somente declare os pré-requisitos PRONTOS quando todas as áreas aplicáveis de 100% do Roadmap tiverem sido examinadas, nenhuma decisão necessária estiver aberta, todos os pré-requisitos externos estiverem comprovados e as dependências internas puderem ser produzidas na ordem planejada. Declare separadamente se a execução pode ser CONTÍNUA NO TRECHO ou se possui CHECKPOINTS, indicando responsável e momento de cada pausa.

Não inicie a implementação ao concluir. Entregue o caminho do relatório aprovado e o prompt exato para iniciar /roadmap-executor com o mesmo escopo.
```

Se não houver arquitetura formal ou documentos adicionais, remova essas linhas. A ausência desses documentos só bloqueia o pre-check quando houver uma decisão técnica necessária que não possa ser sustentada pelas fontes aprovadas existentes.
