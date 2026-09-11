# Protocolo de snapshots e cache

## Layout

Use `docs/product-as-is/` na raiz, salvo convenção ou caminho explícito do usuário. Os artefatos de cache são Markdown. Não modifique `.gitignore` automaticamente.

```text
docs/product-as-is/
  INDEX.md
  snapshots/<YYYY-MM-DDTHHMMSS>-<id>/
    CHECKPOINT.md
    INVENTORY.md
    COVERAGE.md
    AS-IS.md
    HANDOFF.md
    EVOLUTION.md
    EVIDENCE.md
    units/<unit-id>.md
```

Use identificador adicional para evitar colisões. `INDEX.md` aponta separadamente para última auditoria finalizada com cobertura integral do escopo, última parcial e execução em andamento. Snapshots finalizados são imutáveis; apenas índice e execução em andamento são atualizados. Retenha snapshots referenciados por outros; não faça limpeza automática.

Em repositórios grandes, divida inventário/evidências por unidade em subarquivos `.md` ligados aos índices. Gere tabelas de metadados por ferramenta local e leia apenas os lotes necessários, sem carregar listas gigantes no contexto.

## Manifesto verificável

`INVENTORY.md` registra versão do protocolo (1), raiz/identidade, hora, método de descoberta, commit, estado de trabalho, exclusões, submódulos e arquivos externos inacessíveis.

Para cada arquivo próprio relevante, registre caminho, categoria, unidade e SHA-256 do conteúdo observado. Considere rastreados alterados e arquivos novos, inclusive relevantes ignorados. Commit e mtime sozinhos não identificam conteúdo local. Detecte remoções comparando inventários. Renomes só preservam identidade com evidência da correspondência.

Para dependências/gerados excluídos, registre grupos, contagem e manifests/origens que os governam. Arquivos sensíveis recebem classificação e motivo, sem conteúdo nem hash de segredos. Mudanças não verificáveis neles invalidam conclusões dependentes de configuração, ou as mantêm explicitamente não verificadas.

Exclua a pasta de saída da auditoria do fingerprint do Produto para evitar invalidação circular; registre essa exclusão e motivo.

## Snapshot de unidade

Cada `units/<unit-id>.md` contém:

1. Identidade, produto/domínio, estado, data, origem do cache e versão do protocolo.
2. Arquivos cobertos e fingerprint: hash calculado sobre lista ordenada de caminhos e hashes, incluindo contratos/configurações relevantes.
3. Dependências e consumidores conhecidos, flags, schemas, manifests e fontes externas; dependências incertas explícitas.
4. Capacidades, jornadas e regras com IDs, três dimensões de estado e referências de evidência.
5. Dados, interfaces, efeitos externos, erros e limitações.
6. Verificações estáticas e executadas, distinguindo resultados históricos.
7. Lacunas, contradições, impacto sobre outras unidades e pendências.

Resumo reutilizado precisa de proveniência e evidências. O snapshot não é fonte primária. Pode referenciar detalhe anterior imutável, declarando revalidação atual e mantendo links resolvíveis; aponte ao detalhe original para evitar cadeias longas.

## Primeira execução

Sem cache compatível, inventarie tudo e analise cada unidade relevante. Relatórios antigos sem manifesto/evidências orientam buscas, mas não dispensam inspeção. Não importe contagens ou conclusões como fatos novos.

Trabalhe em lotes até esgotar a fila. Após cada lote, persista unidade e checkpoint. Leia resumos de dependências e trechos necessários em vez de todo o monorepo de uma vez. A economia vem de leitura seletiva e persistência, não de omitir unidades.

## Execuções seguintes

1. Refaça o inventário completo e identifique adições, alterações, remoções, renomes e fontes inacessíveis. Reconheça mudanças no workspace mesmo se HEAD não mudou.
2. Valide identidade, protocolo, evidências e fingerprint de cada unidade. Cache incompleto, incompatível ou não verificável exige reanálise da parte afetada.
3. Invalide unidades alteradas e consumidores transitivos de contratos, regras, schemas, permissões, flags, dependências, build/configuração e interfaces que mudaram. Reavalie dependências descobertas; não dependa apenas do grafo antigo.
4. Se não puder limitar impacto de mudança compartilhada ou dependência dinâmica, amplie reanálise para todo o escopo potencialmente afetado. Explique a abrangência escolhida.
5. Nas unidades sem alteração, confira arquivos, referências e condições de validade antes de reutilizar conclusões estáticas. Toda unidade recebe decisão atual, mesmo sem alterações.
6. Evidências de banco, deploy, flags remotas, serviços e documentos externos precisam de nova observação para afirmações atuais. Se inacessíveis, preserve observação anterior com data e atualidade desconhecida. Hash de código não renova evidência operacional.
7. Testes antigos continuam históricos. Para reafirmar resultado atual, execute testes pertinentes; registre mudanças de ambiente/dependências.
8. Reconcilie inventário no fim. Se código/dependências mudaram durante auditoria, reanalise afetados até obter recorte coerente. Com edição contínua, registre intervalos/hashes por unidade e finalize como parcial por falta de snapshot consistente.

Arquivo removido invalida evidências atuais; investigue sua capacidade para distinguir remoção, substituição ou deslocamento. Documento novo pode mudar entendimento e confiança sem mudança no software.

## Cobertura e retomada

`COVERAGE.md` lista cada unidade com estado: pendente, em análise, analisada nesta execução, cache revalidado ou bloqueada. Inclua quantidade de arquivos relevantes, caminho do detalhe e motivo de bloqueio/exclusão. Toda unidade aparece, inclusive sem interface pública ou testes.

Mostre contagens por categoria e unidades analisadas/revalidadas/bloqueadas. Excluídos têm denominador separado. Inventário completo e análise completa são medidas diferentes; cobertura de arquivos não é cobertura funcional total.

`CHECKPOINT.md` contém execução/base, estado, filas pendentes/invalidadas, lotes concluídos, fontes bloqueadas, decisões e próxima ação. Atualize antes de compactação/interrupção. Na retomada, revalide inventário contra checkpoint. Não suponha que processos ou subagentes anteriores continuam ativos.

Estados finais:

- **Completa no escopo declarado:** inventário reconciliado e todas as unidades relevantes analisadas ou com cache revalidado. Não implica produção validada nem ausência de defeitos.
- **Parcial:** unidades relevantes bloqueadas/pendentes ou inconsistência temporal não resolvida. Liste quais; não esconda bloqueios em exclusões.

Atualize `INDEX.md` depois de salvar relatórios e conferir links. Auditoria parcial pode ser reutilizada por unidade, mas não substitui silenciosamente a última base completa.

## Verificação dos artefatos

Confira caminhos sem classificação, IDs duplicados, referências quebradas e afirmações sem proveniência. Confira hashes reutilizados e invalidação de consumidores. Não afirme SHA-256 ou testes executados se apenas descreveu o procedimento.

O handoff deve conter fatos essenciais sem exigir acesso ao cache. AS-IS e detalhes devem permitir rastrear conclusões às fontes. Preserve segredos e dados pessoais fora de todos os arquivos.
