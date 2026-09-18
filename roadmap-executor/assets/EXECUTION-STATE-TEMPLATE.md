# Estado da execução — [Iniciativa]

> Adaptar ao registro existente. Guardar no projeto em local canônico acessível entre branches/worktrees. Não incluir credenciais.

## Base e autorização

- PRD aprovado: [caminho / revisão / referência de aprovação]
- Roadmap aprovado: [caminho / revisão / referência de aprovação]
- Documentos complementares: [referências]
- Pre-check ou handoff equivalente: [caminho / revisão / base / veredito; mudanças posteriores que exigem revalidar]
- Acordo de execução: [caminho canônico]
- Alcance autorizado: [fases]
- Continuidade prevista: [contínua no trecho / checkpoints acordados]
- Checkpoints e revisão: [regras / agente / gates humanos ou delegados]

## Posição atual

- Estado: [preparação / executando / validando / em revisão / aguardando humano / bloqueado / limite atingido / trecho concluído / roadmap concluído]
- Fase / TaskPlan / tarefa: [referências]
- Branch / worktree / commit: [referências]
- Alterações não commitadas: [descrição e localização]
- Última integração: [referência]
- Fila interna e ownership, se houver: [referências para reconciliação; docs/TASKS.md não é a fila]
- Próxima ação concreta: [ação]

## Jira e Bitbucket — Valeti (quando aplicável)

- Rovo MCP / site / cloudId / projeto / Board: [contexto confirmado]
- Usuário confirmado / accountId: [identidade verificada]
- Agente responsável pela sincronização: [identidade real]
- ROADMAP item → Task pai → TASKPLAN item → Subtask: [IDs estáveis, chaves e URLs, sem placeholders tratados como cards reais]
- Branch/PR por pai e repositório: [prefixo/CHAVE-DA-TASK-PAI / URL; compartilhados pelos itens do pai]
- Última reconciliação: [card / assignee relido / evidência / status e coluna confirmados / data]
- Escritas incertas ou pendentes e cards não elegíveis: [motivo e pesquisa a fazer antes de repetir]

## Ambiente e recursos da execução

- Receita e acesso não secreto: [referências]
- Serviços iniciados pelo executor: [comando / PID ou sessão / logs / porta]
- Fixtures e recursos criados: [identificadores]
- Limpeza realizada ou pendente: [estado / procedimento]

## Verificação e revisão

| Requisito / gate | Revisão do código / ambiente | Verificação | Evidência | Resultado | Revisor |
|---|---|---|---|---|---|
| [ID] | [referência] | [cenário / comando] | [caminho / link] | [PASS/FAIL/BLOQUEADO/PENDENTE] | [identidade real] |

## Bloqueios e aprendizado

- Bloqueio / decisão necessária: [causa e impacto]
- Tentativas anteriores e resultados: [evidências úteis]
- Trabalho independente possível dentro do acordo: [itens ou nenhum]
- Refinamentos técnicos autorizados: [referências]
- Retrospectiva da última fase: [referência]

## Retomada

Releia o acordo e a base aprovada. Confira o estado real do Git, processos, dados e evidências. Reconcile a fila interna quando aplicável e revalide os resultados afetados por alterações. Continue da próxima ação respeitando o checkpoint registrado; não repita autorizações ainda válidas.

Na Valeti, releia os cards mapeados via Rovo MCP e seus responsáveis antes de continuar ou sincronizar. Preserve chaves, pai, branch e PR; não recrie cards nem restaure status antigo sobre uma mudança humana.
