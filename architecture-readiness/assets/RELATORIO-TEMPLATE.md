# Relatório de Engenharia: [sistema / iniciativa]

> Snapshot: [ID e link] · Readiness de origem: [ID e link]
> Base avaliada: [repositórios/revisões/estado local] · PRD: [revisão e link]
> Data e timezone: [data] · Cobertura arquitetural: [completa no escopo / parcial]
> Proposta: [em elaboração / bloqueada por Q / pronta para revisão / aprovada com referência]
> Prontidão observada no Readiness: [veredito original, separado do estado desta proposta]

## 1. Leitura para aprovação

[Explique o que passa a funcionar, o que permanece e por que as mudanças são necessárias. Destaque decisões, custos/riscos materiais e pendências que afetam a aprovação. Não alegue prontidão porque o TO-BE foi escrito.]

| Pacote / revisão | Resultado para Produto e proposta | Alcance | Risco / recuperação | Dependências | Aceite observável | Estado |
|---|---|---|---|---|---|---|
| [chave completa] | [resultado + como chegar] | [fronteira] | [efeito material] | [IDs ou nenhuma] | [condição/ação/resultado] | [proposto etc.] |

**Decisão solicitada:** [conjunto finito de pacotes, arquitetura e/ou Qs; distinguir cada tipo de decisão].

**Limitações:** [fontes, ambiente, evidências e lacunas materiais, ou ausência constatada].

## 2. O que muda: AS-IS → TO-BE

| Delta | PRD / aceite / achado | Hoje: AS-IS e evidência | Destino: TO-BE | Efeito no Produto / motivo | Ações |
|---|---|---|---|---|---|
| D-001 | [links/IDs] | [estado observado] | [seção e proposta] | [efeito observável ou sustentação da qualidade] | [ENG-...] |

**Capacidades preservadas:** [requisitos e como a equivalência será verificada].

**Fora do recorte:** [itens e justificativas do PRD, sem convertê-los em trabalho obrigatório].

## 3. Ações de Engenharia

### ENG-001 — [resultado]

- **Origem:** [PRD/aceite, critério/achado Readiness, D-..., Q se houver].
- **Estado atual e problema:** [evidência].
- **Alteração concreta:** [o que construir/corrigir/remover/documentar/verificar e referência ao TO-BE].
- **Alcance:** [repositórios, componentes e caminhos conhecidos; caminhos novos são propostos].
- **Resultado esperado:** [comportamento/qualidade observável].
- **Dependências e ordem:** [ENG/lotes/Qs/recursos; nenhuma quando aplicável].
- **Risco e recuperação:** [impacto e reversão/migração quando pertinente].
- **Aceite e validação:** [condições, cenários, resultado, método e ambiente; estado atual da prova].
- **Pacote responsável:** [readiness-id/L-xx/rN ou snapshot-id/ARCH-L-xx/rN].

[Repetir para todas as ações necessárias ao escopo; se não houver, declarar a conclusão sustentada.]

## 4. Pacotes de desenvolvimento e sequência

### [Chave completa do pacote] — [resultado]

- **Estado / revisão / base:** [proposto etc.; versão e premissas].
- **Origem:** [lote Readiness existente ou novo pacote arquitetural].
- **Ações e aceites:** [conjunto finito de ENG e critérios].
- **Proposta e alcance:** [escopo concreto revisável, incluindo diferenças frente a revisão anterior].
- **Dependências:** [pacotes, decisões e recursos].
- **Efeitos a autorizar:** [código, testes, specs, operação ou ambiente específico].
- **Riscos e recuperação:** [efeitos materiais].
- **Validação:** [cenários, método e ambiente].
- **Decisão do usuário:** [pendente, ou referência confiável à decisão e escopo].

**Sequência recomendada:** [ordem por dependências; fases conduzem ao destino completo].

## 5. Matriz Produto ↔ Engenharia e cobertura

Matriz detalhada: [MATRIZ-PRODUTO-ENGENHARIA.md](MATRIZ-PRODUTO-ENGENHARIA.md).

| Conferência | Resultado | Contagem / denominador | IDs pendentes e motivo |
|---|---|---|---|
| PRD inventariado ↔ matriz, incluindo exclusões | [passou/falhou/não verificável] | [real] | [lista ou nenhum] |
| RN/UC/RF no escopo ↔ TO-BE §2 ↔ §8.1 | [resultado] | [real] | [lista] |
| Qualidades ↔ AS-IS §4.5 ↔ RNFs §9 ↔ §8.1 | [resultado] | [real] | [lista] |
| Critérios/achados/lotes do Readiness com destinação | [resultado] | [real] | [lista] |
| Deltas com ações; ações com âncora, pacote e aceite | [resultado] | [real] | [lista] |
| Dependências resolvíveis e sem ciclos | [resultado] | [real] | [lista] |

[Distinguir cobertura documental, testes planejados e evidências executadas. Não substituir verificação por percentual.]

## 6. Inconsistências e decisões

Registro: [INCONSISTENCIAS.md](INCONSISTENCIAS.md).

| Q | Conflito / decisão | Estado | Impacto no plano / pacotes bloqueados |
|---|---|---|---|
| [ID] | [resumo e link] | [estado] | [impacto] |

[Se não houve conflito, registrar quais fontes foram comparadas. Registrar metas técnicas propostas e decisões ainda necessárias.]

## 7. Histórico desta proposta e documentos

- **ARCH AS-IS:** [canônico e cópia histórica deste snapshot].
- **ARCH TO-BE:** [canônico e cópia histórica deste snapshot].
- **Base documental preservada:** [sources e manifesto].
- **Snapshot anterior:** [link ou primeira execução].
- **Mudanças desde o snapshot anterior:** [separadas do delta AS-IS → TO-BE].
- **Canônicos atualizados / pendentes:** [caminhos, resultado e motivo].

## Checklist de revisão

- [ ] Base pré-remediação verificável e limitações explícitas.
- [ ] Modelos e numeração preservados; exemplos não foram tratados como decisões.
- [ ] AS-IS factual; TO-BE completo com propostas identificadas.
- [ ] Reconciliação bidirecional sem lacunas indispensáveis.
- [ ] Todas as Qs bloqueantes resolvidas e alterações acordadas aplicadas.
- [ ] Pacotes concretos, sem duplicação e com escopo/revisão/aceite.
- [ ] Links, evidências e sincronização de canônicos conferidos.
- [ ] Aprovação humana registrada apenas quando efetivamente recebida.
