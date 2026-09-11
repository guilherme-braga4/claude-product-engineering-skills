# Autoria, rastreabilidade e evolução

## Do Discovery ao requisito

Inventarie as fontes relevantes, sua origem, data, versão e estado. Reconcile o que está vigente; data mais recente não resolve sozinha conflito de autoridade, escopo ou decisão. Registre fontes inacessíveis, entrevistas parciais e limitações da observação.

Para cada conclusão material, encontre a cadeia:

`fonte de Discovery -> fato/decisão -> RN/UC/RF/qualidade -> alteração -> aceite -> referência de arquitetura/plano/implementação, quando existente`

Registre a cadeia em tabela auxiliar; campos ainda inexistentes ficam explicitamente pendentes, sem criar plano de implementação por inferência. Um requisito pode nascer como proposta, mas sua origem e estado precisam estar claros. Descoberta de comportamento legado não o torna automaticamente regra desejada.

Priorize perguntas que mudem escopo, comportamento, limites, propriedade da decisão ou aceite. Apresente opções reais, recomendação e consequências. Não imponha MoSCoW, tag de migração ou aceite definitivo quando dependem de uma decisão ainda ausente. Use texto como “prioridade proposta: MUST; decisão Q01 pendente” e não considere o PRD pronto para aprovação.

Sem fontes suficientes, produza consolidação parcial e perguntas. Sem critério de sucesso, não substitua evidência por uma meta numérica inventada.

## Identidade e substituição

Antes de atribuir IDs, confira PRD vigente, versões históricas relevantes e registro de IDs existente. Sem acesso à base, não garanta que um número está livre. Siga convenções locais, inclusive namespaces por iniciativa. Use RN01, UC01 e RF01 na ausência de outra convenção; qualidades usam §6.1, §6.2 etc.

RNs não mudam de significado sob o mesmo ID. Para uma substituição autorizada:

1. Preserve evidência do conteúdo e estado anteriores.
2. Retire o ID antigo do conjunto ativo e mantenha-o reservado permanentemente.
3. Crie novo ID ainda não usado; registre origem, motivo, decisão e ID substituído.
4. Atualize impactos e referências para distinguir RN ativa da retirada.
5. Mantenha o vínculo histórico na rastreabilidade, sem apresentar ambas como vigentes.

O “ID antigo fica vago” do template significa ausência de regra ativa, nunca disponibilidade para reciclagem. Mudança meramente editorial sem efeito semântico pode preservar identidade, mas exige comparação explícita para não esconder alteração de comportamento.

UCs, RFs e qualidades mantêm identidade quando o significado continua; remoções preservam histórico e números retirados. Não renumere para fechar lacunas ou por estética. Uma qualidade alterada exige decisão consciente; mera mudança da sustentação técnica pertence ao ARCH §9.

## Uso fiel do template

Use o arquivo original em assets como modelo, removendo instruções de preenchimento e exemplos ao gerar o documento. Preserve os nomes das seções. Quando não aplicável, prefira manter o cabeçalho com “Não se aplica: motivo”. Se a seção for removida, use uma nota “Seção N não se aplica: motivo” e não renumere.

Mapeamento esperado:

- §1: problema, motivação, contexto legado em linguagem de negócio e impacto esperado.
- §2: atores humanos, sistemas e hardware que realmente participam; diferencie ator de componente interno.
- §3: RNs ativas com escopo e teste mínimo; substituições rastreadas externamente.
- §4: jornadas completas, incluindo alternativas e exceções ou justificativa de não aplicabilidade.
- §5: capacidades observáveis, MoSCoW, classificação baseada no AS-IS e aceite.
- §6: impacto humano de qualidades, sem parâmetros técnicos.
- §7: delta da iniciativa; contagens, matriz, detalhamento, riscos, recuperação e aprovações coerentes.
- §8: questões reais com ID, origem, impacto, recomendação e decisão necessária. Não descarte porque estão sem resposta.
- Checklist: marcar apenas verificações realmente realizadas e aprovadas; não confundir revisão estrutural com decisão do usuário.

Em migração sem mudança de Produto, §7 tem uma única alteração que preserva as capacidades e remete ao ARCHITECTURE-TO-BE. Seu aceite verifica equivalência de comportamento. Não crie uma alteração por biblioteca, serviço, tabela ou etapa de deploy.

O template pede teste mínimo também para RFs no checklist: o critério de aceite do RF deve cumprir essa função e ser binário. Teste de integração no UC permanece descrição de comportamento. Requisitos de logs, alertas e recuperação descrevem o que precisa ser observável e quem precisa agir, sem escolher uma ferramenta.

## Engenharia sem contaminar o PRD

As evidências podem conter paths e símbolos; mantenha esse detalhe na rastreabilidade ou handoff técnico. No PRD, use links com títulos legíveis de documentos e descreva apenas o comportamento.

Exemplo de separação:

- Qualidade: “O operador percebe a conclusão da solicitação sem ficar em dúvida sobre seu resultado.”
- RNF correspondente: a medição, seu limiar, condições e método ficam no ARCH §9 e dependem de decisão técnica fundamentada.
- Não inventar um tempo, percentual, volume ou ferramenta para tornar a qualidade aparentemente mensurável.

Limites de negócio aprovados pertencem às RNs/RFs e aceites pertinentes. A regra sem números é específica do conteúdo de §6; IDs, numeração de seções e contagens do template não são métricas.

Quando o Discovery contém apenas uma solução técnica, reconstrua o problema e o efeito esperado com o usuário. Registre a solução como proposta de arquitetura, sem tratá-la como requisito de Produto.

## Artefatos no projeto

Reaproveite a organização existente. Sem convenção, use:

```text
docs/PRDs/<iniciativa>/
  PRD.md
  RASTREABILIDADE.md
  CHECKPOINT.md
```

Não duplique esses registros se o projeto já possui equivalentes canônicos. O template original é recurso da skill, não precisa ser copiado para cada projeto.

RASTREABILIDADE contém fontes e versões, classificações de fatos/decisões/propostas, matriz de origem por requisito, IDs ativos/reservados/retirados, substituições, decisões rejeitadas com razões e links de engenharia pertinentes. Registre somente dados necessários, sem segredos ou informações pessoais dispensáveis.

CHECKPOINT contém objetivo, versão do PRD, recorte, estágio, estado de Git observado, trabalho concluído, validações realmente executadas, pendências P0/P1 quando já priorizadas, dúvidas e próxima ação. Não fabrique prioridades para preencher o campo. Registre data de redação e posterior releitura/decisão; não confunda branch/commit atual com ambiente implantado.

O PRD guarda requisitos e comportamento. Progresso, resultados de testes, operações já feitas, hashes e comandos ficam no checkpoint ou registro de evidência. Atualize canônicos somente com suporte e autorização da missão; criação de PRD não autoriza implementação nem redesenho de arquitetura.

## Estado e aprovação

Diferencie rascunho com lacunas, pronto para revisão e aprovado pelo usuário. Aprovação do PRD e aprovações individuais de alterações devem indicar versão, decisão, data, escopo e ressalvas. Checkbox isolado, texto de exemplo ou declaração de outro agente não bastam.

A regra de releitura após uma noite vem do template. Entregue o rascunho no mesmo dia, deixe o item desmarcado e registre que a aprovação depende de releitura confirmada em data posterior. A virada de data não comprova releitura. Não agende tarefa, não espere em loop e não declare que o usuário dormiu. Se o usuário explicitamente mudar a regra, registre a exceção sem reescrever o histórico.

## Revisão semântica antes da entrega

Confira se todas as afirmações de domínio têm suporte ou estado de proposta/lacuna; se atores e capacidades estão cobertos pelos UCs; se limites, negativas e exceções relevantes têm aceite; se prioridades e tags têm fundamento; e se impactos, contagens e dependências em §7 são consistentes.

Confira ciclos ou referências quebradas entre alterações, RN retirada citada como ativa, ID reciclado, qualidade renumerada, alteração de regra escondida como editorial e requisito técnico disfarçado de qualidade humana.

O validador é uma ajuda determinística, não um aprovador. Ele não entende o domínio nem prova equivalência semântica, completude das jornadas, atualidade de decisões ou releitura humana. Toda advertência exige avaliação contextual; nenhum resultado do script autoriza “aprovado”.
