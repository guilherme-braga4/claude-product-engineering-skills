# Acordo de execução

Leia antes de iniciar ou ao detectar uma mudança material no alcance autorizado. Aproveite instruções e respostas existentes. Pergunte escolhas ainda necessárias em um grupo conciso; não peça confirmação ritual do que já foi autorizado.

## Escolhas iniciais

| Decisão | Alternativas a apresentar quando indefinida |
|---|---|
| Alcance | Roadmap completo; até determinada fase inclusive; apenas uma fase |
| Checkpoints | Continuidade automática; liberação humana entre fases; checkpoints especificados |
| Revisão | Agente revisor identificado; revisão humana; combinação por gate |
| Git | Branch base/de integração, commits, push, merge e limites aplicáveis |
| Publicação | Ações e ambientes de destino, somente se parte da execução |
| Validação real | Ambiente, contas de teste e limites para UI, API e banco |

Explicite ao usuário quais gates originalmente humanos serão delegados. Use o agente existente escolhido pelo usuário quando disponível. Não exija criar um novo agente se o ambiente já oferece revisão independente adequada.

## Registro mínimo no projeto

- PRD e Roadmap: caminhos canônicos, revisão aprovada e evidência da aprovação.
- Outros documentos que governam a execução e suas revisões.
- Alcance e regra de avanço entre fases.
- Revisor, gates delegados e gates reservados ao humano.
- Estratégia e destinos de Git; ações de publicação autorizadas, se houver.
- Ambiente de validação, URLs e identificadores não secretos de contas/conexões.
- Operações de dados permitidas: leitura, criação por UI/API, fixtures, migrações ou escrita direta quando necessárias.
- Efeitos externos permitidos e substitutos de teste para pagamentos, mensagens ou integrações aplicáveis.
- Limites de execução definidos pelo usuário ou pelo runtime e comportamento ao atingi-los.
- Evidência da autorização: resposta do usuário ou referência à sessão; data e condições de validade.

Não registre tokens, senhas, cookies ou strings de conexão com credenciais. Referencie o mecanismo existente de acesso.

## Autorização de testes

Verificar o ambiente e os acessos faz parte da prontidão. Use o ambiente de desenvolvimento/teste já autorizado. Operações rotineiras de teste nele não exigem nova autorização por comando.

Não presuma que acesso de leitura ao DB autoriza escrita. Uma ação pela interface ou API também pode alterar dados e disparar efeitos externos; considere o efeito, não a ferramenta. Para permitir iteração contínua, combine antecipadamente fixtures, contas e operações necessárias. Se houver acesso a ambiente compartilhado/produção, o acordo precisa delimitar o que será executado ali.

## Mudanças durante a execução

O executor pode refinar tarefas e corrigir código preservando os compromissos aprovados. Descobertas que mudem produto, aceite ou decisões reservadas ao usuário devem virar propostas rastreáveis, sem alterar silenciosamente a base aprovada.

Só renegocie a parte afetada do acordo. Uma interrupção técnica ou compactação não cancela as demais autorizações. A permissão das ferramentas permanece um controle separado: não prometa execução sem prompts apenas por existir autorização textual.
