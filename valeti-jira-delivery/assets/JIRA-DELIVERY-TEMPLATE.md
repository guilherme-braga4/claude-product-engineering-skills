# Rastreabilidade Jira — [iniciativa]

> Incorporar ao acordo/estado existente. IDs abaixo são placeholders, nunca chaves válidas para implementar. Em planejamento somente leitura, registrar intenção e campos pendentes, sem alegar cards criados.

## Contexto confirmado

- ROADMAP / revisão / trecho autorizado: [referência]
- PRD / aceite / autorização de execução: [referências]
- Rovo MCP / site / cloudId / projeto / Board: [identificadores sem credenciais]
- Usuário confirmado / accountId: [identidade verificada na conexão da Valeti]
- Agente responsável pela sincronização: [executor ou participante real identificado]
- Prefixo de branch / base por repositório: [convenção verificada]
- Configuração de colunas/status: [consulta e momento; revalidar antes das transições]

## ROADMAP → Tasks pais → branches

| ID estável / nome do item do ROADMAP | Task pai / URL | Assignee confirmado | TASKPLAN / revisão | Repositório / branch do pai / PR | Gates restantes |
|---|---|---|---|---|---|
| [ID / título = summary da Task] | [chave retornada / URL] | [accountId / horário] | [referência] | [repo / prefixo/CHAVE-PAI / URL quando existir] | [pendências] |

## TASKPLAN → Subtasks

| ID estável / título do item | Task pai | Subtask / URL | Assignee confirmado | Aceite / evidência / commit | Estado técnico |
|---|---|---|---|---|---|
| [ID / título = summary da Subtask] | [chave validada] | [chave retornada / URL] | [accountId / horário] | [critério / referência / SHA] | [planejado / em execução / validado / bloqueado] |

## Sincronização por card

| Data / agente | Card / assignee relido | Status e coluna anterior | Destino justificado / evidência | Transição usada | Status e coluna confirmados | Resultado / pendência |
|---|---|---|---|---|---|---|
| [data / identidade real] | [chave / accountId] | [observado] | [estado / gate] | [ID retornado pelo Jira ou nenhuma] | [observado após escrita] | [confirmado / já consistente / ignorado: outro responsável / bloqueado] |

## Retomada

- Escrita com resposta incerta: [operação / referência estável a pesquisar antes de repetir]
- Cards não elegíveis e bloqueios: [chaves / motivo / próxima ação]
- Branch/worktree/diff preservado: [local e condição]
- Próxima ação: [ação técnica ou sincronização pendente]
