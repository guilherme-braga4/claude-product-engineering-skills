---
name: prd-from-discovery
description: "Gera ou evolui PRDs a partir de Discovery, usando o modelo de Produto do usuário: atores, RNs imutáveis, UCs observáveis, RFs MoSCoW, qualidades humanas e mudanças rastreáveis. Use para transformar discovery, entrevistas, AS-IS e decisões em requisitos verificáveis, iniciar uma iniciativa ou definir uma nova frente de produto. Não substitui discovery sem fontes, desenho de arquitetura, plano de código ou auditoria de prontidão."
---

# PRD a partir de Discovery

Transforme o Discovery em um contrato de Produto que permita orientar implementação e avaliar resultados. Descubra o domínio de cada projeto; não presuma stack, setor, maturidade ou regra de negócio. Escreva em português, salvo pedido diferente.

Leia o [template original](assets/PRD-TEMPLATE.md) e o [protocolo de autoria](references/authoring-protocol.md) antes de redigir. O template fornecido pelo usuário define a estrutura; o protocolo resolve rastreabilidade, evolução e separação de responsabilidades.

## 1. Delimite a iniciativa e as fontes

Leia as instruções aplicáveis do repositório. Comece por `docs/`, mas procure Discovery, PRDs anteriores, decisões, fluxogramas e especificações relevantes também fora dela, incluindo arquivos ocultos/ignorados pertinentes. Classifique fontes antes de abrir conteúdo sensível. Preserve alterações locais.

Identifique objetivo, problema, atores, resultado desejado, recorte, exclusões e estado atual. Aceite documentos, entrevistas, notas, transcrições, chats e handoffs de `product-as-is` e `high-level-engineering` quando acessíveis. Essas skills são opcionais; não as instale nem pressuponha acesso à memória de outro chat.

Separe em registro de trabalho: fato observado, decisão explícita, proposta, hipótese, conflito e lacuna. Código comprova comportamento existente; não define sozinho o comportamento desejado. Sugestão de outro agente, item de roadmap e hipótese do Discovery não são requisitos aprovados.

Sem Discovery suficiente, consolide o que é conhecido e faça perguntas específicas com recomendação e consequência. Continue nas partes independentes. Nunca preencha lacunas com metas, atores, regras, números, prioridades ou aprovações inventados.

## 2. Escolha a operação correta

- Novo produto ou iniciativa: derive escopo e comportamento desejado do Discovery e das decisões.
- Nova frente de produto existente: leia a base vigente, explicite o delta e preserve invariantes e exclusões.
- Evolução de PRD: compare versões e decisões, preserve a identidade dos requisitos e registre substituições.
- Migração sem mudança de Produto: preserve comportamento e faça uma única alteração na seção 7, remetendo ao ARCHITECTURE-TO-BE. Mudanças observáveis reais deixam de ser uma migração puramente técnica.

Use o namespace de IDs do projeto. Na ausência de convenção, mantenha IDs estáveis por iniciativa e suas versões, sem impor unicidade global entre produtos independentes.

## 3. Redija pelo modelo

Preserve ordem, títulos e numeração das oito seções e do Checklist de Validação Final. Preencha os campos aplicáveis. Se remover uma seção inaplicável, deixe nota explícita com número e motivo, sem renumerar as seguintes. Não deixe placeholders de preenchimento; questões reais ficam identificadas como pendências em §8.

Regras centrais:

- Cada RN expressa regra de domínio, escopo e teste mínimo binário. Mudança de significado exige novo ID; o antigo é retirado da lista ativa e nunca reciclado. Preserve motivo e ligação da substituição no registro de rastreabilidade, sem apagar o histórico.
- Cada UC descreve ator, pré-condições, fluxo principal, alternativas, exceções, pós-condições, telemetria mínima e teste de integração mínimo. A descrição deve permitir observar o comportamento de fora.
- Cada RF recebe MoSCoW, tag MANTIDO/EVOLUÍDO/NOVO, aceite binário, dependências e notas. A tag depende da base AS-IS; ausência de evidência não significa NOVO. Prioridade proposta continua proposta até decisão. WON'T significa fora do recorte, sem promessa de implementação.
- §6 contém somente qualidades e impacto humano/negócio, sem números, métricas, formatos ou unidades técnicas. IDs e numeração estrutural não são metas. Métricas técnicas pertencem ao ARCHITECTURE-TO-BE §9, ancoradas na qualidade correspondente.
- §7 contém somente mudanças desta iniciativa, com total e classificação coerentes, matriz e detalhes com impactos explícitos em UC/RN/RF/qualidades. Declare não aplicabilidade de um tipo de impacto quando sustentada; não invente requisitos para preencher tabela.
- Para cada mudança, descreva comportamento esperado, testes necessários, observabilidade pertinente, riscos, recuperação, dependências e aceite. RNs requerem cenários unitários; UCs, de integração; qualidades, verificação dos RNFs associados. Isso define obrigações verificáveis sem escrever código de teste ou definir ferramentas.

Critérios devem definir condições, ação e resultado observável, inclusive negativa, exceção e limite relevante. “Funciona”, “é seguro” e “testes passam” não são critérios suficientes. Não adicione cenários, exigências ou percentuais sem fundamento no produto.

## 4. Preserve a fronteira Produto/Engenharia

O PRD não contém libs, funções, classes, caminhos de código, snippets, schemas, protocolos, endpoints ou métricas de implementação. Números de negócio fundamentados podem existir fora de §6; não confunda preço, prazo comercial ou limite de domínio com RNF técnico.

Os campos de implementação, infraestrutura e rollback do template permanecem, mas descrevem responsabilidades e efeitos de alto nível. Não imponha feature flags, dashboards, deploy reverso ou tecnologias apenas porque aparecem como exemplos no template.

Informação técnica relevante vai para a referência canônica de arquitetura existente ou para um handoff técnico separado em `docs/`; não invente que o ARCH §9 já existe ou está aprovado. Não modifique arquitetura fora do escopo solicitado.

Use nomes e links de documentos como referências. A proibição de paths se refere a detalhes de implementação no conteúdo de Produto, não ao destino de links que permitem navegar entre artefatos.

## 5. Valide e entregue

Faça revisão semântica pelo checklist do template e pelo protocolo. Execute a verificação estrutural usando o caminho real da skill:

```text
python3 <pasta-da-skill>/scripts/validate_prd.py <caminho-do-PRD>
python3 <pasta-da-skill>/scripts/validate_prd.py <caminho-do-PRD> --baseline <PRD-anterior>
```

O script identifica parte dos problemas de estrutura, IDs e §6; não prova cobertura semântica, imutabilidade de domínio, aceite correto ou aprovação humana. Avalie cada aviso. Corrija falhas sustentadas por evidência; com lacunas reais, entregue rascunho com decisões pendentes, sem fabricar respostas para zerar o validador.

O PRD nasce como rascunho ou pronto para revisão, nunca autoaprovado. Mantenha as aprovações de §7 pendentes até decisão explícita. O checklist de releitura após uma noite fica desmarcado até confirmação do usuário em data posterior à redação. Não espere um dia para entregar o rascunho; aguarde apenas a aprovação em momento apropriado. Instrução posterior explícita do usuário que altere essa regra deve ser registrada.

Grave o PRD em `docs/` do projeto responsável, na convenção existente. Use um registro auxiliar de rastreabilidade/decisões e um checkpoint, reaproveitando os existentes. Detalhes estão no protocolo.

Na resposta, informe o estado do PRD, o recorte, as decisões que faltam com sua recomendação, as mudanças de regras/IDs, as validações realizadas e links para os artefatos. Não execute implementação, não inicie Agent Team e não publique mudanças por efeito implícito de criar um PRD.

Antes de compactar, consulte [CONTEXT-COMPACTION.md](CONTEXT-COMPACTION.md). Persista decisões, rejeições, proveniência, IDs reservados/retirados e próxima ação no artefato apropriado.
