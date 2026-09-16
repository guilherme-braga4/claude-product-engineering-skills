# Prompt — execução do Roadmap completo

Use este prompt em uma nova sessão de execução, depois que o pre-check tiver sido aprovado com o veredito `PRONTO`. Substitua os caminhos entre colchetes antes de enviar:

```text
/roadmap-executor

Execute 100% do Roadmap aprovado em @[CAMINHO_DO_ROADMAP], usando como handoff obrigatório o relatório de pre-check aprovado em @[CAMINHO_DO_RELATORIO_DE_PRE_CHECK].

Use também como fontes canônicas:
- PRD aprovado: @[CAMINHO_DO_PRD]
- Arquitetura e decisões técnicas, quando existirem: @[CAMINHO_DA_ARQUITETURA_OU_DAS_DECISOES]
- Demais documentos aplicáveis: @[CAMINHOS_ADICIONAIS]

Antes da primeira alteração, confira brevemente se o escopo, as revisões dos documentos, o estado do Git e os recursos voláteis relevantes ainda correspondem ao relatório. Reutilize todas as decisões, autorizações, evidências, branches/worktrees, ambientes, procedimentos de validação e checkpoints já aprovados. Não repita o pre-check inteiro nem reabra decisões sem mudança material.

Trabalhe continuamente até concluir todas as fases e o gate global do Roadmap. Para cada fase, crie ou atualize somente o TaskPlan da fase executável atual; implemente cada tarefa; escreva testes capazes de detectar ausência ou regressão do comportamento; revise o código e a força dos testes; execute o produto real; valide os critérios aplicáveis pela UI, API, banco de dados, logs e testes automatizados; corrija as falhas encontradas; registre evidências; e somente então feche o gate e avance automaticamente para a próxima fase.

Use a estratégia de branches, worktrees, commits, push, revisão, integração e publicação definida no acordo e no relatório. Preserve alterações preexistentes e nunca descarte trabalho para trocar de branch. Mantenha o acordo e o estado de execução em local canônico, atualizando fase, tarefa, commit, branch/worktree, alterações não commitadas, processos, dados criados, verificações executadas, evidências, bloqueios e próxima ação em checkpoints relevantes. O estado deve permitir retomada segura após compactação, outage ou nova sessão.

Corrija autonomamente problemas de implementação, testes, integração e ambiente que estejam dentro do escopo e das autorizações existentes. Uma entrega ainda não construída, mas prevista em fase anterior do Roadmap, é trabalho da execução e não um blocker de preparação.

Se surgir uma mudança material ou um pré-requisito externo novo, registre exatamente o delta e retorne ao /roadmap-executor-pre-check-deps somente para o trecho afetado. Continue todo trabalho independente autorizado enquanto isso for possível. Não reduza escopo, enfraqueça critérios, pule fases dependentes ou transforme falha em ressalva para avançar.

Respeite os checkpoints humanos ou externos explicitamente registrados. Fora deles, não pare para pedir revisões intermediárias já delegadas nem repita autorizações persistidas. Pare apenas quando:
- alcançar um checkpoint obrigatório;
- existir um bloqueio externo novo sem qualquer trabalho independente possível;
- atingir um limite real da ferramenta ou da conta;
- ou concluir 100% do Roadmap e sua validação global integrada.

Não declare conclusão parcial como sucesso. Considere uma fase concluída somente com todos os seus aceites e gates comprovados. Considere o Roadmap 100% concluído somente quando todo o escopo aprovado estiver implementado, integrado, revisado e validado de fora, com a suíte aplicável verde, a rastreabilidade atualizada e nenhuma pendência obrigatória aberta.

Ao final, entregue um resumo verificável contendo fases concluídas, commits e branches, revisões realizadas, testes e validações em execução, evidências dos gates, desvios aprovados e qualquer item que não pôde ser verificado. Se tudo estiver comprovado, declare explicitamente que 100% do Roadmap aprovado foi concluído.
```

Se o relatório liberar somente um intervalo do Roadmap, substitua “100% do Roadmap” pelo trecho exato aprovado. Se não houver arquitetura formal ou documentos adicionais, remova essas linhas; não invente fontes nem decisões.
