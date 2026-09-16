# Architecture TO-BE: [NOME DO SISTEMA]

> **Propósito:** projeto prescritivo do código alvo. Descreve o **destino completo** da iniciativa — não pedaços intermediários. Cada decisão técnica é uma escolha consciente, com justificativa explícita ancorada num item do PRD.

> **Como usar este template:** este é o documento mais pesado intelectualmente. Você é o protagonista — a IA pode ajudar a explorar opções, mas as decisões são suas. Não delegue isso à IA sem participar ativamente.

> **Regra de ouro:** cada decisão técnica precisa ancorar num item do PRD (por ID — RN/UC/RF — ou por Qualidade §6.X). Se você quer adicionar algo e não consegue apontar qual item do PRD justifica, é over-engineering — não adicione.

---

## 1. Visão Geral

- **Stack alvo:** [Versões específicas — ex: Node.js 22, ESM, Sequelize 6, etc.]
- **Paradigma arquitetural:** [Ex: Funcional com factory functions e DI via Composition Root]
- **Princípios norteadores (3-5 frases):**
  1. [Princípio 1]
  2. [Princípio 2]
  3. ...

---

## 2. Mapa PRD → Arquitetura Nova

> Tabela que vincula cada item do PRD ao componente técnico que vai sustentá-lo. **Esta tabela deve estar em paridade com a Seção 8.1 (matriz de testes) — todo ID que aparece aqui aparece lá, e vice-versa.**

| PRD ID | Componente | Módulo / Pasta |
|---|---|---|
| RF01 | [nome do componente] | [src/módulo/arquivo.js] |
| RN13 | [nome do componente] | [src/módulo/arquivo.js] |
| UC01 | [nome do componente] | [src/módulo/arquivo.js] |

---

## 3. Estrutura de Pastas

```
[arvore comentada com responsabilidade de cada pasta]
projeto/
├── src/
│   ├── domain/        # regras de negócio puras (testáveis sem mocks)
│   ├── services/      # orquestração, factory functions
│   ├── repositories/  # acesso a dados, abstrai ORM
│   ├── controllers/   # finos, só orquestram
│   ├── infra/         # infraestrutura externa
│   ├── compositionRoot.js  # único lugar de instanciação
│   └── app.js         # setup da aplicação
└── tests/
    ├── unit/          # testa funções puras
    └── integration/   # testa fluxos completos
```

---

## 4. Componentes Principais

### [Nome do Componente]

- **Sustenta:** [PRD IDs]
- **Localização:** [path/arquivo.js]
- **Stack:** [libs específicas]
- **Pattern:** [factory function, classe, etc.]
- **Interface pública:** [funções/métodos expostos]
- **Dependências (injetadas):** [outros componentes que recebe]
- **Decisões:**
  - [Decisão 1 + justificativa apontando pro PRD]
  - [Decisão 2 + justificativa]

### [Próximo Componente]

[repetir]

---

## 5. Composition Root

> Como os serviços são instanciados e injetados. Esboço de código aceito (não precisa ser final).

```javascript
// [path/compositionRoot.js]
// Esboço da construção da árvore de dependências
```

**Justificativa:** [por que essa estrutura, o que ela permite — testes substituírem dependências, etc.]

---

## 6. Fluxos Quentes (TO-BE)

> Sequência técnica de cada UC no novo design. Mostra como a nova arquitetura sustenta o mesmo comportamento observável do PRD.

### UC01: [Nome do UC]

1. [Endpoint] → [controller]
2. [Controller chama] → [service]
3. [Service usa] → [domain function + repository]
4. ...

**Diferença chave do AS-IS:** [o que mudou em termos de testabilidade, organização, etc.]

### UC02: [Nome do UC]

[repetir]

---

## 7. Decisões de Implementação

> Cada decisão tem justificativa explícita ancorada no PRD. Sem âncora, a decisão não pertence aqui.
>
> **Diferença em relação à Seção 9 (RNFs):** decisões de implementação são escolhas pontuais sobre como construir (qual lib, qual pattern, qual estrutura). RNFs são especificações mensuráveis de qualidade (latência, uptime, formato exato). As duas categorias coexistem no ARCH mas têm naturezas diferentes.

| Decisão | Justificativa | Sustenta (PRD IDs ou §6.X) |
|---|---|---|
| [Decisão técnica] | [Por que essa escolha, não outra] | [IDs] |

---

## 8. Estratégia de Testes

- **Unitários (`tests/unit/`):** [o que testam, com qual ferramenta]
- **Integração (`tests/integration/`):** [o que testam, com qual ferramenta]
- **E2E (se aplicável):** [o que testam]
- **Convenção de nomeação:** [como os testes citam IDs do PRD — ex: `describe('RN13: deduplicação 30s', ...)`]
- **Cobertura mínima exigida:** [100% dos IDs do PRD na matriz §8.1, ou outro critério]

---

## 8.1 Matriz de Rastreabilidade PRD ↔ Testes

> Esta matriz é o checklist mestre de cobertura. **Todo ID do PRD (RN/UC/RF) e toda Qualidade do PRD §6 aparecem aqui sem exceção.** É o que transforma "testes passando" numa métrica confiável de sucesso.

### Convenção

- ⬜ Não implementado
- 🟡 Implementado mas falhando (TDD: teste escrito antes da implementação)
- ✅ Implementado e passando
- 🔍 Validação manual em andamento (RNFs não-automatizáveis)
- ❌ Item do PRD descoberto sem teste correspondente (bloqueia gate de fase)

### Regras de Negócio (RN)

| ID PRD | Descrição curta | Tipo de teste | Arquivo de teste | Status |
|---|---|---|---|---|
| RN01 | [descrição] | Unitário | tests/unit/[arquivo].test.js | ⬜ |
| RN02 | [descrição] | Unitário | tests/unit/[arquivo].test.js | ⬜ |

### Casos de Uso (UC)

| ID PRD | Descrição curta | Tipo de teste | Arquivo de teste | Status |
|---|---|---|---|---|
| UC01 | [descrição] | Integração | tests/integration/[arquivo].test.js | ⬜ |

### Requisitos Funcionais (RF)

| ID PRD | Descrição curta | Tipo de teste | Arquivo de teste | Status |
|---|---|---|---|---|
| RF01 | [descrição] | Integração | tests/integration/[arquivo].test.js | ⬜ |

### Qualidades do PRD §6 e seus RNFs Técnicos

> Esta tabela rastreia cada qualidade do PRD §6 até o RNF técnico do ARCH §9 que a sustenta, e até o mecanismo de verificação que prova o cumprimento.

| Qualidade PRD | RNFs que sustentam | Tipo de verificação | Status |
|---|---|---|---|
| §6.1 [Nome da qualidade] | RNF-T01 | Teste de carga (`tests/perf/[arquivo]`) | ⬜ |
| §6.2 [Nome da qualidade] | RNF-T02, RNF-T03 | Teste de contrato + observação produção | ⬜ |
| §6.X [Nome] | RNF-T0X | Dashboard + alerta (validação alternativa) | 🔍 |

### Validação Alternativa para Qualidades Não-Automatizáveis

> Algumas qualidades do PRD §6 só podem ser validadas em produção ou por observação manual.

| Qualidade PRD | Por que não automatizável | Mecanismo de validação | Quando validar |
|---|---|---|---|
| §6.X [nome] | [razão] | [dashboard, teste com hardware real, etc.] | [quando aplicar] |

### Verificação de Cobertura

Antes de fechar qualquer fase, esta verificação deve passar:

1. **Cobertura completa:** todo ID do PRD (RN/UC/RF) e toda Qualidade §6.X tocada pela fase tem linha na matriz com status ✅ (ou tem mecanismo de validação alternativa executado).
2. **Sem buracos:** nenhum ID do PRD nem Qualidade tocada pela fase tem status ❌ ou ⬜.
3. **Qualidade revisada:** os testes adicionados na fase foram revisados manualmente pelo Product Engineer com a pergunta: "se eu sabotasse a implementação de forma sutil, esse teste pegaria?". Se a resposta for não, o teste é reescrito antes do gate fechar.

---

## 9. Sustentação Técnica de Qualidades (RNFs)

> Esta seção contém os Requisitos Não-Funcionais técnicos que sustentam as Qualidades Esperadas do PRD §6. Cada RNF cita explicitamente qual qualidade do PRD ele sustenta. **RNF sem âncora em qualidade do PRD não pertence aqui — é over-engineering.**

> **Por que RNFs vivem aqui e não no PRD:** RNFs são especificações técnicas mensuráveis (latência em ms, uptime em %, formato JSON exato). Esses detalhes são especializações técnicas que sustentam qualidades do produto, não promessas de produto em si. O PRD §6 promete a qualidade ("cancelas operam sem atraso perceptível"); o ARCH §9 traduz essa promessa em métrica verificável ("latência p95 <500ms").

> **Diferença em relação à Seção 7 (Decisões de Implementação):** decisões de implementação são escolhas pontuais sobre COMO construir (qual lib, qual pattern). RNFs são especificações mensuráveis de QUALIDADE (latência, uptime, formato). As duas categorias coexistem no ARCH mas têm naturezas diferentes.

### 9.1 Performance

- **RNF-T01:** [Métrica técnica específica e mensurável]
  - **Sustenta:** PRD §6.X — [Nome da Qualidade]
  - **Verificação:** [Como é medido — teste de carga, dashboard, observação manual, etc.]

### 9.2 Disponibilidade & Resiliência

- **RNF-T0X:** [Métrica]
  - **Sustenta:** PRD §6.X — [Nome da Qualidade]
  - **Verificação:** [Método]

### 9.3 Segurança & Compliance

- **RNF-T0X:** [Especificação técnica]
  - **Sustenta:** PRD §6.X — [Nome da Qualidade]
  - **Verificação:** [Método]

### 9.4 Observabilidade

- **RNF-T0X:** [Especificação técnica]
  - **Sustenta:** PRD §6.X — [Nome da Qualidade]
  - **Verificação:** [Método]

### 9.5 Contratos de Interface Externa

> Formatos exatos exigidos por sistemas externos (câmeras, APIs de parceiros, webhooks). Esses contratos são especificação técnica fixada por compatibilidade, não decisão arquitetural livre.

- **RNF-T0X:** [Formato exato]
  - **Sustenta:** PRD §6.X — [Nome da Qualidade]
  - **Imposto por:** [qual sistema externo exige esse formato]
  - **Verificação:** [teste de contrato, validação manual com sistema real, etc.]

---

## 10. Migração / Compatibilidade

> Se aplicável: como o novo coexiste com o antigo durante a transição. Strangler Fig, feature flags, blue/green, etc.

[Estratégia detalhada]

---

## 11. Operação Alvo

### Variáveis de Ambiente
- `[VAR_NAME]`: [propósito]

### Secrets / Credenciais
- [Onde armazenar]

### Deploy
- [Como deploy será feito]

### Observabilidade
- [Métricas, dashboards, alertas alvo]

---

## Checklist de Validação Final

Antes de considerar o TO-BE pronto para começar a execução:

- [ ] **Paridade de comportamento:** lista de IDs únicos da Seção 2 (RN/UC/RF) == lista de IDs únicos da Seção 8.1 (matriz de testes)
- [ ] **Paridade de qualidades:** toda Qualidade do PRD §6 aparece na Seção 9 do ARCH com pelo menos um RNF-T que a sustenta
- [ ] **Sem RNF órfão:** todo RNF-T da Seção 9 cita explicitamente a Qualidade do PRD §6 que sustenta
- [ ] **Sem qualidade órfã:** toda Qualidade do PRD §6 tem entrada na tabela "Qualidades do PRD §6 e seus RNFs Técnicos" da §8.1
- [ ] Cada componente da Seção 4 cita os IDs do PRD que sustenta
- [ ] Cada decisão de implementação da Seção 7 tem justificativa apontando pro PRD
- [ ] A estratégia de testes (Seção 8) cobre TDD em escala de fase
- [ ] A Seção 8.1 lista TODOS os IDs do PRD (RNs, UCs, RFs) e todas as Qualidades §6, mesmo que ainda ⬜
- [ ] Nenhuma decisão técnica foi tomada por viés pessoal sem âncora no PRD
- [ ] O destino descrito é o estado COMPLETO após a iniciativa, não pedaços intermediários