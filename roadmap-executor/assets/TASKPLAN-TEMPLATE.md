# TaskPlan — Fase [N]: [Nome]

> Preencher somente a fase atual. Referenciar requisitos por ID, sem duplicá-los. Usar o template local do projeto quando existir.

## Contexto

- Roadmap e fase: [referência e revisão]
- Alterações do PRD: [IDs da §7, quando aplicável]
- RN/UC/RF e Qualidades tocados: [IDs / §6.X]
- Arquitetura e RNF-T: [referências existentes ou registro técnico equivalente]
- Acordo de execução: [referência, revisor e gates delegados]
- Pré-condições verificáveis: [condições e evidências]
- Branch/worktree de trabalho e destino de integração: [referências]

## Tarefas

### TASK-01: [Verbo + objeto]

- Sustenta: [IDs do PRD e decisões técnicas]
- Dependências: [tarefas / condições]
- Arquivos esperados: [orientação]
- Aceite binário:
  - [ ] [comportamento verificável]
- Verificação: [teste ou cenário real e resultado esperado]
- Evidência: [referência ao resultado e à revisão de código validada]
- Notas: [somente restrições não óbvias]

[Repetir para as tarefas necessárias à fase.]

## Cenários no projeto em execução

| Cenário / requisito | Pré-condições e fixture | Ação UI/API/etc. | Resultado esperado e efeito no DB/serviço quando aplicável | Evidência / status |
|---|---|---|---|---|
| [ID] | [estado] | [ação real] | [asserções] | [resultado] |

- Receita do ambiente: [referência a comandos e serviços]
- Dados e efeitos externos autorizados: [referência ao acordo]
- Limpeza: [recursos da execução e procedimento]

## Gate de saída

- [ ] Todas as tarefas com aceite comprovado e revisão acordada concluída.
- [ ] Suíte completa verde; nenhum teste omitido ou enfraquecido para passar.
- [ ] Testes novos e mocks revisados quanto à capacidade de detectar regressões.
- [ ] Cenários aplicáveis executados no produto real, com evidências.
- [ ] Matriz de rastreabilidade atualizada; todo requisito tocado validado, incluindo validações alternativas executadas.
- [ ] Código integrado e validações pertinentes confirmadas no estado integrado.
- [ ] Estado, Discovery Log e decisões técnicas atualizados conforme aplicável.
- [ ] Critério de sucesso da fase verificado de fora.
- [ ] Revisões humanas obrigatórias realizadas, ou gates especificamente delegados revisados pelo agente identificado.

## Rollback

[Referência ao procedimento aprovado, gatilhos e efeitos sobre dados.]

## Retrospectiva pós-fase

- Funcionou bem: [observações]
- Fricção: [observações]
- Aprendizado para a próxima fase: [ajustes dentro do escopo]
- Candidato a melhoria do método: [proposta; não alterar automaticamente a skill global]
