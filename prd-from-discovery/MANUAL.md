# Manual — PRD a partir de Discovery

## Quando usar

Use para transformar Discovery, entrevistas, decisões e o contexto AS-IS em um PRD verificável, no modelo fornecido. Serve para novo produto, iniciativa, frente de evolução ou migração de produto existente.

## Invocação

Abra o Claude Code no projeto e envie:

```text
/prd-from-discovery
Crie o PRD da iniciativa [nome] a partir deste Discovery: [arquivo ou contexto].
```

Para delimitar melhor:

```text
/prd-from-discovery
Objetivo e resultado esperado:
Fontes de Discovery e decisões:
PRD vigente ou iniciativa relacionada, se existir:
Recorte e exclusões:
Público/atores e restrições conhecidos:
```

Não é necessário repetir dados já documentados. A skill procura as fontes em docs e no restante relevante do projeto. Chats e handoffs podem ser fornecidos como contexto; acesso à janela interna de outra sessão não é presumido.

## O que ela entrega

- PRD nas oito seções do seu [template](assets/PRD-TEMPLATE.md), mais checklist.
- Rastreabilidade de Discovery, decisões, regras, jornadas, capacidades, mudanças e aceite.
- Lacunas e perguntas objetivas com recomendação, sem fabricar requisitos para preencher campos.
- Registro de substituição de RNs, preservando IDs antigos sem reciclagem.
- Checkpoint com progresso, validações e próxima ação.

Os artefatos ficam em docs do projeto responsável. O PRD trata comportamento de Produto; detalhes técnicos e RNFs permanecem nos artefatos de Engenharia.

## Exemplos de continuidade

```text
Evolua o PRD desta frente com as decisões da nova rodada de Discovery.
Preserve invariantes e identifique qualquer RN que precise ser substituída.
```

```text
Esta iniciativa é uma migração sem mudança de Produto.
Preserve o comportamento e mantenha a seção 7 enxuta, apontando para o ARCH.
```

## Validação e aprovação

O script scripts/validate_prd.py verifica parte da estrutura, referências de IDs, campos mínimos e conteúdo de qualidades. A revisão semântica continua necessária. O resultado do script não aprova o PRD nem confirma que todos os requisitos têm evidência.

Use `--baseline` para comparar o texto das RNs com a versão anterior e `--migration-only` para exigir uma única alteração na seção 7. Mudança de texto gera aviso para revisão semântica; o script não decide sozinho se a regra mudou de significado nem detecta reciclagem de um ID ausente da base fornecida.

Para executar os testes do validador, na raiz deste repositório:

```bash
python3 -m unittest discover -s prd-from-discovery/tests -v
```

O PRD é entregue como rascunho ou pronto para revisão. A regra de releitura após uma noite, presente no template, fica pendente até sua confirmação em data posterior. Isso não impede a redação e entrega do documento no mesmo dia.

## Relação com as demais skills

product-as-is fornece a base existente; prd-from-discovery define o que deve ser entregue; high-level-engineering define a solução técnica; product-engineering-readiness confronta a entrega com o aceite. Podem existir ciclos entre Discovery e Engenharia sem transformar sugestões técnicas em decisões de Produto.

## Compactação

Use [CONTEXT-COMPACTION.md](CONTEXT-COMPACTION.md). Preserve especialmente origem dos requisitos, decisões rejeitadas, IDs retirados/reservados, pendências e versão em revisão. Esses registros devem permitir continuar sem reabrir decisões assentadas.
