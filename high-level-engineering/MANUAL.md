# Manual — High-Level Engineering

## Quando invocar

Use para entender a engenharia atual do projeto e conectar uma necessidade de Produto à arquitetura, aos componentes, contratos, dados, riscos e validação. É adequada para discovery técnico, desenho de solução, revisão arquitetural e planejamento de implementação.

Para inventário completo do Produto existente, use `product-as-is`. Para decidir se uma release pode ser lançada, use `product-engineering-readiness`.

## Invocação mínima

Abra o Claude Code na raiz do repositório e envie:

```text
/high-level-engineering
Entenda o contexto atual deste projeto e avalie a solução para [objetivo].
```

## Entrada recomendada

```text
/high-level-engineering

Objetivo de Produto:
[resultado esperado]

Escopo:
[capacidades, sistemas ou repositórios envolvidos]

Critérios de aceite:
[condições observáveis de sucesso]

Contexto adicional:
[PRD, spec, decisão, fluxograma, chat ou handoff]

Restrições:
[prazo, compatibilidade, segurança, operação ou limites de mudança]
```

Não é necessário preencher o que já estiver documentado: a skill começa por `docs/`, lê instruções do repositório e confronta documentação com código, testes e configuração atuais.

## O que esperar

- Estado atual com evidências.
- Fronteiras e responsabilidades dos componentes.
- Alternativas, recomendação e trade-offs.
- Impactos em contratos, dados, integração e operação.
- Direção de implementação e estratégia de validação.
- Specs criadas ou atualizadas quando a missão autorizar mudanças.

O contexto herdado de outro chat deve ser fornecido ou referenciado. Ele orienta a investigação, mas decisões e status relevantes são revalidados nas fontes atuais.

## Antes de compactar

Use os prompts de [CONTEXT-COMPACTION.md](CONTEXT-COMPACTION.md) ao final de uma etapa longa ou antes de `/compact`.

