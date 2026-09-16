# Pré-checagem de dependências — [Iniciativa / trecho]

> Relatório anterior à implementação. Preencher a partir das verificações; placeholders, promessas e procedimentos ainda não executados não comprovam prontidão. Em Plan mode, usar o artefato de plano permitido pelo runtime; exportar ao projeto somente quando permitido. Preservar a revisão anterior ao atualizar.

## 1. Base e alcance

- ID / revisão / data do relatório: [identificação]
- Local canônico deste relatório: [caminho real; se ainda apenas na conversa, declarar]
- PRD aprovado: [caminho, revisão/hash e referência da aprovação]
- Roadmap aprovado: [caminho, revisão/hash e referência da aprovação]
- Alcance: [fase / intervalo / Roadmap completo]
- Outros documentos e decisões aplicáveis: [referências]
- Repositórios e bases: [paths, branches, commits e alterações locais relevantes]
- Ambiente(s): [identificação não secreta]
- Acordo existente ou decisões de execução registradas aqui: [referências]
- Trabalho já concluído, se for execução em andamento: [referências; preservar]

## 2. Veredito e continuidade

- Pré-requisitos: [PRONTO / PENDENTE / INCONCLUSIVO]
- Continuidade: [CONTÍNUA NO TRECHO / COM CHECKPOINTS / ainda indefinida]
- Justificativa baseada em evidências: [conclusão]
- Trecho efetivamente liberado: [mesmo alcance aprovado ou nenhum]
- Aprovação das conclusões e escolhas: [resposta/referência real ou pendente]
- Próxima ação: [ação e responsável]

PRONTO significa condições de execução comprovadas, não funcionalidades futuras implementadas nem ausência garantida de imprevistos. Pendência obrigatória e área necessária não verificada impedem PRONTO.

## 3. Cobertura de todas as entregas

| Fase / entrega | IDs de requisito | Código / contratos inspecionados | Dependências / ordem | Build / testes / validação real prevista | Revisão / entrega / gate | Resultado da pré-checagem / evidências |
|---|---|---|---|---|---|---|
| [item] | [IDs] | [referências reais ou pontos de integração para código novo] | [DEP-IDs / produtor] | [receita, recursos e cenário futuro] | [responsável e critério] | [resultado] |

Cobertura: [itens examinados / total do trecho]. Lacunas: [itens não examinados ou nenhuma]. Áreas não aplicáveis: [justificativa por área]. Não criar TaskPlans futuros aqui.

## 4. Inventário e verificações

| Área / recurso | Destino e revisão | Verificação permitida / evidência anterior aplicável | Resultado observado | Data | Lacuna ou validade |
|---|---|---|---|---|---|
| [runtime / Git / DB / infraestrutura / UI / API / CI / revisão / dados] | [identificação sem segredo] | [comando sanitizado ou referência] | [observação, não expectativa] | [data] | [conclusão] |

### Linha de base da qualidade

| Repositório / commit | Verificação | Resultado e identidade das falhas | Gate exigido | Tratamento aprovado / evidência |
|---|---|---|---|---|
| [referência] | [suíte / lint / tipos / build] | [evidência ou NÃO VERIFICADO] | [critério] | [correção, exceção explicitamente aprovada ou pendência] |

## 5. Dependências e saneamento

| ID | Entregas afetadas | Classe | Condição e evidência atual | Ação necessária / responsável | Pré-dependências | Critério de fechamento | Estado / evidência final |
|---|---|---|---|---|---|---|---|
| DEP-001 | [itens] | [externa / entrega interna / checkpoint / fora do escopo justificado] | [fato] | [procedimento concreto; indicar escrita e autorização necessária] | [IDs ou nenhuma] | [como comprovar] | [aberta / resolvida / interna sequenciada / checkpoint acordado / não aplicável justificado] |

Contagem de pendências externas obrigatórias: [n]. Decisões necessárias abertas: [n]. Verificações necessárias inconclusivas: [n]. Dependências internas sem produtor/ordem executável: [n]. Todas precisam ser zero para PRONTO.

Uma entrega interna sequenciada não está implementada por constar nesta tabela. Um checkpoint acordado também não está realizado: ele limita a continuidade conforme a seção seguinte.

## 6. Checkpoints e autoridade

| Momento / gate | Ação | Responsável | Autorização existente | O executor pode fazer sozinho? | Condição de liberação |
|---|---|---|---|---|---|
| [fase / etapa] | [revisão / PR / merge / deploy / hardware] | [quem] | [referência] | [sim/não e limite] | [evidência necessária] |

Se o pedido exigir execução ininterrupta e houver “não” dentro do trecho, resolver essa incompatibilidade antes de PRONTO. Não tratar autorização para código como autorização para publicação ou ações de dados.

## 7. Registro das rodadas

| Pergunta / DEP-ID | Evidência e opções consideradas | Decisão / resposta | Fonte da aprovação | Impacto e verificação posterior |
|---|---|---|---|---|
| [ID] | [resumo] | [resposta real] | [referência] | [áreas rechecadas e evidência] |

## 8. Handoff para roadmap-executor

- Escopo liberado e referências de aprovação: [referências]
- Ordem das dependências internas: [produtores → consumidores]
- Receita verificada de ambiente e validação: [comandos/referências sem credenciais]
- Revisor e gates delegados/humanos: [referências]
- Git, publicação, ambientes e operações de dados autorizadas: [acordo existente ou respostas registradas]
- Local de estado/checkpoints/evidências: [acessível entre sessões e worktrees]
- Condições voláteis a conferir no início: [acesso, saúde, disco, revisão relevante etc.]
- Condições que invalidam conclusões: [mudanças materiais e linhas afetadas]
- Limitações e riscos residuais aprovados: [evidências; não listar bloqueios obrigatórios como ressalvas]
- Transição para execução já solicitada? [referência explícita ou não]
- Comando sugerido, somente se PRONTO: `/roadmap-executor [trecho aprovado] @[roadmap] @[caminho real deste relatório]`.
