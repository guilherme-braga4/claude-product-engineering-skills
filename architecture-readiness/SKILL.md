---
name: architecture-readiness
description: "Transforma uma avaliação de Product Engineering Readiness em snapshot datado de arquitetura: AS-IS da base avaliada, TO-BE para atender ao PRD, relatório de mudanças e matriz Produto ↔ Engenharia ↔ validação. Use após Readiness ou para atualizar ARCHs e preparar aprovação do desenvolvimento com base nessa avaliação. Resolve conflitos PRD ↔ ARCH em Plan mode, questão por questão. Não substitui o Readiness nem executa implementação durante a análise."
---

# Architecture Readiness

Converta o diagnóstico de Readiness em uma proposta de Engenharia que o usuário possa aprovar sem reconstruir o raciocínio técnico. Escreva em português, salvo pedido diferente. O PRD define o que o produto deve cumprir; código e evidências descrevem o que existe; o TO-BE propõe como atender ao destino completo da iniciativa.

Fluxo: `Readiness diagnóstico → AS-IS da base avaliada → TO-BE alvo → delta e ações → aprovação do desenvolvimento → implementação → novo Readiness`.

“Estado Readiness” no TO-BE significa **estado alvo que atende aos critérios**, não certificação de que o software já está pronto. Aprovar arquitetura, resolver uma questão, implementar e comprovar prontidão são estados distintos.

## Entradas e limites

- Leia `AGENTS.md`/`CLAUDE.md`, o PRD vigente com objetivo, escopo e aceite, o Readiness identificado (`REVIEW.md`, `COVERAGE.md`, `ACTIONS.md` e checkpoint ou equivalentes), ARCHs existentes e a implementação pertinente. Descubra fontes em `docs/` e siga suas referências; não escolha canônicos apenas pelo nome ou pela data.
- Reutilize IDs de requisitos, critérios, achados e lotes do projeto. Não invente requisitos, metas de qualidade, aprovações ou evidências. Engenharia pode propor RNFs mensuráveis justificados, identificados como propostas até decisão.
- Esta missão autoriza criar os artefatos e criar/atualizar os ARCHs canônicos pertinentes, preservando as versões anteriores. Não modifica automaticamente o PRD, código, testes, configuração ou ambiente. Prepare essas ações para aprovação; respeite autorização já explícita na conversa.
- Sem PRD ou Readiness identificável, registre a entrada pendente e peça especificamente o que falta; continue inventário factual independente, mas não feche TO-BE ou relatório como pronto para aprovação. Readiness parcial/negativo é entrada válida: suas limitações acompanham o snapshot.
- Não inicie Agent Team como efeito desta skill. Se o usuário pedir um time, cumpra as instruções locais e confirme PRD com aceite antes de decompor trabalho ou delegar.

## 1. Fixe a base e prepare o snapshot

Leia [snapshots.md](references/snapshots.md) antes de escrever ou retomar. Identifique iniciativa, release, ambiente, execução do Readiness, revisão do PRD, repositórios/commits e alterações locais. Leia os [modelos AS-IS](assets/ARCH-AS-IS-TEMPLATE.md) e [TO-BE](assets/ARCH-TO-BE-TEMPLATE.md) antes de redigir; use o [modelo de relatório](assets/RELATORIO-TEMPLATE.md) para a entrega decisória.

O AS-IS registra o software **pré-remediação da execução de Readiness**, normalmente a base capturada no começo daquela revisão. Se o código mudou desde então, use a base histórica verificável sem fazer checkout destrutivo. Não chame o checkout novo de “pré-Readiness”. Se a base não puder ser reconstruída, declare a limitação temporal e bloqueie as conclusões dependentes até recuperar evidência ou acordar uma nova avaliação/base com o usuário.

Localize `ARCH-AS-IS`, `ARCHITECTURE-AS-IS`, `ARCH-TO-BE`, `ARCHITECTURE-TO-BE` e equivalentes sem limitar a busca à grafia. Distinga canônicos de snapshots e documentos de outras iniciativas. Havendo canônicos, atualize-os nos caminhos existentes; não crie concorrentes. Preserve extensões úteis e adapte a estrutura aos modelos sem apagar decisões históricas não substituídas.

## 2. Mapeie o estado observado e reconcilie as fontes

Cubra componentes, stack/versões reais, fronteiras, fluxos quentes, contratos, dados, dependências, operação e dívida técnica pertinentes ao PRD. Para cada afirmação factual, cite arquivo/símbolo/linha na base correta ou evidência operacional com ambiente/data. “Não encontrado” exige alcance de busca; “não medido” não significa inexistente.

No AS-IS, preserve seções e numeração do modelo, inclusive §4.5. Faça todas as RNs, UCs, RFs e qualidades aparecerem no mapa de cobertura, incluindo ausentes, parciais, não verificáveis e fora do recorte explicitamente justificados. Qualidade não verificável recebe esse estado adicional, sem forçar “adequada/frágil/inexistente”. Registre desconhecimento histórico; não preencha a justificativa por suposição. Não introduza recomendações no documento descritivo.

Antes de fechar qualquer proposta, compare PRD ↔ AS-IS existente ↔ TO-BE existente ↔ Readiness ↔ evidência. Leia e aplique [inconsistencies.md](references/inconsistencies.md) sempre que houver conflito documental, decisão incompatível, requisito sem definição ou disputa de base. Uma funcionalidade nova ainda não implementada é delta esperado, não conflito por si só. Um ARCH que afirma comportamento incompatível com o PRD exige rodada de inconsistências, mesmo que pareça desatualização simples.

## 3. Projete o destino completo

Use o modelo TO-BE preservando ordem e numeração, inclusive §§8.1 e 9. Os exemplos de stack, pastas, factory functions, DI e Composition Root são ilustrativos: não imponha arquitetura ao projeto. Se uma seção não se aplica, mantenha título e motivo sem renumerar as demais.

- Sustente cada componente e decisão por requisitos/qualidades do PRD, com justificativa, alternativas relevantes e impacto. Mantenha o comportamento aprovado; não esconda mudança de Produto em refatoração.
- Descreva o estado final de toda a iniciativa, inclusive capacidades mantidas. Fases e migração conduzem até ele, sem substituir o destino por um primeiro incremento.
- Em §9, vincule cada RNF-T a uma qualidade do PRD, com métrica/condições/método de verificação e origem da meta. Limiar novo fundamentado é proposta de decisão, não obrigação aprovada. Dependência de definição de Produto abre Q. Não use números ilustrativos dos modelos como requisitos reais.
- Planeje compatibilidade, migração de dados, observabilidade, operação e recuperação quando necessárias ao aceite. Registre tarefas de verificação quando falta apenas evidência; não infira necessidade de redesenho.
- Em §8.1, testes e mecanismos ainda planejados permanecem ⬜ com caminhos identificados como propostos. ✅ exige execução comprovada na base/ambiente relevante; resultado atual não prova um design futuro. Os gates de execução do modelo se aplicam após implementação; não impedem entregar uma arquitetura revisável com testes planejados.

## 4. Produza delta, ações e matriz

Leia [traceability.md](references/traceability.md). Preencha `RELATORIO.md` e `MATRIZ-PRODUTO-ENGENHARIA.md` no snapshot. Mostre o que muda do AS-IS para o TO-BE, o efeito no Produto, o motivo, ações concretas de Engenharia, dependências, riscos e como o aceite será demonstrado. Distinga esse delta do histórico de alterações entre dois snapshots.

Reconcile cada achado/lote do Readiness: ação correspondente, coberto por ação compartilhada, mantido sem mudança, questão bloqueante ou exclusão justificada. Reutilize lotes existentes por execução/ID/revisão; não crie uma segunda fila com o mesmo trabalho. Ações novas recebem pacotes próprios de aprovação no relatório. Não edite `docs/TASKS.md` como fila.

Execute a reconciliação bidirecional descrita na referência e registre contagens e lacunas reais. Complete toda análise acessível antes de entregar; limite a alegação de completude ao escopo e às fontes efetivamente verificadas. Sem mudanças necessárias, entregue o snapshot e a matriz com itens mantidos, sem fabricar ações.

## 5. Feche a proposta e entregue para decisão

Confira preservação dos modelos, links, IDs, cobertura, estados de evidência, temporalidade e questões abertas. Salve a base anterior antes de atualizar canônicos; finalize e indexe conforme o protocolo. Não declare proposta pronta para aprovação com conflitos bloqueantes abertos; entregue o material como parcial e continue a rodada de questões.

Na conversa, apresente: execução/base, estado da proposta, principais mudanças observáveis, resumo dos pacotes para aprovação com alcance/risco/dependências/aceite e links do snapshot, ARCHs, relatório e matriz. Use um exemplo de instrução de aprovação com IDs/revisões reais, claramente identificado como exemplo. Enviar relatório significa entregá-lo nesta conversa e no projeto; não enviar email/mensagem externa sem pedido explícito.

Resolver Q ou aprovar TO-BE não autoriza desenvolvimento por si só. Uma aprovação explícita dos pacotes concretos autoriza seus escopos: encaminhe à execução de lotes do Readiness, ou ao fluxo equivalente do projeto, sem repetir pedidos já respondidos. Não execute remediações durante a autoria do snapshot. Após implementação, uma nova execução de Readiness produz nova base e novo snapshot; preserve os anteriores.
