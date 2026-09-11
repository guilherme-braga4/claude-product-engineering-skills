# PRD: [NOME DO PROJETO/INICIATIVA]

> **Como usar este template:** preencha todos os placeholders entre colchetes. Apague seções que não se aplicam (com nota explicando por quê). Antes de aprovar, releia procurando vazamentos de engenharia (libs, paths, snippets de código) — eles não pertencem ao PRD.

---

## 1. PROBLEMA & CONTEXTO

- **O que estamos resolvendo:** [Resumo do problema em linguagem de negócio]
- **Motivação:** [Por que agora? Ex: ROI, escala, débito técnico, oportunidade de mercado]
- **Contexto do Legado:** [Breve resumo do estado atual mapeado no Discovery — sem detalhes técnicos]
- **Impacto do Sucesso:** [O que acontece quando terminarmos? Métricas observáveis quando possível]

---

## 2. ATORES

Quais são todos os atores envolvidos nessa iniciativa?

| Ator | Tipo (humano/sistema/hardware) | Como interage |
|------|-------------------------------|---------------|
| | | |

---

## 3. REGRAS DE NEGÓCIO (BUSINESS RULES)

> Regras do domínio que regem o comportamento dos atores. RNs NÃO mudam. Quando uma RN parece estar mudando, na verdade está sendo substituída por outra RN — o ID antigo fica vago, um novo ID é criado.

Categorize por tema quando fizer sentido (ex: "Segurança", "Pagamento", "Detecção").

### [Categoria]

- **RN01:** [Regra em linguagem de negócio]
  - **Escopo:** [Quando aplica]
  - **Teste mínimo:** [Cenário binário verificável — descrição em linguagem natural]

- **RN02:** ...

---

## 4. CASOS DE USO DE PRODUTO

> Jornadas dos atores. Sem tecnologia. Cada UC é uma sequência de ações observáveis de fora.

### UC01: [Nome do Caso de Uso]

- **Ator:** [Quem/o que inicia]
- **Pré-condições:** [Estado necessário do sistema]
- **Fluxo Principal (Happy Path):**
  1. [Passo 1 — sem mencionar tecnologia]
  2. [Passo 2]
  3. ...
- **Fluxos Alternativos:** [Variações esperadas]
- **Fluxos de Exceção:** [O que acontece se algo falhar]
- **Pós-condições:** [Estado final esperado e efeitos colaterais observáveis]
- **Telemetria mínima:** [Que tipo de evento/log deve existir — sem dizer com qual ferramenta]
- **Teste de integração mínimo:** [Cenário(s) que devem existir]

### UC02: ...

---

## 5. REQUISITOS FUNCIONAIS (RF)

> Capacidades observáveis do sistema. Lista numerada com priorização MoSCoW e tag de migração.

- **RF01 — [MUST/SHOULD/COULD/WON'T] — [Tag: `[MANTIDO]` / `[EVOLUÍDO]` / `[NOVO]`]:** [Descrição clara da capacidade]
  - **Critério de aceite:** [Como validar de fora]
  - **Dependências:** [Que outras capacidades, atores ou integrações são necessárias]
  - **Notas:** [Restrições importantes]

- **RF02 — ...**

---

## 6. QUALIDADES ESPERADAS DO PRODUTO

> Esta seção descreve qualidades observáveis que o produto precisa ter para operar corretamente em seu contexto. Cada qualidade é descritiva, focada no impacto humano, sem métricas técnicas.
>
> **As métricas técnicas que sustentam cada qualidade vivem no ARCHITECTURE-TO-BE §9 como RNFs**, ancorados explicitamente nas qualidades desta seção. A relação é: PRD §6 diz POR QUE a qualidade importa pro produto; ARCH §9 diz COMO ela é medida e garantida tecnicamente.
>
> **Regra de ouro desta seção:** se uma frase contém número, métrica, formato técnico ou unidade de medida (ms, %, MB, JSON, HTTP code), ela está vazando engenharia — mover para o ARCHITECTURE-TO-BE §9.

### 6.1 [Nome da Qualidade]

[Descrição do impacto humano. Por que essa qualidade importa pro produto? O que acontece com o usuário/operador/negócio se ela não for atendida? Sem números, sem métricas, sem técnica.]

### 6.2 [Próxima Qualidade]

[mesmo padrão]

### 6.3 [Próxima Qualidade]

...

---

## 7. MUDANÇAS (TO BE)

> **Objetivo:** Documentar APENAS o que será alterado para entregar a iniciativa. Cada mudança mapeia seus impactos em UCs, RNs, RFs e Qualidades para identificar quais testes precisam de atenção máxima.

> **Lembrete:** Se esta é uma migração sem mudança de produto, esta seção contém UMA única alteração apontando para o ARCHITECTURE-TO-BE.

### 7.1 Visão Geral

#### Resumo:

- **Total de alterações:** [X]
- **Classificação:** [X] Migrações | [X] Novas funcionalidades | [X] Refatorações | [X] Remoções | [X] Extensões
- **Estratégia de execução:** [Sequencial / Paralelo / Faseado]

#### Matriz de Impacto:

| # | Alteração | Tipo | Prioridade | Impacto (UC/RN/RF/Qualidade) | Risco |
|---|-----------|------|------------|------------------------------|-------|
| 1 | [Nome] | [Tipo] | MUST/SHOULD/COULD | UC02, RN03, RF05, §6.1 | 🔴🟡🟢 |

---

### 7.2 Alterações Detalhadas

---

#### Alteração 1 — [Prioridade] — [Nome Descritivo]

**Classificação:** [Migração de RN / Novo RF / Extensão de UC / Refatoração / Remoção / etc.]

**Tipo:** [Migração / Criação / Refatoração / Extensão / Remoção]

**Dependências:** [Nenhuma / Depende de Alteração X / Bloqueante para Alteração Y]

##### Descrição:

[O que será alterado e por quê — 2 ou 3 frases. Comportamento, não código.]

##### Impacto:

**UCs Impactados:**
- ✅ **UC0X** — [Descrição do impacto]
- ⚠️ **UC0Y** — [Descrição do impacto]

**RNs Impactadas:**
- ✅ **RN0X** — [Descrição do impacto]
- ➕ **RN0Y** (NOVA) — [Descrição]
- ❌ **RN0Z** — [Descrição do impacto]

**RFs Impactados:**
- ✅ **RF0X** — [Descrição do impacto]
- ➕ **RF0Y** (NOVO) — [Descrição]
- ❌ **RF0Z** — [Descrição do impacto]

**Qualidades Impactadas:**
- ⚠️ **§6.X — [Nome da qualidade]** — [Descrição do impacto. Se a qualidade muda, ela precisa de aprovação consciente. Se só a forma técnica de sustentá-la muda, isso vai pro ARCHITECTURE-TO-BE §9, não aqui.]
- ➕ **§6.Y — [Nome da nova qualidade]** (NOVA) — [Descrição]

**Legenda:** ✅ Alterado | ➕ Novo | ⚠️ Precisa atenção | ❌ Removido

##### O Que Precisa Ser Feito:

**Implementação:** [Descrição de alto nível do que implementar — sem código, sem libs]

**Testes:** [Quais são TODOS os testes a criar/atualizar — RNs afetadas precisam de testes unitários, UCs afetados precisam de testes de integração, Qualidades afetadas precisam dos seus RNFs técnicos verificados]

**Infraestrutura/Observabilidade:** [Apenas o básico — feature flags, dashboards, alertas necessários]

##### Critérios de Aceite:

- [ ] [Critério funcional específico e mensurável]
- [ ] [Critério de qualidade ancorado em §6.X]
- [ ] [Critério de cobertura de testes]

##### Gestão de Risco:

**Risco:** 🔴 Alto / 🟡 Médio / 🟢 Baixo

**O que pode dar errado:** [Descrição do risco principal]

**Como mitigar:**
- [Ação preventiva / detecção / recuperação]
- [Feature flag + plano de rollback]

**Rollback:**
- **Mecanismo:** [Como reverter — feature flag, deploy reverso, etc.]
- **Gatilhos:** [Condições que disparam rollback]

##### APROVAÇÃO:

- [ ] Aprovado
- [ ] Aprovado com Ressalvas: [descrever]
- [ ] Rejeitado: [motivo]
- [ ] Pendente: [o que falta]

**Comentários:** [espaço livre]

---

#### Alteração 2 — [Prioridade] — [Nome Descritivo]

[Repetir estrutura acima]

---

## 8. PERGUNTAS EM ABERTO

(SE NÃO APLICAR, IGNORE)

- [Unknowns que precisam de POC, validação com stakeholders, ou dados adicionais]
- [Decisões pendentes e dependências externas]

---

## Checklist de Validação Final

Antes de aprovar este PRD:

- [ ] Nenhuma menção a libs, funções, classes, paths ou snippets de código (R1)
- [ ] Nenhuma métrica técnica, número, formato ou unidade de medida na Seção 6 (Qualidades) — tudo isso vai pro ARCH §9
- [ ] Todos os IDs (RN/UC/RF) e seções de Qualidade (§6.X) são únicos e não reciclam IDs antigos (R2)
- [ ] Toda RN, UC e RF tem um "teste mínimo" que é binário (R3)
- [ ] Toda Qualidade da Seção 6 descreve impacto humano, não métrica
- [ ] Se é migração sem mudança de produto, Seção 7 está enxuta e aponta pro ARCHITECTURE-TO-BE
- [ ] Cada alteração da Seção 7 mapeia explicitamente UCs, RNs, RFs e Qualidades (§6) impactados
- [ ] Releitura feita após dormir uma noite (PRD nunca aprovado no mesmo dia em que foi escrito)
