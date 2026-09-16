# Rodada de inconsistências

## O que abre uma questão

Todo conflito PRD ↔ ARCH deve ser exposto ao usuário antes da reconciliação: comportamento contraditório, requisito removido/alterado sem decisão, qualidade contrariada, arquitetura que amplia escopo, contrato incompatível ou canônicos concorrentes. Inclua conflitos identificados antes e durante a redação.

Classifique sem resolver por conta própria:

| Situação | Tratamento |
|---|---|
| ARCH afirma que retry duplica cobrança, PRD exige cobrança única | Q documental/comportamental com evidências; o usuário decide a reconciliação. |
| PRD pede exportação nova, AS-IS documenta que ela ainda não existe | Delta esperado: ação de implementação, sem Q apenas por essa diferença. |
| Código viola regra clara e ambos os ARCHs reconhecem o estado e a correção | Defeito demonstrado: ação de correção; não exigir nova decisão de Produto. |
| TO-BE propõe infraestrutura sem vínculo com o PRD | Q de escopo ou retirada explícita da proposta sem promover a requisito. |
| Qualidade sem limiar técnico definido | Proponha RNF com fundamento; abra Q se faltar decisão indispensável ou houver incompatibilidade. |
| PRD prevê algo; nenhum ARCH existe ainda | Ausência documental: criar pelos modelos, sem inventar conflito. |

O PRD vigente é a referência de requisitos, não licença para apagar uma contradição silenciosamente. Código continua sendo referência do estado real. Uma decisão pode corrigir o ARCH, confirmar um bug ou solicitar evolução do PRD; esta última requer aprovação explícita do novo requisito.

## Registro por questão

Crie `INCONSISTENCIAS.md` com IDs estáveis `Q-001`, `Q-002` etc. Para cada Q:

- estado: aberta, apresentada, respondida, aplicada, adiada ou substituída;
- fontes e versões, trechos mínimos pertinentes e links às evidências;
- afirmações em conflito e categoria, sem escolher silenciosamente uma delas;
- requisitos/aceites, seções ARCH, ações e lotes afetados;
- impacto e o que fica bloqueado;
- pergunta única, opções viáveis, recomendação fundamentada e consequências;
- resposta efetiva do usuário, proveniência na conversa, data e alcance;
- alteração documental acordada e verificação de consistência após aplicação.

Adiada não significa resolvida. Substituição precisa apontar para a Q sucessora ou decisão que a tornou desnecessária; preserve histórico. Dependências circulares ou resposta ambígua permanecem pendentes.

## Plan mode e perguntas uma a uma

1. Prepare o inventário de Qs e as evidências disponíveis. Antes de alterações dependentes, entre em **Plan mode** usando a capacidade real do ambiente, se disponível. Se o modo restringe escrita, use somente o arquivo de plano permitido ou o registro na conversa; persista nos artefatos autorizados quando sair do modo. Não contorne suas restrições para escrever snapshots.
2. Use **AskUserQuestion** (a ferramenta de perguntas do Claude Code, chamada pelo usuário de “AskUserQuestions”) para apresentar **uma Q por vez**, em ordem de dependência e impacto, com opções e recomendação. Leia a resposta antes de avançar para a próxima Q. Não despeje todas as questões em uma pergunta genérica de aprovação.
3. Em outro ambiente, use o equivalente efetivamente disponível para perguntas em plano, como `request_user_input`, respeitando modo, schema e instruções superiores. Não invente ferramenta nem afirme mudança de modo que não ocorreu.
4. Se não puder ativar Plan mode, peça ao usuário que o ative e mantenha as decisões dependentes bloqueadas. Se a ferramenta de perguntas não existir, informe a limitação e peça autorização para conduzir a rodada uma Q por vez na conversa. Não trate o fallback como cumprimento literal do fluxo solicitado.
5. Após cada resposta, registre decisão e impactos; reavalie as próximas Qs, abrindo novas quando necessário. Silêncio, timeout, sugestão preselecionada e “adiar” não são respostas aprovadas. Não reabra decisões já inequívocas e ainda válidas.
6. Com todas as Qs bloqueantes resolvidas, apresente o conjunto de refinamentos acordados e siga o mecanismo do ambiente para sair de Plan mode. Aplique somente alterações autorizadas: atualizar ARCHs pertence à missão; mudar o PRD exige decisão explícita sobre a alteração concreta. Refaça matriz e paridades depois de mudar fontes.

Trabalho factual e partes independentes podem continuar sob as permissões do modo vigente. Canônicos e TO-BE dependentes do conflito ficam preservados; o snapshot permanece em andamento/parcial. Não libere desenvolvimento dependente nem marque o relatório como pronto enquanto houver conflito bloqueante sem resolução.
