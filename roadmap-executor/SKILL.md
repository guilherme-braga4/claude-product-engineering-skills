---
name: roadmap-executor
description: "Execute a preflighted, approved PRD and roadmap iteratively, planning one phase at a time, implementing, reviewing, and validating the running product through its UI, APIs, database, and tests. Use to start or resume execution with an agreed scope and review policy; route unresolved preparation to roadmap-executor-pre-check-deps."
---

# Roadmap Executor

Conduza a execução de uma iniciativa refinada, aprovada e preparada. Planeje uma fase por vez, implemente, obtenha evidências, corrija falhas e avance até o limite autorizado. O scan completo de pré-requisitos pertence à `roadmap-executor-pre-check-deps`; aqui, consuma seu handoff e mantenha a continuidade da implementação.

## 1. Receba o pre-check e confira sua validade

1. Leia as instruções locais e identifique PRD, Roadmap e base aprovada. Localize o relatório de `roadmap-executor-pre-check-deps` informado pelo usuário ou referenciado no acordo/estado, inclusive quando ainda estiver no arquivo de plano do runtime. Templates não equivalem a aprovação.
2. O relatório deve cobrir todo o trecho autorizado, ter veredito PRONTO e registrar evidências, decisões, dependências internas, checkpoints e autoridade. Relatório PENDENTE/INCONCLUSIVO não libera implementação. Sem relatório suficiente, encaminhe a preparação à `roadmap-executor-pre-check-deps` em Plan mode antes de implementar; leia seu SKILL.md quando disponível. Se ausente, informe a entrada necessária sem fingir que o scan ocorreu ou instalar ferramentas automaticamente.
3. Faça uma conferência curta da validade: escopo/revisões, estado real do Git e recursos voláteis relevantes. Reutilize as evidências válidas e as respostas já dadas. Não repita o scan inteiro nem reabra decisões por trocar de sessão. Mudanças materiais voltam à pré-checagem apenas nas linhas afetadas.
4. Leia Discovery, Brain Dump e arquitetura conforme a tarefa exigir. Hipóteses não viram decisões aprovadas. Use a receita de ambiente/validação do relatório; siga [validação do produto em execução](references/runtime-validation.md) durante a implementação.
5. Recupere o acordo e estado existentes. Se o relatório estiver apenas no artefato de plano, persista uma cópia identificada no local canônico do projeto quando o modo e o escopo já permitirem, sem modificar a versão aprovada. Registre a referência no acordo/estado.

**Execuções já iniciadas antes deste pre-check:** não resete entregas nem recomece a fase para criar um documento novo. Um conjunto existente de acordo, TaskPlan, evidências e estado pode servir de handoff equivalente se comprovar os mesmos pré-requisitos. Registre a equivalência e revalide o necessário; lacunas reais do trabalho restante voltam à pré-checagem. Ausência de um nome de arquivo específico não é bloqueio por si só.

O TaskPlan não é pré-requisito de entrada. Sua criação detalha decisões aprovadas. Arquitetura formal é opcional: use os registros técnicos e de rastreabilidade definidos na preparação. Uma decisão substantiva pendente volta ao pre-check; não invente seções de ARCH nem métricas de aceite. Componentes a construir pelo próprio Roadmap são dependências internas sequenciadas, não recursos que obrigatoriamente precisavam existir antes do início.

## 2. Estabeleça o acordo de execução

Use [acordo de execução](references/execution-agreement.md) para consolidar as escolhas já aprovadas no pre-check: alcance, checkpoints, revisão, ações de Git, ambientes e validações permitidas. Não faça outra rodada geral de permissões. Se uma escolha obrigatória foi omitida, registre a lacuna e resolva somente ela antes do trabalho dependente.

Persista o acordo no projeto antes da primeira implementação. Autorizações continuam válidas após compactação, troca de branch ou reinício, desde que sua base, alcance e condições não tenham mudado. O acordo não altera permissões das ferramentas nem supera bloqueios do ambiente.

Se uma revisão humana for obrigatória nos documentos, só substitua os gates nomeados quando o usuário delegar explicitamente essa revisão. Registre revisão por agente como tal. Uma simulação não substitui validação humana, de hardware ou de produção requerida.

## 3. Planeje somente a fase executável atual

Em projetos da Valeti, leia e aplique [valeti-jira-delivery](../valeti-jira-delivery/SKILL.md) antes de planejar a implementação. Primeiro reconcilie cada item do ROADMAP autorizado com sua Task pai via Rovo MCP; depois leia/crie o TASKPLAN e vincule cada item a uma Subtask desse pai. O nome do item do ROADMAP é o summary da Task. Não produza código nem crie branch sem os cards verificados. Se o protocolo não estiver instalado, localize a fonte versionada ou informe a dependência antes de implementar; não omita o gate.

1. Reconcile o estado real com o Roadmap. Selecione a próxima fase autorizada com dependências satisfeitas.
2. Confira se as pré-condições registradas permanecem válidas e se as entregas internas das quais a fase depende foram comprovadas. Crie ou atualize o TaskPlan usando o template local; na ausência dele, use [o template desta skill](assets/TASKPLAN-TEMPLATE.md). Não repita a preparação integral a cada fase.
3. Referencie RN/UC/RF e Qualidades do PRD, e RNF-T da arquitetura quando existirem. Não duplique requisitos ou recicle IDs. Delimite exclusões expressamente aprovadas.
4. Defina tarefas revisáveis, aceite binário e como observar os efeitos relevantes no produto em execução. Arquivos esperados são orientações, não limitações artificiais à implementação.
5. Não escreva TaskPlans de fases futuras. O aprendizado desta fase deve informar a próxima.

Em Agent Teams, confirme o PRD antes de decompor ou delegar; cada participante lê o PRD e os documentos pertinentes. A tasklist interna coordena tarefas, dependências e ownership. `docs/TASKS.md` é apenas o espelho append-only do hook local: não o edite como fila. O TaskPlan documenta a fase e o estado persistido permite reconciliar a fila após reinício.

## 4. Execute, observe e corrija

Para cada tarefa:

1. Preserve alterações preexistentes e confira o estado do Git. Use a estratégia acordada de branches/worktrees; nunca descarte trabalho para trocar de branch. Na Valeti, use `<prefixo>/<CHAVE-DA-TASK-PAI>` (ex.: `feature/VWAD-1234`), compartilhada pelos itens do TASKPLAN; não crie branch/PR por Subtask. Tasks pais diferentes podem ter suas próprias branches e worktrees. Para paralelismo dentro do mesmo pai/repositório, siga o isolamento e a integração serial de `valeti-jira-delivery`, sem checkout concorrente da mesma branch ou reorganização automática das worktrees existentes. Em projetos fora da Valeti, use worktrees separados e ownership explícito conforme o acordo.
2. Implemente o comportamento referenciado e testes capazes de detectar sua ausência ou regressão.
3. Execute as verificações automatizadas pertinentes e o produto real quando o aceite envolver comportamento em execução. Siga [runtime-validation.md](references/runtime-validation.md) para UI, API, DB, logs e evidências.
4. Compare resultados esperados com observados. Investigue a causa, corrija e repita o cenário que falhou, ampliando testes conforme o impacto. Registre tentativas úteis para evitar repetir abordagens sem progresso.
5. Acione o revisor acordado com o PRD, TaskPlan, diff e evidências. Ele verifica código e força dos testes e pode executar verificações no ambiente autorizado. Achados pendentes retornam ao executor para correção e nova revisão.
6. Salve checkpoints e evidências vinculadas à revisão do código. Não marque aceite apenas porque o código foi escrito ou porque o agente afirmou que está pronto.

O revisor deve ter contexto próprio e conhecer os critérios originais. Não forneça a conclusão desejada como instrução de avaliação. Não atribua identidade ou aprovação a um revisor que não foi executado. Se a delegação não estiver disponível, use a alternativa autorizada ou registre o bloqueio.

## 5. Feche a fase pelo gate

Use [gates de fase](references/phase-gates.md), preservando os requisitos mais específicos do projeto. Integre conforme autorizado e valide o estado integrado. Uma aprovação anterior não cobre alterações posteriores automaticamente.

Na Valeti, o agente responsável pela sincronização reconcilia pai e Subtasks do trecho com as evidências e transições reais do Board, conferindo o assignee antes de cada escrita. Atualiza somente os cards do usuário confirmado, inclusive ao encerrar com bloqueio ou checkpoint. Review/merge pendentes não viram DONE. Registre status/coluna confirmados e pendências remotas antes de declarar o fechamento.

Após o gate passar, registre retrospectiva e próxima ação. No modo por fase, aguarde a liberação acordada. No modo contínuo, crie o próximo TaskPlan sem pedir a mesma autorização novamente.

## 6. Persista e retome

Use a organização existente do projeto; se não houver estado de retomada, adapte [EXECUTION-STATE-TEMPLATE.md](assets/EXECUTION-STATE-TEMPLATE.md). Mantenha o acordo e o estado fora de diretórios efêmeros. Use um local canônico acessível às branches/worktrees da iniciativa e registre o caminho.

Atualize estado em checkpoints relevantes: fase/tarefa, versões dos documentos, branch/worktree, commit, alterações não commitadas, validações, processos iniciados, dados criados, bloqueios e próxima ação. No `CLAUDE.md`, mantenha um ponteiro curto ao estado canônico, evitando cópias concorrentes.

Ao retomar, releia o acordo, os documentos e o estado; confira Git, código, processos, dados e evidências antes de reconstruir a fila. Resultado de teste antigo não comprova o código atual.

Na Valeti, recupere também o mapeamento ROADMAP → Task → TASKPLAN → Subtask → branch/PR e releia os cards pelo Rovo MCP. Preserve suas chaves; não recrie cards ou sobrescreva mudanças humanas a partir de estado antigo.

## 7. Continuidade e encerramento

Esta skill define o procedimento; não inicia por si só um supervisor persistente. Após prontidão e acordo, formule uma condição de `/goal` para o trecho autorizado, incluindo os gates e checkpoints. Se o ambiente não permitir ativá-lo diretamente, forneça o comando ao usuário sem alegar que o loop foi ativado. `/goal` não reinicia um processo encerrado nem substitui a validação independente.

Corrija autonomamente falhas de implementação/testes dentro do acordo: elas fazem parte da iteração e não justificam retornar ao planejamento geral. Um componente ainda não construído, mas previsto e sequenciado no Roadmap, também pertence à execução. Checkpoints humanos registrados são pausas previstas. Se surgir um pré-requisito externo ausente, contrato incompatível ou descoberta que invalide decisão aprovada, registre o delta como nova revisão do relatório, preservando a aprovada, e retorne à `roadmap-executor-pre-check-deps` apenas para o trecho afetado. Continue trabalho independente autorizado enquanto possível. Não enfraqueça requisitos, pule fases dependentes ou amplie escopo para contornar um bloqueio.

Pare no limite acordado, no checkpoint humano, em bloqueio sem trabalho independente ou ao atingir um limite de execução configurado. Esses estados não significam conclusão. Considere o trecho concluído apenas com seus gates satisfeitos; declare o Roadmap completo somente se todo o seu escopo aprovado e a validação global do sistema integrado tiverem sido atendidos.

Entregue um resumo com fases concluídas, evidências, código validado, revisão realizada, desvios e pendências reais. Declare explicitamente o que não pôde ser verificado.
