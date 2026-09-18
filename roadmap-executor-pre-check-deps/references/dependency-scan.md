# Roteiro de inspeção de dependências

Examine as áreas aplicáveis para cada entrega do trecho escolhido. Registre localização, revisão, observação e implicação. README, configuração e relato do usuário são pistas; confirme capacidades operacionais com evidências disponíveis. Distingua verificado agora, evidência anterior ainda aplicável, informado e não verificado.

## Produto, decisões e cobertura

- Todos os itens do trecho têm aceite verificável, dependências e documentos canônicos identificados?
- PRD, Roadmap, arquitetura e decisões concordam? Prioridades/exclusões estão explícitas? Referências apontam para seções e IDs reais?
- Há decisões de comportamento, contrato, métrica ou autorização que o executor teria de inventar? Registre-as antes de começar.
- Monte uma linha por entrega/pacote, com implementação prevista, dependências, validação e gate final. Não crie TaskPlans futuros: o resultado aqui é cobertura de pré-requisitos.

## Código e contratos

- Leia os pontos reais de entrada, consumidores, serviços, modelos e testes relacionados a cada alteração. Para componentes novos, confirme os pontos existentes de integração.
- Confira contratos entre repositórios: campos, estados, códigos de erro, versões, autenticação, efeitos assíncronos e compatibilidade durante rollout.
- Identifique biblioteca/runtime/gerador exigidos e suas restrições. Não escolha outra arquitetura sem a decisão correspondente.
- Relacione tarefas que modificam arquivos compartilhados e a ordem necessária. Detecte ciclos de dependência e dependências em trabalho não aprovado.
- Defeitos que são o próprio objeto da iniciativa pertencem à execução; defeitos externos que impedem desenvolver ou validar precisam de preparação ou revisão explícita do escopo.

## Repositórios, worktrees e preservação

- Repositórios, branches base e revisões existem e estão acessíveis? Confira alterações locais para evitar tratá-las como base limpa.
- Verifique estratégia de isolamento e referências reais de `.git`, dependências e artefatos. Uma worktree em outra pasta pode continuar dependendo de metadados e links no local original.
- Confira disponibilidade local dos arquivos, armazenamento, espaço e caminhos de documentos/evidências; não presuma que arquivos ignorados pelo Git aparecerão em um clone/worktree novo.
- Registre branches empilhadas, ordem de integração e responsáveis; se push/CI fazem parte do trecho, verifique acesso de leitura/configuração e identifique limites não comprováveis sem escrita.
- Ausência de erro em `git status` não certifica build, testes ou permissões de publicação.

## Jira e branches — Valeti

- Leia [valeti-jira-delivery](../../valeti-jira-delivery/SKILL.md). Confirme por leitura Rovo MCP, usuário/accountId, site/projeto/Board, tipos Task/Subtask e metadados exigidos; não teste permissões criando cards em Plan mode.
- Identifique vínculos existentes do ROADMAP com Tasks pais, responsáveis e duplicidades/ambiguidades; planeje criar os faltantes fora do Plan mode antes de código. TASKPLANs futuros e Subtasks ainda não planejadas são entregas internas sequenciadas, não lacunas externas.
- Verifique prefixo, base e branches/PRs existentes no Bitbucket. Planeje `<prefixo>/<CHAVE-DA-TASK-PAI>` compartilhada por pai/repositório, inclusive para saneamento de código; não use branches por Subtask ou por agente.
- Registre o agente responsável pela sincronização, limites de assignee, configuração real de status/colunas e gates de DONE. Acesso desconhecido continua não verificado; preparação não autoriza reatribuir issues, mudar workflow ou iniciar escrita.

## Runtime, dependências e infraestrutura

- Versões reais de runtime e package manager, lockfile, binários locais, dependências nativas, arquitetura da máquina e imagens necessárias.
- Comandos de instalação/build/início e seus efeitos; existência de serviços, redes, portas, volumes, workers e filas necessários.
- Configuração e credenciais por mecanismo existente, sem revelar valores. Verifique destino e identidade/escopo acessível quando a operação de leitura permitir.
- Saúde/conectividade de recursos preexistentes, disponibilidade de portas e capacidade de disco para o procedimento planejado. Recursos ainda não provisionados não ficam prontos pela existência de IaC.
- Serviços a construir pelo Roadmap entram como dependência interna; ambiente externo que precisa existir para construí-los/validá-los é pré-requisito.

## Banco e dados

- Leia schema, migrações, seeds, versão do banco, extensões e permissões necessárias; compare com metadados do ambiente autorizado quando acessíveis.
- Distinga schema que deveria existir antes de começar de migrações que são entregas aprovadas do Roadmap.
- Verifique viabilidade de banco isolado, fixtures, seed, rollback e limpeza. Registre efeitos fora de transação e a necessidade de outra conexão/worker.
- Consultar via SELECT não comprova autorização/capacidade de executar DDL ou escrever. Use metadados de privilégios quando disponíveis; se uma capacidade obrigatória continuar desconhecida, registre INCONCLUSIVO.
- Imagens, arquivos de teste e dados representativos estão disponíveis e autorizados para os testes exigidos? Não substitua uma evidência real obrigatória por dados sintéticos sem fundamento no aceite.

## Testes, UI, API e linha de base

- Leia configuração e scripts de testes/lint/typecheck/build para saber o que cobrem, quais serviços usam e se produzem efeitos. Não rode testes destrutivos por presumir que são verificações de leitura.
- Obtenha uma linha de base executada e vinculada à revisão. Reuse evidência pertinente quando verificável; se a execução necessária não couber no Plan mode, prepare a verificação e peça sua realização autorizada antes do veredito PRONTO.
- Registre falhas por identidade e cenário, não só por quantidade. Se o gate exige suíte verde e a base falha, resolver a preparação ou uma alteração explícita aprovada do contrato antes de liberar. Não adotar “sem falhas novas” por conta própria.
- Para jornadas de UI, confira ferramenta de navegador/automação, conta, papel, rota e ambiente. Para APIs, cliente, destino, autenticação, payload de teste e observação dos efeitos.
- Para integração real, confira disponibilidade dos dois lados, callbacks, redes, certificados e dados necessários. Um mock só sustenta o trecho que realmente verifica.
- Não tente executar uma funcionalidade que ainda será construída como condição de início. Comprove a infraestrutura de validação e defina o cenário futuro; marque a implementação futura como entrega interna.

## Revisão, publicação e critérios externos

- O revisor existe no ambiente e tem ferramentas/acesso necessários? Quem aprova cada gate? Que gates humanos foram explicitamente delegados?
- CI pode rodar os testes exigidos? Existem pipeline, runner, variáveis por referência, ambiente e acesso necessários? Configuração presente não comprova um futuro run verde.
- Quem cria PR, faz merge, deploy e valida em HML/produção? Uma entrega dependente de ação humana é checkpoint previsto, não autonomia contínua até o fim.
- Hardware, contas de parceiro, janela operacional e responsáveis estarão disponíveis quando exigidos? Agendamento ou promessa não comprovam disponibilidade atual; identifique o checkpoint ou mantenha pendência conforme a exigência do trecho.
- Ferramentas e permissões podem gerar prompts mesmo quando o usuário autorizou o trabalho. Identifique regras concretas de bloqueio, autenticação pendente e limites observáveis; não altere permissões ou orçamento para remover a barreira.

## Saneamento e validade

Para cada falha: IDs afetados, causa/evidência, ação concreta, responsável, dependências, necessidade de escrita, critério de fechamento e como verificar depois. Preserve histórico quando resolvida.

O relatório é válido para a base e ambiente registrados. Mudanças de contrato, revisão relevante, credencial, disponibilidade ou método de teste exigem revalidar as linhas afetadas. Não invente prazo fixo de validade para todos os tipos de evidência.
