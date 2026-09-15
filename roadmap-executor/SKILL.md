---
name: roadmap-executor
description: "Execute an approved PRD and roadmap iteratively, planning one phase at a time, implementing, reviewing, and validating the running product through its UI, APIs, database, and tests. Use to start or resume roadmap execution with an agreed scope and review policy."
---

# Roadmap Executor

Conduza a execução de uma iniciativa refinada e aprovada. Planeje uma fase por vez, implemente, obtenha evidências, corrija falhas e avance até o limite autorizado.

## 1. Verifique prontidão antes de implementar

1. Leia as instruções locais e identifique os documentos canônicos. PRD e Roadmap aprovados são obrigatórios; templates com placeholders não equivalem a documentos aprovados.
2. Leia Discovery, Brain Dump e ARCH AS-IS/TO-BE quando existirem. Hipóteses do Brain Dump não equivalem a decisões aprovadas. O AS-IS descreve comportamento observado; o TO-BE define o destino.
3. Confira escopo, critérios de aceite, dependências e aprovações do trecho pretendido. Não inicie com pontos em aberto que afetem sua execução. Apresente lacunas concretas para refinamento, sem implementar com suposições de produto.
4. Inspecione o código e os recursos necessários para executar e validar o projeto. Identifique comandos, serviços, dados de teste, acesso à interface, APIs e banco aplicáveis. Siga [validação do produto em execução](references/runtime-validation.md).
5. Procure um acordo e estado de execução existentes. Reutilize autorizações compatíveis com o escopo atual; não repita perguntas já respondidas.

O TaskPlan não é pré-requisito de entrada. Sua criação detalha decisões aprovadas. Arquitetura formal é opcional: se faltar, use registros técnicos e de rastreabilidade existentes ou crie um registro proporcional antes de implementar. Uma decisão substantiva ainda pendente exige refinamento; não invente seções de ARCH nem métricas de aceite.

## 2. Estabeleça o acordo de execução

Use [acordo de execução](references/execution-agreement.md) para resolver apenas escolhas ainda indefinidas: alcance, checkpoints, revisão, ações de Git, ambientes e validações permitidas.

Persista o acordo no projeto antes da primeira implementação. Autorizações continuam válidas após compactação, troca de branch ou reinício, desde que sua base, alcance e condições não tenham mudado. O acordo não altera permissões das ferramentas nem supera bloqueios do ambiente.

Se uma revisão humana for obrigatória nos documentos, só substitua os gates nomeados quando o usuário delegar explicitamente essa revisão. Registre revisão por agente como tal. Uma simulação não substitui validação humana, de hardware ou de produção requerida.

## 3. Planeje somente a fase executável atual

1. Reconcile o estado real com o Roadmap. Selecione a próxima fase autorizada com dependências satisfeitas.
2. Verifique as pré-condições e crie ou atualize o TaskPlan usando o template local; na ausência dele, use [o template desta skill](assets/TASKPLAN-TEMPLATE.md).
3. Referencie RN/UC/RF e Qualidades do PRD, e RNF-T da arquitetura quando existirem. Não duplique requisitos ou recicle IDs. Delimite exclusões expressamente aprovadas.
4. Defina tarefas revisáveis, aceite binário e como observar os efeitos relevantes no produto em execução. Arquivos esperados são orientações, não limitações artificiais à implementação.
5. Não escreva TaskPlans de fases futuras. O aprendizado desta fase deve informar a próxima.

Em Agent Teams, confirme o PRD antes de decompor ou delegar; cada participante lê o PRD e os documentos pertinentes. A tasklist interna coordena tarefas, dependências e ownership. `docs/TASKS.md` é apenas o espelho append-only do hook local: não o edite como fila. O TaskPlan documenta a fase e o estado persistido permite reconciliar a fila após reinício.

## 4. Execute, observe e corrija

Para cada tarefa:

1. Preserve alterações preexistentes e confira o estado do Git. Use a estratégia acordada de branches/worktrees; nunca descarte trabalho para trocar de branch. Em trabalho paralelo, use worktrees separados e ownership explícito.
2. Implemente o comportamento referenciado e testes capazes de detectar sua ausência ou regressão.
3. Execute as verificações automatizadas pertinentes e o produto real quando o aceite envolver comportamento em execução. Siga [runtime-validation.md](references/runtime-validation.md) para UI, API, DB, logs e evidências.
4. Compare resultados esperados com observados. Investigue a causa, corrija e repita o cenário que falhou, ampliando testes conforme o impacto. Registre tentativas úteis para evitar repetir abordagens sem progresso.
5. Acione o revisor acordado com o PRD, TaskPlan, diff e evidências. Ele verifica código e força dos testes e pode executar verificações no ambiente autorizado. Achados pendentes retornam ao executor para correção e nova revisão.
6. Salve checkpoints e evidências vinculadas à revisão do código. Não marque aceite apenas porque o código foi escrito ou porque o agente afirmou que está pronto.

O revisor deve ter contexto próprio e conhecer os critérios originais. Não forneça a conclusão desejada como instrução de avaliação. Não atribua identidade ou aprovação a um revisor que não foi executado. Se a delegação não estiver disponível, use a alternativa autorizada ou registre o bloqueio.

## 5. Feche a fase pelo gate

Use [gates de fase](references/phase-gates.md), preservando os requisitos mais específicos do projeto. Integre conforme autorizado e valide o estado integrado. Uma aprovação anterior não cobre alterações posteriores automaticamente.

Após o gate passar, registre retrospectiva e próxima ação. No modo por fase, aguarde a liberação acordada. No modo contínuo, crie o próximo TaskPlan sem pedir a mesma autorização novamente.

## 6. Persista e retome

Use a organização existente do projeto; se não houver estado de retomada, adapte [EXECUTION-STATE-TEMPLATE.md](assets/EXECUTION-STATE-TEMPLATE.md). Mantenha o acordo e o estado fora de diretórios efêmeros. Use um local canônico acessível às branches/worktrees da iniciativa e registre o caminho.

Atualize estado em checkpoints relevantes: fase/tarefa, versões dos documentos, branch/worktree, commit, alterações não commitadas, validações, processos iniciados, dados criados, bloqueios e próxima ação. No `CLAUDE.md`, mantenha um ponteiro curto ao estado canônico, evitando cópias concorrentes.

Ao retomar, releia o acordo, os documentos e o estado; confira Git, código, processos, dados e evidências antes de reconstruir a fila. Resultado de teste antigo não comprova o código atual.

## 7. Continuidade e encerramento

Esta skill define o procedimento; não inicia por si só um supervisor persistente. Após prontidão e acordo, formule uma condição de `/goal` para o trecho autorizado, incluindo os gates e checkpoints. Se o ambiente não permitir ativá-lo diretamente, forneça o comando ao usuário sem alegar que o loop foi ativado. `/goal` não reinicia um processo encerrado nem substitui a validação independente.

Corrija autonomamente problemas técnicos dentro do acordo. Se descobrir algo que invalide uma decisão aprovada, exija novo acesso ou exceda a autorização, registre o bloqueio e solicite somente a decisão necessária. Continue apenas trabalho independente autorizado. Não enfraqueça requisitos, pule fases dependentes ou amplie escopo para contornar um bloqueio.

Pare no limite acordado, no checkpoint humano, em bloqueio sem trabalho independente ou ao atingir um limite de execução configurado. Esses estados não significam conclusão. Considere o trecho concluído apenas com seus gates satisfeitos; declare o Roadmap completo somente se todo o seu escopo aprovado e a validação global do sistema integrado tiverem sido atendidos.

Entregue um resumo com fases concluídas, evidências, código validado, revisão realizada, desvios e pendências reais. Declare explicitamente o que não pôde ser verificado.
