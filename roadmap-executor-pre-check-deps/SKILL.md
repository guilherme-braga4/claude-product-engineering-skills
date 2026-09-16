---
name: roadmap-executor-pre-check-deps
description: "Preflight an approved roadmap before implementation: inspect code, cross-repository contracts, infrastructure, database, test environments and delivery dependencies in Plan mode; resolve prerequisite questions with the user and produce an evidence-backed execution handoff. Use before roadmap-executor or when changed prerequisites need reassessment."
---

# Roadmap Executor — Pre-check de dependências

Prepare o trecho aprovado do Roadmap para execução contínua. Percorra o caminho que o executor terá de seguir, da primeira alteração à comprovação do último aceite, e feche as condições necessárias antes de liberar a implementação. Escreva em português, salvo preferência diferente do usuário.

## Fronteira: pré-checar, resolver decisões e comprovar prontidão

- Trabalhe em **Plan mode**. Se disponível, use a ferramenta nativa para entrar nesse modo; se não estiver ativo e não puder ativá-lo, explique como iniciar em Plan mode e mantenha a atuação em análise/leitura. Não altere configurações globais nem afirme ter mudado o modo sem confirmação do runtime.
- Leia instruções locais e respeite os acessos já autorizados. Faça inspeções de código e verificações de ambiente compatíveis com planejamento e permissões. Não implemente funcionalidades, corrija código, instale dependências, aplique migrações, publique branches ou altere infraestrutura como efeito implícito da pré-checagem.
- Inspecione scripts antes de executar comandos: até testes, build, health checks e leitura de endpoints podem produzir efeitos. Uma sonda só é apropriada quando seus efeitos são conhecidos e permitidos. Não use Bash/SQL/browser para contornar restrições de Plan mode.
- Uma condição que exige saneamento com escrita continua pendente até execução autorizada pelo usuário ou responsável e comprovação do resultado. Prepare o procedimento concreto e volte a verificar depois; não marque como resolvida só porque há um plano de correção.
- Mantenha o relatório no arquivo de plano permitido pelo runtime, ou apresente-o na conversa quando não houver persistência disponível. Não force gravação em `docs/` se Plan mode bloquear. O handoff deve indicar o local real do relatório; sua exportação ao projeto pode ocorrer posteriormente, no modo e escopo autorizados.
- Esta skill não garante ausência de imprevistos nem que o produto já satisfaz requisitos futuros. Seu veredito é sobre pré-requisitos verificados para um escopo, revisão e ambiente identificados.

## 1. Fixe a base e o limite de autonomia

1. Localize PRD e Roadmap aprovados. Sem eles, solicite especificamente a entrada faltante; não decomponha implementação nem inicie Agent Team. Se houver documentação parcial, registre as lacunas sem inventar aprovação.
2. Reutilize o escopo informado: fase, intervalo ou Roadmap completo. Pergunte apenas se faltar definição que altere a inspeção. Confira todos os itens do trecho escolhido, incluindo sua integração e entrega final.
3. Leia arquitetura, Discovery, decisões, acordos e avaliações anteriores aplicáveis. Identifique contradições, aprovações e revisões vigentes. Não confunda hipótese com decisão.
4. Recupere ou refine o acordo inicial: alcance, checkpoints, revisor, gates delegados, Git, publicação, ambientes e operações de dados. Registre respostas com referências; `roadmap-executor` deve reutilizá-las, não perguntar tudo de novo.
5. Se já há execução em andamento, inspecione commits/worktrees e evidências existentes. Preserve as entregas e audite os pré-requisitos do trabalho restante; não exija reset ou refaça implementação para satisfazer este fluxo.

Arquitetura formal e TaskPlans futuros não são pré-requisitos universais. Sem ARCH, use registros técnicos existentes e identifique apenas decisões realmente necessárias. O TaskPlan continua sendo produzido uma fase por vez pelo executor.

## 2. Percorra cada entrega como se fosse executá-la

Leia [o roteiro de inspeção](references/dependency-scan.md). Para cada entrega/pacote, percorra: requisitos → pontos de código e contratos afetados → dependências → build/testes → produto em execução → revisão → integração/publicação → aceite externo. Registre evidências concretas, não apenas a existência de arquivos.

Cubra todos os itens do trecho aprovado e aprofunde os caminhos compartilhados ou de maior impacto. Uma amostra não sustenta o veredito do trecho inteiro. Aprofundamento deve seguir o alcance da mudança; não transformar o scan em auditoria irrestrita de todos os sistemas da empresa.

Classifique cada dependência:

| Classe | Tratamento |
|---|---|
| Pré-requisito externo já necessário | Precisa estar disponível e comprovado antes de liberar o trecho dependente. Exemplos: acesso ao banco de teste, runtime executável, decisão de contrato. |
| Entrega interna do Roadmap | Pode ainda não existir. Registre produtor, consumidor, ordem e critério de disponibilidade; isso não bloqueia o início quando o plano permite produzi-la antes do uso. |
| Checkpoint humano/externo previsto | Registre responsável, momento e evidência exigida. É uma pausa planejada; não prometa execução ininterrupta através dela. |
| Fora do escopo | Justifique por que não afeta as entregas e seus aceites. Se afetar, reclassifique como pré-requisito. |

Exemplo: uma tabela a ser criada por uma migração prevista no Roadmap não precisa existir hoje; o agente precisa ter ambiente, procedimento e autorização para criar e validar essa tabela quando chegar à tarefa. Já uma credencial externa necessária e indisponível é pendência de preparação.

## 3. Conduza o fechamento das pendências

Leia [o protocolo de refinamento](references/refinement.md). Use preferencialmente `AskUserQuestion` do Claude Code quando disponível; em outro host, use o mecanismo equivalente permitido ou perguntas curtas na conversa. A skill não disponibiliza uma ferramenta que o host não oferece.

Agrupe perguntas independentes e priorize decisões que destravam outras. Proponha opções com consequência e recomendação fundamentada. Não peça ao usuário fatos que você pode verificar no código ou no ambiente.

Mantenha IDs estáveis por pendência. A cada resposta, registre decisão, referência da autorização, impacto e evidência ainda necessária. Volte às áreas afetadas e atualize o relatório. Uma resposta resolve uma escolha; não comprova que acesso, serviço ou instalação passaram a funcionar.

Continue as rodadas enquanto houver investigação útil e decisões a resolver. Não encerre como concluído com lista de pendências transferida ao executor. Quando depender de uma ação/resposta externa, apresente o que falta e aguarde mantendo estado PENDENTE. Não gere loops de perguntas idênticas, não invente consentimento e não prometa continuar executando sem recursos ou respostas.

Se o usuário alterar o recorte, registre a revisão e seu motivo; não remova silenciosamente um bloqueio reduzindo o escopo.

## 4. Produza relatório completo e verificável

Use [PRE-CHECK-REPORT-TEMPLATE.md](assets/PRE-CHECK-REPORT-TEMPLATE.md), adaptando a organização do projeto. Complete a cobertura de cada entrega, inventário de ambiente, dependências, pendências resolvidas/abertas, ações de preparação e handoff. Se uma área não se aplicar, indique o motivo; se não foi inspecionada, indique NÃO VERIFICADO.

Identifique a base por revisões/hashes dos documentos, commits dos repositórios e diffs relevantes não commitados; anote quando e onde as verificações ocorreram. Não exponha segredos, dumps de dados ou credenciais. Preserve relatórios anteriores ao revisá-los.

## 5. Emita dois resultados distintos

**Pré-requisitos:**
- `PRONTO`: todas as áreas aplicáveis foram examinadas; nenhuma decisão necessária está aberta; pré-requisitos externos foram comprovados; dependências internas são executáveis na ordem definida; procedimentos/recursos de validação estão disponíveis. O relatório e suas decisões foram aceitos pelo usuário, aproveitando aprovações já explícitas.
- `PENDENTE`: há impedimento identificado ou decisão necessária sem fechamento.
- `INCONCLUSIVO`: falta acesso/evidência para determinar se uma condição necessária está satisfeita. Esse estado não libera execução.

**Continuidade:**
- `CONTÍNUA NO TRECHO`: não há intervenção humana/externa conhecida necessária durante o trecho liberado, respeitadas as permissões reais e os limites de recursos.
- `COM CHECKPOINTS`: o trabalho pode avançar, mas há checkpoints explícitos com responsável e momento. Se o usuário exige zero pausas, resolver/delegar o checkpoint quando possível ou acordar outro trecho antes de liberar.

Nunca use `PRONTO COM RESSALVAS` para esconder um pré-requisito obrigatório ausente. Riscos residuais explicitamente aceitos não equivalem a critérios obrigatórios dispensados. A aprovação de uma exceção deve revisar expressamente o contrato afetado; não reescreva um gate para coincidir com a falha encontrada.

## 6. Entregue ao executor sem iniciar implementação

Informe veredito, alcance exato, evidências e checkpoints previstos. Com PRONTO, forneça o caminho do relatório e a instrução de `/roadmap-executor` com o mesmo trecho. Aprovar o relatório de pré-checagem não significa mandar implementar; respeite a instrução do usuário para a transição.

O executor fará uma conferência curta da base e dos recursos voláteis. Mudança material de contrato, ambiente, acesso ou escopo invalida apenas as conclusões afetadas e deve voltar a esta pré-checagem. Uma compactação, nova sessão ou ausência de um TaskPlan futuro não invalida por si só uma preparação já comprovada.
