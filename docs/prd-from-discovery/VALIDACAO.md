# Validação — PRD a partir de Discovery

Data: 2026-09-11.

## Entrega e origem

A skill está versionada em [prd-from-discovery](../../prd-from-discovery/SKILL.md). A instalação pessoal do Claude Code usa um link para essa pasta, de modo que mudanças versionadas sejam refletidas na instalação. Invocação: `/prd-from-discovery`.

O [template fornecido](../../prd-from-discovery/assets/PRD-TEMPLATE.md) foi preservado integralmente; a única normalização foi adicionar a quebra de linha ao final do arquivo. O [manual](../../prd-from-discovery/MANUAL.md) e o [protocolo de compactação](../../prd-from-discovery/CONTEXT-COMPACTION.md) acompanham a skill.

## Contrato implementado

| Necessidade | Implementação |
|---|---|
| PRD nas oito seções do modelo e checklist | Template em assets e instruções de autoria em SKILL.md. |
| Discovery como origem verificável | Classificação de fatos, decisões, propostas e lacunas; registro auxiliar de rastreabilidade. |
| RN imutável, sem reciclagem de ID | Protocolo de substituição, reserva de IDs antigos e confronto com a base. |
| Produto separado de Engenharia | PRD em linguagem observável; métricas técnicas e soluções no ARCH ou handoff pertinente. |
| Mudanças com impacto e aceite | Matriz de RN/UC/RF/qualidade e detalhamento de alteração segundo o modelo. |
| Aprovação após releitura posterior | Rascunho entregue imediatamente; aprovação humana e confirmação de releitura registradas sem inferência. |
| Continuidade após compactação | Checkpoint e rastreabilidade mantêm estado, decisões, rejeições e IDs. |

## Verificações realizadas

- Validador de skill: `Skill is valid!`.
- Links locais do novo conteúdo e do README conferidos.
- Texto do template comparado com o arquivo fornecido, aceitando somente a quebra final descrita acima.
- Protocolo de compactação comparado com o das skills existentes.
- Quinze testes automatizados do validador passaram: estrutura válida, seção ausente, omissão justificada, RN duplicada, campo vazio, métrica técnica em §6, número de negócio fora de §6, prioridade e tag ausentes, placeholder, hyperlink legítimo, referência indefinida, RN alterada sob mesmo ID, RN com novo ID, contagem de alterações em migração e bloco de código indevido.
- CLI do validador executada sobre o template não preenchido: rejeição estrutural correta, saída JSON válida e sinalização de revisão humana obrigatória.
- Link de instalação pessoal conferido contra a pasta versionada.

## Limites

Os testes exercitam o script de verificação, não a geração de um PRD por uma LLM. Não foi executada avaliação nativa de autoria no Claude Code nesta entrega. Nenhum PRD de produto foi gerado ou aprovado por estes testes.

O script detecta apenas parte dos problemas estruturais e lexicais. Não decide se uma regra mudou semanticamente, se uma fonte está vigente, se há cobertura completa de jornadas, se o aceite é adequado ou se ocorreu releitura humana. Avisos sobre IDs externos/históricos exigem interpretação. Comparação com uma única versão anterior não garante ausência de reciclagem em todo o histórico.

Para validar a autoria em uso real, os primeiros cenários relevantes são: Discovery incompleto, nova frente que substitui uma RN, migração sem mudança de Produto e Discovery contendo uma solução técnica sem problema de negócio estabelecido. O resultado deve ser avaliado pelas evidências e pelo template, sem interpretar sucesso estrutural como aprovação do conteúdo.
