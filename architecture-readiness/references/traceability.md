# Rastreabilidade e ações de Engenharia

## Identidades e cobertura

Preserve IDs reais do PRD e do Readiness, qualificados pela iniciativa/execução quando necessário. Sem ID estável para um aceite, atribua um alias local ligado à seção e texto de origem, sem reescrever o PRD. Use `D-001` para delta e `ENG-001` para ação, estáveis entre revisões; nunca recicle um ID retirado.

Inventarie o conjunto integral de RNs, UCs, RFs, qualidades e aceites. Mantenha itens fora do recorte (por exemplo WON'T) visíveis e justificados; não lhes atribua implementação obrigatória. Exiba denominadores separados para total inventariado, dentro e fora do escopo. Qualidades usam §6.X do modelo ou seu ID real com correspondência explícita.

## Matriz mestre

`MATRIZ-PRODUTO-ENGENHARIA.md` deve permitir rastrear em ambas as direções:

`PRD/aceite → critério/achado Readiness → AS-IS/evidência → delta → TO-BE/decisão/RNF → ação/lote → validação → prova futura`.

Use uma linha por relação verificável; pode haver várias linhas para o mesmo requisito quando muda o cenário, ação ou validação. Não junte IDs em uma célula se isso esconder qual relação está coberta.

| Item PRD / aceite (link) | Critério / achado Readiness | AS-IS e evidência | Delta | TO-BE / decisão / RNF | Ação ENG | Lote / revisão | Validação e resultado esperado | Estado da prova / link | Q / dependência |
|---|---|---|---|---|---|---|---|---|---|

Estados devem distinguir observado, parcial, ausente e não verificável no AS-IS; mantido, alterar, criar, remover ou fora do recorte no delta; planejada, executada/aprovada, executada/reprovada ou bloqueada na prova. “Sem alteração — mantido” é válido para ação; ainda exige vínculo de arquitetura e validação. “Não avaliado no Readiness” é uma lacuna explícita, não um achado inventado.

Pode dividir tabelas por domínio para legibilidade, mantendo índice único e a mesma semântica. O resumo de cobertura registra números, conjuntos faltantes e links de evidência da reconciliação; um percentual sozinho não basta.

## Reconciliação obrigatória

Antes de declarar cobertura completa:

1. Compare conjuntos de IDs: **PRD inventariado = matriz mestre** (incluindo exclusões explícitas). Liste faltantes, extras indevidos e IDs duplicados inconsistentes; relações múltiplas válidas não são duplicatas acidentais.
2. Para RNs/UCs/RFs no escopo: **PRD = TO-BE §2 = TO-BE §8.1**. Itens fora do escopo permanecem identificados em notas/tabelas de exclusão nas duas seções, sem exigir testes de execução da iniciativa.
3. Para cada qualidade no escopo: **AS-IS §4.5 ↔ TO-BE §9 com ao menos um RNF-T ↔ TO-BE §8.1 ↔ matriz mestre**. Todo RNF-T aponta a qualidade existente e método verificável; metas propostas ficam marcadas.
4. Cada critério obrigatório/achado/lote do Readiness tem destinação explícita. Critério sem âncora no PRD precisa de fonte/decisão reconhecida ou Q; não invente requisito para fechar a tabela. Achado fora do recorte é listado separadamente com razão, sem desaparecer.
5. Cada delta material tem ao menos uma ação; cada ação/decisão/componente tem âncora em Produto, inclusive trabalho transversal e ações compartilhadas. Toda ação identifica o resultado verificável e lote. Dependências referenciam IDs existentes, não formam ciclos e não escondem Q bloqueante.
6. Verifique no sentido inverso: nenhuma ação sem justificativa, nenhum teste sem objetivo identificável e nenhum requisito no escopo sem arquitetura/validação previstas. Aceites mantidos precisam de prova/regressão pertinente; futuras execuções não recebem ✅ antecipadamente.
7. Registre o resultado de cada conferência: passou, falhou ou não verificável, com contagens e IDs pendentes. Cobertura documental pode estar completa com testes planejados; prontidão operacional só é comprovada por evidências atuais no Readiness.

Complete o trabalho acessível que estiver faltando. Persistindo lacuna indispensável ou Q, entregue parcial/bloqueado com a lista, nunca “100% garantido”. A matriz garante rastreabilidade verificável; não prova sozinha que o sistema satisfaz o PRD.

## Delta e pacotes para aprovação

O relatório começa pelo efeito no Produto e compara **base avaliada → destino proposto**. Inclua alterações em componentes, fluxos, contratos, dados, dependências, operação, testes e documentação quando necessárias, além das capacidades preservadas e exclusões. Histórico entre snapshots é seção separada.

Cada `ENG-...` informa: problema, vínculo PRD/aceite/achado/delta, resultado, arquivos ou fronteira de implementação, proposta concreta, dependências, risco, validação e lote responsável. Investigações e validações são ações legítimas quando falta evidência; marque quando seu resultado condiciona a solução. Evite estimativas numéricas sem base.

Para lote existente, use a chave `readiness-id/L-xx/rN` e seu escopo/revisão. A matriz e o relatório são visões desse mesmo trabalho, não outra aprovação independente. Se o desenho amplia seu escopo, mostre a revisão proposta e o delta; não reutilize autorização da revisão anterior para a ampliação.

Para ações sem lote existente, crie `snapshot-id/ARCH-L-xx/rN` no relatório. Cada pacote deve conter:

- resultado e impacto no Produto, requisitos/aceites e ações ENG incluídas;
- proposta e alcance concreto (repositórios/componentes/arquivos conhecidos);
- dependências e ordem de execução, Qs e recursos necessários;
- efeitos a autorizar, riscos e recuperação pertinente;
- critérios de aceite observáveis, método e ambiente de validação;
- base/revisão, estado proposto/aprovado/etc. e proveniência de decisão quando houver.

Uma ação pertence a um pacote principal; outras relações são dependências. Não duplique código, testes ou deploy em lotes paralelos. Apresente juntos pacotes existentes e novos como conjunto finito para decisão, preservando execução e revisão de origem. Aprovações já válidas continuam válidas para o mesmo escopo; pacotes novos/ampliados não são aprovados automaticamente.
