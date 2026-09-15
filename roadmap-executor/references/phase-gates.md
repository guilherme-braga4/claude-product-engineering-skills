# Gates de fase e conclusão

Leia ao planejar e fechar cada fase. Os critérios aprovados do projeto governam o gate. Este checklist complementa a ausência de um template local e não relaxa exigências existentes.

## Execução e revisão

- Todas as tarefas da fase têm aceite comprovado.
- O revisor acordado avaliou o código e os achados bloqueantes foram corrigidos e reavaliados.
- Gates humanos só são considerados atendidos por agente quando explicitamente delegados e identificados como revisão por agente.
- O código está integrado no destino autorizado e as evidências se referem ao estado integrado relevante.

## Testes e comportamento real

- Toda a suíte exigida pela fase/projeto passa, incluindo a suíte completa quando exigida pelo template do usuário.
- Nenhum teste foi pulado, ignorado, comentado ou enfraquecido para obter aprovação. Falhas anteriores não viram exceções implícitas.
- As jornadas aplicáveis foram exercitadas no projeto em execução e os efeitos relevantes conferidos em UI, API, banco, logs ou sistemas correspondentes.
- Os testes novos foram revisados quanto à capacidade de detectar falhas sutis; mocks não substituem o comportamento que deveriam verificar.
- Validações alternativas exigidas ocorreram no ambiente e momento previstos e têm evidência. Validação ainda aguardando produção/hardware não recebe PASS.

## Rastreabilidade

- Cada RN/UC/RF e Qualidade tocados pela fase está na matriz com evidência de cumprimento; RNF-T referencia sua Qualidade quando existe arquitetura formal.
- Se houver ARCH TO-BE, preserve a matriz §8.1, a paridade com §2 e as relações com RNF-T de §9. Sem ARCH, use o registro canônico equivalente definido na preparação.
- Nenhum requisito tocado fica sem verificação, falhando ou em andamento. Um mecanismo alternativo apenas descrito não é validação executada.
- Os estados dos requisitos das fases futuras podem permanecer pendentes. A conclusão final deve cobrir todo o escopo aprovado e suas exclusões explícitas, sem reduzir escopo por conveniência.
- Matriz e código são versionados juntos quando exigido pelo projeto. Artefatos grandes/temporários podem viver no armazenamento de evidências indicado, com referências duráveis.

## Documentação e sucesso

- Estado de execução atualizado e acessível na retomada; `CLAUDE.md` aponta ao estado canônico.
- Discovery Log registra aprendizado relevante; refinamentos técnicos autorizados aparecem na arquitetura ou registro equivalente.
- O critério de sucesso do Roadmap foi verificado pelo comportamento observável de fora, e não apenas pela estrutura interna do código.
- Retrospectiva registrada após aprovação, antes de planejar a próxima fase.

## Quando falha

Não feche a fase. Registre causa e evidências; corrija e reexecute verificações afetadas e obrigatórias. Use rollback apenas quando o procedimento/gatilho aprovado exigir, preservando dados e trabalho alheios. Gate falhando durante desenvolvimento não exige automaticamente desfazer todas as alterações.

## Encerramento global

Após a última fase autorizada, valide as jornadas integradas do trecho e todos os critérios transversais aplicáveis. Só declare 100% do Roadmap quando todas as fases do escopo aprovado, revisões e validações obrigatórias tiverem sido atendidas. Pare por checkpoint, limite ou bloqueio com esse estado explícito, sem convertê-lo em sucesso.
