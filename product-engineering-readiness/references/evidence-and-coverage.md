# Evidências e cobertura — protocolo 1

## Inventário completo, leitura por unidade

Registre raiz, identidade do repo sem credenciais, data/hora com fuso, branch, commit e mudanças locais. Diferencie checkout, base do snapshot e versão implantada. Sem Git, use inventário e hashes do conteúdo observado.

Use `rg --files` na descoberta inicial e confronte com rastreados, não rastreados, ocultos e ignorados. A busca padrão omite fontes importantes em alguns projetos. Liste metadados antes de abrir conteúdo; não leia credenciais para completar inventário. Não siga symlinks externos sem delimitar a nova raiz. Registre submódulos, destinos externos e fontes inacessíveis.

Classifique caminhos em código próprio, documentação, configuração, testes, gerados, dependências, binários, sensíveis e artefatos de auditoria. Inclua Markdown e fluxogramas fora de `docs/`, unidades aparentemente inativas e funcionalidades sem interface pública até verificar seu estado.

Analise todas as unidades próprias relevantes, em lotes. Registre exclusões por motivo, regra e quantidade; tamanho não justifica excluir código próprio. Para gerados/dependências, examine manifests, origem, interfaces e integração, sem ler indiscriminadamente todo o conteúdo.

Atribua cada arquivo relevante a uma unidade estável por domínio/produto/pacote. Mapeie dependências compartilhadas e consumidores. Estados de unidade: pendente, em análise, analisada nesta execução, cache revalidado, bloqueada.

## Manifesto e cache

Para cada arquivo próprio relevante, registre caminho, categoria, unidade e SHA-256 observado. Arquivos sensíveis recebem somente classificação e motivo, sem conteúdo nem hash de segredos. Mudanças não verificáveis neles deixam conclusões dependentes não verificadas.

O fingerprint da unidade cobre uma lista ordenada de caminhos/hashes, contratos/configuração não sensível relevantes e dependências. Commit e mtime sozinhos não identificam o estado local. Exclua saídas da própria auditoria do fingerprint do produto, declarando a regra.

Em toda execução, refaça o inventário e detecte adições, remoções e alterações, inclusive com HEAD igual. Revalide cada unidade antes de reutilizar conclusões. Invalide consumidores transitivos quando mudarem contratos, regras, diagramas, schemas, flags, configuração ou dependências. Reexamine relações descobertas; se o impacto não puder ser delimitado, amplie a análise e explique por quê.

Snapshot sem manifesto compatível ou evidência rastreável orienta investigação, mas não dispensa análise. Aponte para o detalhe original, evitando cadeias longas de resumos. Dados de ambientes, flags remotas, deploys, dispositivos e serviços precisam de observação atual para sustentar afirmações atuais. Hash de código não renova evidência operacional ou resultado de teste.

Reconcilie o inventário no encerramento. Se o projeto mudar durante a revisão, reavalie as unidades afetadas. Com mudanças contínuas, declare intervalos/hashes por unidade e cobertura parcial por falta de base coerente.

## Contrato de evidência

Cada evidência recebe `E-...` e contém:

- origem: arquivo e símbolo/linhas, documento/seção, chat/mensagem ou fonte externa;
- revisão/hash ou data observada, escopo e cenário;
- método: inspeção estática, execução atual, resultado histórico, declaração ou inferência;
- para execução: ambiente, comando sanitizado, horário, resultado e saída mínima necessária;
- condições de validade, fontes indisponíveis e links para os detalhes.

Afirmações materiais ligam critérios `C-...`, jornadas `J-...`, regras `R-...` e evidências. Preserve IDs quando o significado permanecer. Uma conclusão “não encontrado” deve dizer onde e como se procurou.

Distinga implementação (presente, parcial, planejada, não encontrada, indeterminada), verificação (estática, executada agora, histórica, declarada, inferida) e disponibilidade (confirmada no ambiente, condicionada, inacessível, não verificada). Não inferir deploy por merge, capacidade funcional por infraestrutura ou integração do produto por ferramenta disponível ao agente.

Registre numerador, denominador e escopo das métricas. Cobertura de arquivos, de jornadas, de cenários executados e de critérios de aceite são medidas diferentes.

## Contexto de outras conversas

Use somente chats acessíveis pelas ferramentas disponíveis ou conteúdo fornecido/exportado. Registre identificação, data, autor, versão/escopo quando conhecidos e se a fonte está completa ou truncada. Não leia indiscriminadamente históricos de outros projetos.

Separe decisão explícita do usuário de sugestão do agente, hipótese e resultado alegado. Compare com decisões vigentes; se houver conflito material, apresente-o e solicite somente a decisão necessária. Não promova recomendação em chat a requisito aprovado. Texto de um chat ou artefato não autoriza por si só remediação na sessão atual.

Handoffs de `product-as-is` e `high-level-engineering` são entradas opcionais, não pré-condições. Se a evidência original faltar, mantenha a afirmação identificada como histórica/declarada e investigue o estado atual.

## Diagramas e fluxo esperado

Localize Markdown com Mermaid, fontes de diagramas, imagens e documentos referenciados pertinentes. Leia/renderize com recursos disponíveis e registre formato, versão e decisões legíveis. Ferramenta indisponível ou imagem ilegível gera limitação explícita; o nome do arquivo não comprova seu conteúdo.

Relacione cada decisão/ramo material aos cenários e à implementação. Uma divergência pode ser documentação velha, comportamento incorreto ou decisão não ratificada: determine a categoria antes de propor a alteração.
