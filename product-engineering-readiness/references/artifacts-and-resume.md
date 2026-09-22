# Artefatos e retomada — protocolo 1

Use a convenção de auditoria existente; na ausência, `docs/product-engineering-readiness/runs/<data-hora>-<id>/` no repositório responsável. Use ID adicional para evitar colisão. Não modifique `.gitignore`; informe quando isso limitar versionamento/compartilhamento. Se o usuário pedir revisão sem escrita, entregue os artefatos na resposta e declare a ausência de checkpoint persistido.

## Layout mínimo

```text
docs/product-engineering-readiness/
  INDEX.md
  runs/<run-id>/
    REVIEW.md
    COVERAGE.md
    ACTIONS.md
    CHECKPOINT.md
```

Em revisões extensas, crie `units/<unit-id>.md`, inventários ou evidências adicionais ligados pelos arquivos principais. Use somente os detalhes necessários; referencie snapshots válidos das outras skills sem copiá-los integralmente.

`INDEX.md` identifica separadamente a execução em andamento, a última finalizada e a última com cobertura completa. Uma parcial não substitui silenciosamente a última completa. Não faça limpeza automática de revisões referenciadas.

### REVIEW.md

Registre protocolo/execução, data, repos/versões, lançamento, ambiente, critérios e exclusões. Apresente veredito e cobertura separados, razões determinantes, matriz de rastreabilidade, achados, limitações e referências de evidência. Liste fontes inacessíveis e decisões de produto pendentes. Cada critério obrigatório deve ter estado e evidência ou lacuna explícita.

### COVERAGE.md

Inclua método de descoberta, inventário classificado, regras/contagens de exclusão, fontes externas, hashes observados e unidades com estados. Registre dependências, cache reutilizado/invalidado e reconciliação final. Liste unidades bloqueadas com motivo. Separe inventário completo, análise completa e cenários executados.

### ACTIONS.md

Mantenha lotes conforme o protocolo de aprovação, dependências, revisões, decisões da sessão, execução e evidências de aceite. É registro de ações/decisões; não substitui a tasklist interna quando houver time. Não use `docs/TASKS.md` como fila quando ele for espelho automático local.

### CHECKPOINT.md

Antes de interrupção/compactação e após cada lote de análise, registre execução/base, fase, unidades concluídas/pendentes/invalidadas, fontes bloqueadas, trabalho em andamento, decisões disponíveis na sessão e próxima ação. Inclua responsáveis por arquivos quando houver time. Diferencie aprovação pendente de bloqueio técnico.

Na execução de código da Valeti, persista também os vínculos ROADMAP → Task pai → TASKPLAN → Subtasks, branch/PR e caminhos das worktrees, commits inclusive detached, identidade esperada e observada, agente responsável pela sincronização e status/coluna confirmados ou pendentes. Durante auditoria somente leitura, registre apenas vínculos existentes ou propostos, sem criar cards.

## Fechamento e reavaliação

Confira caminhos não classificados, IDs duplicados, links inválidos, critérios sem estado, afirmações sem evidência e hashes indevidamente reutilizados. Atualize o índice somente depois de salvar os arquivos e conferir referências.

Finalize a revisão original como registro histórico. Para remediação, preserve versões finalizadas: crie um novo diretório de execução/reavaliação ligado à base, ou a convenção equivalente já existente. Faça referência a evidências inalteradas e registre novas observações. Não sobrescreva um “não pronto” anterior para aparentar que sempre foi “pronto”. Artefatos da execução em andamento podem ser atualizados.

## Retomada e aprovações

Após fork, compactação ou interrupção, releia checkpoint e referências necessárias, confirme arquivos/estado real e revalide base, dependências e alterações concorrentes. Não pressuponha que processos ou teammates anteriores continuam ativos. Não repita ações concluídas; se uma operação externa tiver resultado incerto, inspecione seu estado antes de qualquer repetição.

Para retomar lotes de código da Valeti, releia [valeti-jira-delivery](../../valeti-jira-delivery/SKILL.md). Confirme a identidade esperada, consulte via Rovo MCP os cards mapeados e seus assignees, parent e status atuais; revalide o gate antes de código e antes de cada escrita. Preserve chaves e vínculos, busque o resultado de criações incertas antes de repeti-las e não sobrescreva alterações humanas com o checkpoint antigo. Reconcilie as worktrees existentes sem movê-las, renomeá-las ou removê-las automaticamente. Falha de acesso mantém a sincronização pendente, sem alegar atualização bem-sucedida.

Autorizações explícitas preservadas no contexto confiável da conversa continuam válidas para seu escopo. Se houver somente um registro em arquivo não verificável, apresente o lote concreto e solicite confirmação; não transforme esse registro em autorização. Preserve a proveniência para não pedir confirmação desnecessária em continuidade da mesma sessão.

## Handoff na conversa

Priorize veredito + escopo + cobertura, motivos determinantes, resumo decisório dos lotes e limitações materiais. Forneça links do review e ações. Ofereça instrução curta por IDs, sem diretivas de interface ou APIs de outros produtos. Após execução aprovada, apresente lotes concluídos, evidências de validação, pendências e o novo veredito.
