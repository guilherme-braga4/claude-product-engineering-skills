# Claude Product Engineering Skills

Skills pessoais e reutilizáveis para compreender um produto, orientar sua arquitetura e avaliar prontidão para lançamento no Claude Code.

## Skills

| Skill | Use quando | Resultado principal |
|---|---|---|
| [`high-level-engineering`](high-level-engineering/MANUAL.md) | A necessidade de Produto precisa virar arquitetura, contratos e direção de implementação. | Contexto técnico atual, decisão arquitetural, impactos e validação. |
| [`product-as-is`](product-as-is/MANUAL.md) | É necessário mapear o Produto que existe hoje antes de iniciar uma frente. | Inventário completo, jornadas, regras, evidências, cobertura e handoff. |
| [`product-engineering-readiness`](product-engineering-readiness/MANUAL.md) | Uma release, piloto ou expansão precisa de decisão de prontidão. | Veredito rastreável e lotes de ações prontos para aprovação. |

## Instalação no Claude Code

As pastas deste repositório são a fonte versionada. Para disponibilizá-las em todos os projetos da máquina, crie links na pasta pessoal do Claude Code:

```bash
mkdir -p ~/.claude/skills
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/high-level-engineering ~/.claude/skills/high-level-engineering
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/product-as-is ~/.claude/skills/product-as-is
ln -s /Users/guilhermebraga/Documents/repos/claude-product-engineering-skills/product-engineering-readiness ~/.claude/skills/product-engineering-readiness
```

Antes de criar um link, confira se o destino já existe. Preserve ou remova conscientemente uma instalação anterior; `ln` não deve ser usado para sobrescrever uma pasta sem revisar seu conteúdo.

O comando de cada skill vem do nome de sua pasta:

```text
/high-level-engineering
/product-as-is
/product-engineering-readiness
```

O Claude também pode carregar uma skill automaticamente quando a solicitação corresponder à descrição do `SKILL.md`. A invocação explícita torna a intenção inequívoca.

## Fluxo recomendado

As skills podem ser usadas isoladamente. Para uma iniciativa completa, a sequência típica é:

1. `/product-as-is` para estabelecer o Produto existente com evidências.
2. `/high-level-engineering` para desenhar ou revisar a direção técnica da mudança.
3. `/product-engineering-readiness` para confrontar o lançamento pretendido com Produto, Software e evidências atuais.

O resultado de uma skill é entrada opcional para a próxima. Cada skill revalida contexto e não trata a conclusão de outro agente como prova atual automática.

## Compactação de contexto

Cada pasta contém `CONTEXT-COMPACTION.md` com dois prompts:

1. persistir e reconciliar o estado importante antes da compactação;
2. executar `/compact` preservando apenas o contexto operacional que não pode ser recuperado das fontes canônicas.

Use os dois passos nesta ordem. Aguarde a confirmação de que a sessão está segura para compactar antes de enviar o segundo prompt.

## Manutenção

- Edite a cópia versionada neste repositório.
- Mantenha decisões duráveis nos documentos canônicos do projeto analisado.
- Não inclua segredos, dados pessoais, snapshots de produto ou relatórios de projetos específicos neste repositório de skills.
- Valide o frontmatter e os links depois de alterar uma skill.

