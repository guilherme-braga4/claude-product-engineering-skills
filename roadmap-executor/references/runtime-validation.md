# Validação do produto em execução

Leia na preparação e ao planejar cenários que exercitam o sistema. A escolha de ferramentas depende do projeto e dos acessos disponíveis. Não exija interface gráfica de um sistema sem UI, nem DB de um projeto sem persistência.

## Preparar um ambiente reproduzível

Parta da receita de ambiente e validação verificada no relatório de `roadmap-executor-pre-check-deps`. Rediscubra apenas o que mudou desde a base examinada ou não foi coberto pelo relatório.

1. Descubra a receita real em documentação e configuração: dependências, build, migrações, serviços, workers, comandos de início, portas e dados de teste. Use versões e procedimentos do projeto.
2. Confirme o destino efetivo da aplicação e dos clientes de DB/API antes de executar ações. Confira nomes de ambiente e banco sem expor credenciais.
3. Reutilize serviços saudáveis compatíveis com a revisão em teste. Caso precise iniciar serviços, registre comando, PID/sessão, portas e logs. Aguarde prontidão observável; tempo de espera fixo não comprova que a aplicação subiu.
4. Identifique ferramentas existentes: automação de navegador, Playwright ou equivalente, cliente HTTP como curl ou coleção Postman, CLI/driver/conector do banco. Não alegue acesso porque uma ferramenta foi mencionada. Instalação ou configuração segue as permissões do ambiente e o acordo.
5. Prepare contas e fixtures identificáveis por execução. Considere jobs assíncronos e integrações que possam disparar efeitos fora do ambiente de teste.

Se faltar um recurso necessário ao aceite, resolva a preparação dentro do acordo; se for pré-requisito externo novo, registre o delta e devolva-o à pré-checagem antes de implementar o trecho dependente. Não substitua silenciosamente execução real por mocks.

## Planejar um cenário por comportamento relevante

Vincule cada cenário aos IDs do PRD/Qualidades e, quando aplicável, RNF-T. Descreva pré-condições, ação, resultado esperado, efeitos persistidos e evidência. Inclua alternativas e exceções exigidas pelo PRD, além do caminho feliz.

### Interface

- Rode a aplicação e percorra a jornada usando controles reais, sessão e permissões da conta de teste.
- Verifique conteúdo e estado resultantes, navegação, mensagens e recarga quando a persistência for relevante. Um clique bem-sucedido ou screenshot isolado não prova a jornada.
- Consulte erros do navegador, rede e logs para investigar falhas. O uso direto da API não substitui o cenário de UI quando o aceite exige a interface.
- Use seletores estáveis quando houver automação e preserve evidências dos estados relevantes. Não invente observações de tela não inspecionada.

### API e HTTP

- Use curl, Postman/Newman, cliente de testes ou ferramenta disponível contra o serviço realmente iniciado.
- Verifique status, headers e corpo conforme o contrato, além dos efeitos produzidos. Um HTTP 200 pode conter erro de negócio ou não ter persistido a operação.
- Teste autorização, entradas inválidas, idempotência e demais casos somente quando pertinentes aos requisitos/alterações.
- Não inclua segredos no histórico de comandos ou nos artefatos. Registre uma requisição reproduzível sanitizada, usando referências ao mecanismo de autenticação.

### Banco de dados

- Descubra schema e relações no código, migrações e metadados; não invente tabelas ou campos.
- Faça consultas pontuais para observar pré/pós-condições, relacionamentos, unicidade, segregação, auditoria ou estados exigidos. Limite resultados aos registros de teste necessários.
- Correlacione a requisição ou ação de UI com os registros produzidos, usando identificadores rastreáveis da execução.
- Escritas diretas, seeds e migrações seguem o acordo. Use-as para preparar fixtures quando adequado; inserir diretamente o resultado esperado no DB não valida o fluxo da aplicação que deveria produzi-lo.
- Não suponha que o rollback da conexão do cliente desfaz escritas feitas por outra conexão da aplicação. Limpeza exige identificar os recursos realmente criados.

### Processamento assíncrono e integrações

- Para filas, workers e efeitos assíncronos, aguarde a condição observável com prazo definido pelo contrato/ambiente; registre timeout como falha ou bloqueio investigável.
- Quando o cenário precisar de serviço externo real, use o sandbox ou destino autorizado. Identifique limites dos simuladores: eles comprovam somente o comportamento exercitado, sem promover a conclusão a integração real.

## Ciclo de correção

Execute → observe interface/API/DB/logs → identifique causa → corrija → repita o cenário → execute regressão pertinente.

Transforme bugs relevantes em testes duráveis quando isso proteger comportamento. Não crie testes que apenas repetem a implementação. Preserve os checks canônicos e explique alterações legítimas nos testes ao revisor; nunca remova casos ou reduza expectativas para obter aprovação.

## Evidências

Para cada cenário, registre:

- ID do critério, data, ambiente e revisão exata do código; se houver alterações não commitadas, identifique o diff em teste.
- Pré-condições, identidade não secreta da conta/fixture e operação executada.
- Resultado esperado e observado, com PASS/FAIL/BLOQUEADO.
- Referências a relatório de teste, screenshot, trace, resposta HTTP sanitizada, consulta/resultado limitado ou log correlacionado, conforme necessário.
- Quem executou, quem revisou e eventuais limitações de cobertura.

Guarde evidências no local de artefatos do projeto, sem dumps amplos de dados, tokens, cookies ou informações pessoais desnecessárias. A matriz de rastreabilidade aponta para essas evidências; não basta marcar um checkbox. Evidência do código anterior deve ser reavaliada após mudanças que afetem o comportamento.

## Encerrar e limpar

Limpe apenas os dados e recursos de teste identificados como criados pela execução e cuja remoção esteja autorizada. Não apague dados preexistentes ou resete bancos compartilhados como rotina. Registre resíduos que exijam ação posterior.

Encerre apenas processos iniciados pelo executor quando não forem necessários para a próxima fase, revisão ou uso solicitado. Se mantiver a aplicação rodando, registre como acessá-la e encerrá-la. Não mate processos por porta sem confirmar ownership.
