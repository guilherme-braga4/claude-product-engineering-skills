# Agente único e Agent Team

O contrato de cobertura, evidências, aprovação e saída é idêntico nos dois modos. Use agente único quando suficiente. Considere time quando houver unidades independentes e volume que justifique a coordenação; verifique os recursos realmente disponíveis na sessão do Claude Code. Não habilite funcionalidades experimentais nem altere configuração global automaticamente.

Se o time não estiver disponível e não tiver sido exigido pelo usuário, prossiga individualmente por lotes e informe a adaptação. Se o usuário exigir time, explique a indisponibilidade e peça direção. Não simule participantes nem invente ferramentas. Subagentes de tarefas delimitadas não são um Agent Team com fila compartilhada.

No Claude Code, confirme a disponibilidade de Agent Teams na sessão interativa e a configuração existente. Execuções não interativas (`claude -p`) não validam o modo Agent Team; testes nelas cobrem apenas execução individual/subagentes. Referência de compatibilidade: https://code.claude.com/docs/en/agent-teams (consultada em 2026-09-11); revalide se o comportamento da versão instalada divergir.

## Condição de PRD

Antes de decompor a missão em tarefas ou iniciar participantes, confirme um PRD com objetivo, escopo e critérios de aceite da revisão. Leia-o. Se não existir, pare e peça ao usuário que o forneça/crie. Não use o PRD genérico desta skill como substituto da missão de cada produto. Um PRD de produto sozinho só satisfaz essa condição se também delimitar o objetivo e o aceite da revisão solicitada.

## Divisão de responsabilidades

- Lead: missão, base, critérios, unidades, dependências, ownership de arquivos, consolidação de achados, evidências e veredito; contato para aprovações.
- Product Engineers: unidades por jornada/domínio. Cada participante cruza produto e engenharia; rastreia entradas até efeitos e valida cenários. Evite separar “quem só lê PRD” e “quem só lê código” sem cruzamento das evidências.
- Atribua validação das fronteiras compartilhadas explicitamente; nenhuma integração pode ficar sem responsável porque está entre unidades.

Use a tasklist interna disponível no time para claim, dependências e estado. Dê um dono a cada arquivo; só o Lead consolida arquivos centrais. `ACTIONS.md` registra decisões/resultados. `docs/TASKS.md`, quando espelho automático, é acompanhamento humano e não mecanismo de execução.

## Briefing obrigatório

Cada participante recebe caminhos do PRD, desta skill e dos protocolos pertinentes, além de:

```text
Missão e versão/ambiente:
Unidade/jornadas e critérios atribuídos:
Repos e fontes acessíveis:
Dependências e consumidores a verificar:
Diretório/arquivos de saída sob sua responsabilidade:
Limites: fase de revisão ou IDs/revisões dos lotes já aprovados:
Entrega: cobertura, rastreabilidade, achados, evidências e limitações:
```

Todos leem o PRD e instruções aplicáveis; não dependa do histórico do Lead. Durante review, participantes não corrigem código/specs. Durante remediação, o Lead transmite exatamente o escopo aprovado e critérios de aceite; aprovação de um lote não é autorização para outros.

O Lead reconcilia versões, fontes conflitantes, duplicações, fronteiras e cobertura antes do veredito. Não encerre apenas por receber resumos: confira evidências dos critérios e bloqueadores. Na retomada, reconstrua o estado a partir de arquivos e participantes ativos, não da suposição de que o time anterior foi restaurado.
