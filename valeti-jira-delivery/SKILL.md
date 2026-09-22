---
name: valeti-jira-delivery
description: "Coordena entregas de código da Valeti entre ROADMAP, TASKPLAN, Jira via Rovo MCP e branches do Bitbucket. Use antes de implementar, corrigir ou retomar código da Valeti e ao reconciliar o estado final dos cards do usuário. Não cria cards como efeito de uma auditoria ou planejamento somente leitura, nem impõe o processo a projetos de outras organizações."
---

# Entrega de código da Valeti

Garanta a cadeia `item do ROADMAP → Task pai no Jira → TASKPLAN → Subtasks → branch do pai → evidências → status/coluna do Board`. A Task pai é a unidade de entrega e de branch; Subtasks dão visibilidade ao trabalho sem multiplicar branches e PRs.

## Quando aplicar

Leia este protocolo antes da primeira alteração de código da Valeti, inclusive bugs, testes novos, scripts, migrações, configuração executável, saneamento de pré-requisitos e lotes de Readiness aprovados. Identifique a organização pelas instruções do projeto, missão ou remote do Bitbucket; não aplique esta regra a outros projetos por mera disponibilidade do MCP.

Auditoria, elaboração de PRD/arquitetura e planejamento somente leitura preservam suas fronteiras: prepare o mapeamento, sem criar/editar cards ou branches. Em Plan mode, execute somente consultas permitidas e registre no plano o trabalho de escrita a fazer depois. Quando a implementação estiver autorizada, a criação/reutilização dos cards e a sincronização das tarefas do usuário integram este fluxo; não exija outra aprovação ritual. Isso não autoriza merge, deploy, mudança de responsável ou alteração das configurações do Board.

Antes de coordenar Agent Team, confirme o PRD da iniciativa com objetivo, escopo e aceite. Sem ele, pare antes de decompor ou delegar. Cada participante deve lê-lo. Jira e TASKPLAN não substituem a tasklist interna do time; `docs/TASKS.md` continua sendo apenas seu espelho append-only.

## 1. Confirme conexão, identidade e destino

1. Use o **Rovo MCP da Valeti**, preferindo `rovo-valeti` quando disponível. A identidade esperada é **guilhermebraga@valeti.com**, cujo accountId foi confirmado como `712020:0da228fc-2e83-4136-98a1-6e3be14ae662`. Consulte o usuário autenticado na conexão e compare seu accountId com esse valor antes de qualquer escrita; confira também o email quando exposto. Se houver divergência ou não for possível comprovar a identidade, bloqueie as escritas e solicite a autenticação correta, sem redefinir o usuário esperado a partir da sessão errada. Outra identidade só pode substituir esta por decisão explícita do usuário. Valide também o site; acesso a `valeti.atlassian.net` sozinho não comprova a conta correta. Não reutilize a identidade ou os recursos de outro conector Atlassian. “Minhas tarefas” significa `assignee.accountId` igual ao accountId esperado e confirmado, nunca reporter, criador, nome de exibição ou autor do commit.
2. Use o site `https://valeti.atlassian.net` e confirme projeto/Board da iniciativa. `VWAD` e Board `59` são referências usuais, não autorização para ignorar outro destino explícito. Registre site/cloudId, projeto, Board, accountId e agente responsável pela sincronização no acordo/estado do projeto; não grave credenciais.
3. Consulte tipos e campos obrigatórios para criar **Task** e **Subtask**, a configuração de colunas/status do Board e as transições disponíveis de cada issue quando for movê-la. Resolva nomes localizados e IDs reais; não fixe IDs de tipo, status ou transição na skill.
4. Use ferramentas primárias disponíveis; para operações ausentes, use `discover` e o executor de leitura/escrita indicado no resultado. Não invente nomes de operações. Se acesso, identidade ou metadados indispensáveis não puderem ser confirmados, bloqueie a escrita dependente e preserve o estado para retomada.

## 2. Leia/crie o ROADMAP e reconcilie Tasks pais

- Reutilize o ROADMAP canônico e os IDs estáveis de seus itens. Se não existir, crie um Roadmap proporcional ao escopo já autorizado, com nome, resultado, aceite e dependências por item; não invente aprovação nem altere requisitos. Uma correção pequena pode ter um único item. No executor que exige Roadmap aprovado, cumpra esse gate antes de iniciar execução.
- Para cada item do trecho autorizado, procure o vínculo persistido com Jira e valide a issue. Sem vínculo, busque candidatos no projeto por referência estável da iniciativa/item e título; confira conteúdo, tipo e responsável. O **summary da Task deve ser o nome do item do ROADMAP**. Sem ambiguidade e com correspondência comprovada, reutilize o card; não duplique só porque mudou a sessão ou o título.
- Crie a Task faltante via Rovo MCP no projeto confirmado, atribuída ao usuário confirmado. Inclua referência estável da iniciativa e item, objetivo, escopo, aceite e referência ao ROADMAP/PRD na descrição. Persistir imediatamente a chave e URL retornadas. Caminho local é referência textual, não URL acessível pelo Jira.
- Task existente de outro responsável ou sem responsável não pode ser apropriada, reatribuída ou duplicada para contornar a restrição. Registre a divergência e resolva o vínculo/responsabilidade antes do desenvolvimento dependente. Tipo legado diferente de Task não deve ser convertido silenciosamente; registre e resolva a correspondência com o usuário.
- Se houver mais de um candidato plausível, resolva somente essa ambiguidade. Em timeout/resultado incerto de criação, pesquise novamente a referência estável antes de tentar outra criação; nunca repita uma escrita às cegas.

## 3. Leia/crie o TASKPLAN e reconcilie Subtasks

Depois de confirmar a Task pai, leia/crie o TASKPLAN do item executável atual, conforme os gates da skill chamadora. **Cada item de trabalho do TASKPLAN corresponde a uma Subtask daquele pai**, inclusive testes e validações quando forem itens próprios. Checklist de aceite dentro de um item não gera uma Subtask por checkbox.

Para cada item, use ID estável e título do TASKPLAN; reutilize a Subtask pelo vínculo persistido ou pela referência estável sob o pai, conferindo tipo, parent e responsável. Crie as faltantes com o pai real e assignee do usuário confirmado. Registre chave/URL assim que recebidas e valide a relação no Jira. Não crie Subtasks de Subtasks, pais por arquivo ou pais por subitem. Um TASKPLAN que abranja vários itens do ROADMAP deve explicitar o pai de cada item e separar suas branches.

Mudança de título conserva IDs e vínculo; ajuste o summary somente do card elegível da execução, preservando conteúdo humano. Item removido não autoriza excluir card nem encerrá-lo como concluído; registre a mudança e trate cancelamento conforme a decisão autorizada. Não crie TASKPLANs futuros apenas para preencher Jira antecipadamente.

Use [o registro de rastreabilidade](assets/JIRA-DELIVERY-TEMPLATE.md) dentro dos documentos existentes ou no estado canônico. Ele complementa os templates locais, não exige uma segunda fila.

## 4. Gate antes de produzir código e regra de branch

Antes de criar/trocar a branch ou iniciar cada item de código, confirme no Jira a Task pai e a Subtask correspondente, seus vínculos e responsáveis. Chaves propostas, placeholders, criação pendente e MCP indisponível sem verificação atual não satisfazem esse gate. Preparação documental independente pode continuar.

O nome é **`<prefixo>/<CHAVE-DA-TASK-PAI>`**, por exemplo `feature/VWAD-1234`. Preserve prefixos aprovados do Bitbucket para o repositório/tipo de entrega; use `feature/` para feature quando não houver outra convenção confirmada. A parte após o prefixo é exatamente a chave do pai, sem descrição, ID do TASKPLAN, chave de Subtask ou sufixo de agente. Não aplique o prefixo genérico `codex/` a esse fluxo quando a convenção Valeti exigir outro.

- Inspecione branches/PRs existentes e a base de integração no Bitbucket ou Git remoto acessível; registros históricos sem chave não dispensam a regra. A instrução explícita do usuário prevalece sobre exemplos antigos.
- Use **uma branch de entrega por Task pai e repositório**, compartilhada pelos itens de seu TASKPLAN; reutilize o PR aberto correspondente quando houver. Não abra um PR por Subtask. Em múltiplos repositórios, a mesma chave do pai identifica a branch em cada repo; PRs podem ser necessários por repo/destino autorizado.
- Confira `git status`, branch e `git worktree list --porcelain` antes de escrever. Reutilize a branch existente somente se corresponder à Task e à base correta. Preserve alterações alheias; não renomeie branches locais ou remotas, faça force-push, apague branches ou feche PRs históricos automaticamente para corrigir o padrão. Não mova, renomeie ou remova worktrees existentes automaticamente, inclusive as detached. Uma reorganização exige instrução explícita para os alvos concretos e preservação comprovada de commits e alterações não commitadas.
- Para trabalho legado fora do padrão, registre o mapeamento e prepare a continuidade na branch correta preservando o diff; conflito com branch/PR publicado requer decisão específica antes de uma migração destrutiva.
- Tasks pais diferentes podem ter suas próprias branches e worktrees. Dois worktrees não podem fazer checkout simultâneo da mesma branch. Dentro de um pai/repositório, serialize escritores na branch compartilhada ou use worktrees em detached HEAD com ownership de arquivos e integração serial pelo responsável. Registre caminho, pai/Subtask, base e commits de cada worktree; preserve os commits detached e comprove sua integração antes de qualquer limpeza explicitamente autorizada. Não use `--force` nem invente branches por Subtask/agente. Branches de integração como `master`/`homolog` mantêm seus nomes e seu papel.
- Cite pai/Subtask e evidências em commits/PRs conforme o padrão local, sem mudar autoria Git. Ter card e branch não amplia a autorização de push, PR, merge ou deploy.

## 5. Agente responsável pelo Jira e fechamento

Designe no acordo um **agente responsável pela sincronização do Jira**. Em execução individual, o próprio executor assume explicitamente o papel; em time, um participante identificado faz as escritas de status de forma serial. Os demais fornecem evidências. Não inicie um time só para cumprir esse papel nem afirme revisão/delegação inexistente.

Ao iniciar, bloquear, entregar para revisão e **ao fim do desenvolvimento**, esse agente reconcilia somente as chaves mapeadas no trecho executado. Não mova em massa todas as tarefas do usuário. Antes de **cada mutação**, releia o card e confira `assignee.accountId == usuário confirmado`, inclusive para cada Subtask e para o pai separadamente. Assignee vazio, diferente ou alterado durante a execução implica pular a escrita e registrar a pendência; não reatribua para torná-la elegível. Havendo controle de concorrência disponível, use-o; em conflito, releia e reavalie, sem sobrescrever outra atualização.

O Board é uma visualização do workflow: mova por **transição de status suportada** e confirme o status resultante e sua coluna pelo mapeamento atual. Não edite configuração de colunas, não trate ID de status como ID de transição e não invente uma operação separada de arrastar card. Respeite campos obrigatórios e resolução exigidos pela transição; não preencha valores fictícios. Se filtro/sprint excluir o card do Board, registre o motivo sem inserir em sprint ou alterar filtro automaticamente.

Use a configuração real do Board. No VWAD, estes nomes foram observados e devem ser revalidados na execução:

| Evidência de execução | Estado/coluna correspondente quando disponível |
|---|---|
| Planejado, ainda não iniciado | TO-DO |
| Desenvolvimento ou correção em andamento | IN PROGRESS |
| Impedimento real que impede continuar | BLOCK, com motivo e próxima ação no registro |
| Desenvolvimento validado, aguardando review/aceite/merge obrigatório | IN REVIEW |
| Todos os aceites, revisão, integração e demais gates de conclusão satisfeitos | DONE |

Subtask concluída não conclui o pai. O pai só vai para DONE quando todos os itens do TASKPLAN e os gates da entrega estiverem comprovados; considere também Subtasks existentes fora do recorte e pendências do pai. Não altere cards alheios para satisfazer esse fechamento. Trabalho escrito, testes isolados verdes, PR aberto ou fim de sessão não comprovam conclusão. Se a mudança exigir um caminho de transições intermediárias, verifique os efeitos e pré-condições; não passe por estados falsos só para chegar ao destino.

Atualize o estado local com resultado por card: status/coluna anterior e final, evidência, horário, agente, transição e eventual pendência. Releia após a escrita. Transição não disponível, perda de acesso ou falha mantém a sincronização pendente; não declare Jira atualizado. Na retomada, confira o estado remoto antes de repetir e não reverta alterações humanas para um checkpoint antigo. Falha de sincronização não apaga trabalho concluído; diferencie conclusão técnica, gates restantes e Jira pendente no handoff.

## Saída e retomada

Reporte Tasks/Subtasks e links, branches/PRs, gates e evidências, responsável pela sincronização e estados confirmados ou pendentes. Reutilize o mapeamento em retomadas e faça busca antes de qualquer recriação. Preserve PRD como fonte de requisitos, ROADMAP como escopo, TASKPLAN como plano e Jira como acompanhamento externo; nenhum deles substitui prova de execução.
