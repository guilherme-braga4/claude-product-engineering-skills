# Rodadas de refinamento e fechamento

Conduza a investigação até não restar decisão ou condição externa obrigatória em aberto para o trecho liberado. O usuário quer resolver as perguntas antes de iniciar a implementação, preferencialmente por `AskUserQuestion`.

## Como perguntar

1. Investigue primeiro o que for verificável. Apresente a evidência, o impacto no trecho e a decisão exata necessária.
2. Use IDs estáveis (`DEP-001`, por exemplo). Agrupe poucas perguntas independentes; resolva primeiro a pergunta que determina as opções das seguintes.
3. Ofereça opções concretas com consequências e uma recomendação quando houver fundamento. Não esconda uma dispensa de aceite sob “seguir mesmo assim”.
4. Use `AskUserQuestion` quando disponível no Claude Code; respeite a interface e limites reais da ferramenta. Não confunda a preferência do usuário por esse nome com sua disponibilidade em outro host.
5. Reaproveite as respostas já dadas. Silêncio, opção preselecionada e tempo decorrido não são aprovação. Não repita perguntas resolvidas, salvo mudança material explicitada.

## Quatro situações que precisam de respostas diferentes

| Situação | O que fecha a pendência |
|---|---|
| Decisão necessária | Escolha explícita registrada, consistente com os documentos aprovados ou revisão aprovada deles |
| Recurso/acesso ausente | Disponibilização e verificação da capacidade exigida; resposta “vou criar” continua pendente |
| Falha que exige correção | Saneamento executado no modo/escopo autorizado e evidência de verificação posterior |
| Checkpoint humano do fluxo | Responsável e momento registrados; continuidade marcada COM CHECKPOINTS. Se o usuário exige zero pausas, a incompatibilidade precisa de decisão antes de liberar |

Não crie uma pergunta para autorizar toda leitura, comando permitido ou atualização do plano. Pergunte quando há informação faltante, decisão de produto/engenharia, alteração de aceite ou ação além da autoridade existente.

## Persistência e fim da rodada

Atualize o relatório/artefato de plano permitido após respostas e verificações relevantes, com: pendências, decisões, evidências, fonte da aprovação e próxima ação. Mantenha o caminho do relatório disponível para continuar após compactação.

Quando depender do usuário, devolva a pergunta ou procedimento concreto e permaneça PENDENTE; esse encerramento de turno não é conclusão da pré-checagem. Continue verificações independentes úteis enquanto possível, sem polling repetitivo ou espera artificial.

Quando tudo estiver verificado, apresente a versão concreta do relatório para aceite das conclusões e escolhas ainda não aprovadas. Não repita aprovação já explícita. Se houver liberação prévia inequívoca para executar após a pré-checagem, registre-a no handoff; não infira essa liberação apenas da aprovação do PRD.

Se Plan mode oferecer uma ação de aprovação que também inicia implementação, deixe explícito o efeito. O objetivo da rodada é entregar o pre-check fechado; a execução só começa quando o usuário a tiver solicitado. O relatório pode permanecer no artefato de plano permitido até ser exportado pelo executor autorizado.
