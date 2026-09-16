# Architecture AS-IS: [NOME DO SISTEMA]

> **Propósito:** fotografia descritiva e honesta de como o código atual sustenta o PRD hoje. Não é aspiracional. Não tem opinião sobre o que deveria ser. Documenta como **é**, incluindo as partes feias, dívidas técnicas e decisões questionáveis.

> **Como usar este template:** preencha cada seção lendo o código real. Use a IA (ex: Claude Code apontado pro repositório) para acelerar a leitura, mas revise pessoalmente para garantir fidelidade. Adicione conhecimento histórico que só você tem (decisões de anos atrás, contexto de bugs específicos, etc.).

> **Regra de ouro:** se uma frase começa com "deveria" ou "seria melhor", ela não pertence aqui — vai pro ARCHITECTURE-TO-BE.

---

## 1. Visão Geral

- **Stack atual (versões reais):** [Ex: Node.js 12, Express 4, Sequelize 5, MySQL 5.7, AWS SDK v2]
- **Paradigma arquitetural:** [Ex: Monolito MVC acoplado, microserviço hexagonal, serverless]
- **Diagrama de contexto:** [Texto descritivo ou link para diagrama externo]

---

## 2. Mapa PRD → Código Atual

> Esta tabela é o índice remissivo. Cada item do PRD (RN/UC/RF por ID, ou Qualidade por §6.X) aponta para onde ele vive no código hoje.

| Item do PRD | Componente atual | Arquivo / Localização | Notas |
|---|---|---|---|
| RF01 | [nome do componente] | [path/arquivo.js:linha] | — |
| RN13 | [nome do componente] | [path/arquivo.js:linha] | — |
| UC01 | [nome do componente] | [path/arquivo.js:linha] | — |
| §6.1 [Qualidade] | [como o código atual sustenta isso] | [path:linha ou "espalhado"] | [observação se a sustentação é frágil/não medida/ad-hoc] |

> **Sobre Qualidades nesta tabela:** no AS-IS, frequentemente uma Qualidade do PRD §6 é "sustentada" por código que não foi pensado pra isso (logs ad-hoc, comportamento emergente, efeito colateral). Documentar essa sustentação real — mesmo quando frágil — é o que justifica os RNFs técnicos novos do TO-BE §9. Detalhes vão na Seção 4.5.

---

## 3. Estrutura de Pastas

```
[arvore comentada do projeto, com responsabilidade de cada pasta principal]
projeto/
├── src/
│   ├── controllers/   # [comentário]
│   ├── services/      # [comentário]
│   └── models/        # [comentário]
├── routes/            # [comentário]
└── ...
```

---

## 4. Componentes Principais

### [Nome do Componente]

- **Sustenta:** [PRD IDs que dependem deste componente]
- **Stack:** [libs específicas usadas neste componente]
- **Pattern:** [classe, função, middleware, etc. — descrever, não julgar]
- **Decisões críticas:**
  - [Decisão histórica + justificativa real, ou "decisão histórica desconhecida" quando não souber]
  - [Outra decisão]
- **Dependências externas:** [serviços, APIs, libs externas]

### [Próximo Componente]

[repetir estrutura]

---

## 4.5. Sustentação Atual das Qualidades do PRD §6

> Como cada Qualidade do PRD §6 está sendo sustentada (ou não) pelo código atual. Esta seção é descritiva e honesta — não tenta justificar nem julgar. Documenta o estado real, incluindo quando a sustentação é frágil, ad-hoc, ou inexistente.

> **Por que esta seção existe:** ela é o espelho do AS-IS pra Seção 9 do TO-BE. Quando o TO-BE for criado, cada RNF técnico vai nascer ancorado numa Qualidade que está documentada aqui — e o status atual ("frágil" ou "inexistente") justifica por que o RNF técnico do TO-BE precisa existir. Sem essa seção, o TO-BE §9 fica sem contexto histórico e vira "decisão arbitrária".

### §6.1 [Nome da Qualidade]

- **Como o código atual sustenta:** [Descrição do mecanismo atual — pode ser código intencional, efeito colateral, ou nada]
- **Métrica observada (se houver):** [Latência real medida, uptime real observado, taxa de erro, etc. — ou "não medido"]
- **Localização no código:** [arquivo.js:linha, ou "espalhado em vários lugares", ou "não existe"]
- **Status da sustentação:** ✅ Adequada / 🟡 Frágil / 🔴 Inexistente
- **Observações:** [Por que a sustentação é frágil ou inexistente, se aplicável. Bugs históricos, dependências externas, ausência de instrumentação, etc.]

### §6.2 [Nome da Qualidade]

[repetir estrutura]

### §6.X ...

---

## 5. Fluxos Quentes

> Sequência técnica real de cada UC importante. Quem chama quem, em qual ordem, com referências a arquivos e linhas.

### UC01: [Nome do UC]

1. [Endpoint ou ponto de entrada] → [arquivo.js]
2. [Próximo componente chamado] → [arquivo.js:linha]
3. [Lógica X é executada] → [arquivo.js:linha]
4. ...

### UC02: [Nome do UC]

[repetir estrutura]

---

## 6. Decisões de Implementação Críticas

> Decisões técnicas que afetam o comportamento do sistema. Cada uma com justificativa real (ou "desconhecida" quando aplicável).

| Decisão | Justificativa | Sustenta (PRD IDs ou §6.X) |
|---|---|---|
| [Descrição da decisão] | [Por que foi feita assim] | [IDs ou Qualidades] |

---

## 7. Dívida Técnica Conhecida

> Lista honesta de problemas conhecidos. Não tenta esconder, não exagera. Inclui severidade e impacto.

| Item | Severidade | Impacto | Qualidade afetada (se houver) |
|---|---|---|---|
| [Problema] | 🔴 Alto / 🟡 Médio / 🟢 Baixo | [Como afeta operação ou desenvolvimento] | [§6.X ou "—"] |

> **Sobre a coluna "Qualidade afetada":** se uma dívida técnica afeta diretamente uma Qualidade do PRD §6 (ex: ausência de timeout afeta §6.1 Operação Fluida), citar a Qualidade aqui cria rastreabilidade entre dívida técnica e promessa de produto. Itens sem Qualidade afetada são dívidas internas que não impactam o produto observavelmente.

---

## 8. Operação Atual

### Variáveis de Ambiente
- `[VAR_NAME]`: [propósito]

### Secrets / Credenciais
- [Onde estão armazenados — ex: AWS SSM, .env, etc.]

### Deploy
- [Como deploy é feito hoje — ex: CI/CD, manual, etc.]

### Observabilidade Existente
- [O que existe hoje em termos de logs, métricas, alertas]
- [Limitações conhecidas]

---

## Checklist de Validação Final

Antes de considerar o AS-IS pronto:

- [ ] Cada item do PRD que existe no código (RN/UC/RF) tem linha correspondente na Seção 2
- [ ] Toda Qualidade do PRD §6 tem entrada na Seção 4.5 com status de sustentação atual documentado
- [ ] Qualidades com status 🟡 Frágil ou 🔴 Inexistente estão sinalizadas (essas viram prioridade no TO-BE §9)
- [ ] Cada componente principal está documentado na Seção 4 com referências a arquivos reais
- [ ] Fluxos quentes dos UCs principais estão traçados na Seção 5
- [ ] Dívida técnica está listada honestamente na Seção 7, com Qualidades afetadas marcadas quando aplicável
- [ ] Nenhuma frase começa com "deveria" ou "seria melhor" (isso pertence ao TO-BE)
- [ ] Conhecimento histórico que só você tinha foi adicionado manualmente