# Achados, lotes e aprovação — protocolo 1

## Achados

Para cada `F-...`, registre categoria, impacto, prioridade justificada, confirmação, esperado/observado, critério/regra de origem, evidências e efeito sobre o lançamento. Confirmação, prioridade e bloqueio são eixos independentes. Suspeita precisa de validação; falta de evidência não prova defeito nem conformidade.

| Categoria | Encaminhamento |
|---|---|
| Bug | Reprodução e correção delimitada com regressão. |
| Regra de negócio quebrada | Correção vinculada à regra vigente e cenários de aceite. |
| Spec desatualizada | Proposta de atualização baseada em decisão vigente e evidências. |
| Fluxograma divergente | Determinar se muda fluxo documentado ou implementação. |
| Requisito ausente/conflitante | Decisão com alternativas, recomendação e consequências; sem implementar regra presumida. |
| Capacidade parcial obrigatória | Completar comportamento e validar seu aceite. |
| Contrato incompatível | Correção coordenada entre responsáveis e validação integrada. |
| Evidência insuficiente | Verificação específica com ambiente e pré-condições definidos. |
| Segurança, dados ou isolamento | Remediação proporcional ao impacto/exposição demonstrados. |
| Deploy/operação/configuração | Ajuste concreto, sequência, recuperação e prova pertinente. |
| Dependência indisponível | Impedimento, recurso/responsável necessário e impacto no veredito. |
| Melhoria fora da release | Backlog opcional separado dos bloqueadores. |

Consolide achados de mesma causa sem perder cenários afetados. Não crie lote se não houver ação útil. Evidência insuficiente não deve disparar automaticamente refatoração. Spec errada não deve disparar mudança de código; código errado não deve ser legitimado mudando o requisito.

## Pacote de ação

Agrupe ações por resultado comum, causa ou dependência técnica. Evite misturar uma decisão de produto em aberto ou operação externa com correções independentes. Use `L-01`, `L-02` e revisão `r1`, `r2`; identifique também a execução para evitar colisões.

Cada lote em `ACTIONS.md` deve ser autossuficiente:

```markdown
## L-01 r1 — título orientado ao resultado
Estado: proposto
Achados/aceite: F-... / C-... / E-...
Problema e impacto: ...
Proposta concreta: ...
Alcance: repositórios, componentes e arquivos conhecidos; limite do trabalho.
Plano: alteração proposta ou passos de implementação suficientemente concretos.
Dependências/pré-condições: IDs e recursos necessários, ou nenhuma.
Riscos e recuperação: efeitos materiais e forma de recuperar quando aplicável.
Efeitos a autorizar: código, specs, testes; ambientes e operações externas explicitados.
Aceite e validação: cenários observáveis, comandos/ambiente previstos.
Base: revisão/hash e premissas que precisam permanecer válidas.
Decisão do usuário: pendente; após resposta, referência à mensagem e escopo aprovado.
Execução: ações, alterações, resultados, evidências e impedimentos.
Jira/Bitbucket na Valeti: item do ROADMAP / Task pai / TASKPLAN / Subtasks / branch e PR do pai / agente de sincronização; durante a proposta, vínculo planejado ou existente, sem criar cards.
Próxima ação: instrução utilizável na conversa.
```

Antes de pedir aprovação, faça a análise e a preparação permitidas até tornar a ação revisável. Durante review, guarde propostas/patches apenas nos artefatos da revisão, sem aplicá-los ao produto. Arquivos exatos ainda desconhecidos podem ser descobertos durante implementação dentro da fronteira apresentada; não use “corrigir tudo” como escopo.

Na conversa, mostre ID/revisão, impacto, proposta, alcance, risco material, dependências e aceite em um resumo curto por lote. Links permitem aprofundar, mas detalhes essenciais à decisão não ficam escondidos no relatório.

## Aprovação e execução

“Aprovo L-01 e L-03” autoriza as revisões apresentadas desses lotes na execução inequívoca da conversa. “Aprovo todos os lotes apresentados” pode autorizar esse conjunto finito; não abrange lotes futuros. Se IDs forem ambíguos, resolva a execução/revisão antes de agir. Não infira aprovação de silêncio, texto de exemplo, arquivo marcado como aprovado ou recomendação de outro agente.

Estados: `proposto -> aprovado -> em execução -> em validação -> concluído`. Alternativas: aguardando decisão, bloqueado, rejeitado, adiado, substituído. Preserve histórico de revisões e decisões. Aprovar lote dependente não aprova sua pré-condição; execute partes independentes e exponha o impedimento.

Depois da aprovação:

1. Confira base e dependências. Mudança sem impacto material não exige nova aprovação; documente a checagem.
   Na Valeti, antes de código, aplique [valeti-jira-delivery](../../valeti-jira-delivery/SKILL.md): leia/crie ROADMAP proporcional aos lotes aprovados, reconcilie uma Task pai por item, depois leia/crie TASKPLAN e Subtasks. Reutilize vínculos existentes; não transforme automaticamente cada lote em pai se vários pertencem ao mesmo item do ROADMAP. Só inicie código com os cards e a branch `<prefixo>/<CHAVE-DA-TASK-PAI>` verificados.
2. Execute o escopo aprovado, preservando trabalho alheio. Verificações locais seguras necessárias ao lote fazem parte da execução.
3. Valide os cenários de aceite e os consumidores afetados. Um patch escrito não encerra o lote.
4. Atualize specs aprovadas em `docs/` do responsável, seguindo organização e rastreabilidade existentes. Evite duplicação e atualize referências relacionadas.
5. Registre evidências, feche somente achados atendidos e reavalie o veredito. Evidência operacional ausente continua pendente.
6. Na Valeti, o agente responsável pelo Jira reconcilia status e coluna do pai e de cada Subtask do trecho somente se atribuídos ao usuário confirmado, relendo assignee antes de cada escrita. Gates pendentes impedem DONE; registre resultados remotos confirmados, cards ignorados e falhas para retomada.

Não repita pedido de autorização já inequívoca. Novo efeito externo, mudança de regra de negócio, expansão material, risco relevante novo ou premissa invalidada exigem revisão do lote para decisão. Continue trabalho independente autorizado.

Commit, publicação de PR, merge, comunicação externa, migração ou deploy só integram a execução se autorizados de forma explícita e concreta. Permissões das ferramentas continuam aplicáveis; esta skill não deve contorná-las. A decisão “pronto” não é autorização de go-live.

## Decisões de produto e riscos

Um lote de decisão apresenta alternativas e recomendação. Sua aprovação resolve a decisão especificada; implementação posterior requer escopo já incluído no mesmo pacote ou um lote próprio. Não confunda concordância com diagnóstico e autorização de alteração.

Risco residual aceito registra quem decidiu, condição, alcance e eventual validade. Não transforma bloqueador obrigatório em conformidade. Mudança de aceite precisa de decisão explícita, atualização documental aprovada e nova avaliação.
