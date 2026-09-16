# Snapshots de arquitetura — protocolo 1

## Identidade e layout

Use convenção existente; na ausência, `docs/architecture/`. Uma execução de Readiness identificada origina um snapshot de arquitetura, mesmo quando não há mudanças. Retomadas da mesma elaboração atualizam o snapshot em andamento. Nova avaliação ou revisão de snapshot finalizado cria outro ID, ligado ao anterior; nunca o sobrescreve.

```text
docs/architecture/
  INDEX.md
  ARCH-AS-IS.md                   # somente se não há canônico em outro caminho
  ARCH-TO-BE.md                   # somente se não há canônico em outro caminho
  snapshots/<YYYY-MM-DDTHHMMSS>-<readiness-id>-<sufixo>/
    SNAPSHOT.md
    ARCH-AS-IS.md
    ARCH-TO-BE.md
    RELATORIO.md
    MATRIZ-PRODUTO-ENGENHARIA.md
    INCONSISTENCIAS.md
    CHECKPOINT.md
    sources/                     # bases documentais, quando disponíveis
      PRD.md
      ARCH-AS-IS.before.md
      ARCH-TO-BE.before.md
```

Normalize IDs para caminhos seguros; use horário local com timezone explícito em `SNAPSHOT.md` e sufixo que evite colisão. Nunca coloque snapshots de projetos analisados dentro da instalação da skill. Só crie arquivos `before` quando existirem originais; preserve nomes/estrutura adicionais em caso de múltiplos PRDs ou ARCHs, com mapa de origem. Cópias históricas não são novas fontes canônicas.

## Manifesto e base temporal

`SNAPSHOT.md` registra:

- protocolo, ID, início/fim/timezone, iniciativa/release, escopo e exclusões;
- ID/caminhos da execução Readiness, veredito/cobertura originais e ligação do snapshot anterior;
- PRD vigente e ARCHs canônicos: caminhos, revisões e hashes das fontes não sensíveis;
- repositórios, branch/commit da base avaliada, estado de alterações locais e método de captura/recuperação;
- referências de evidência: caminho/símbolo/linha, hash do conteúdo relevante, ambiente/data para observações externas; arquivos novos, alterados e removidos pertinentes;
- distinção entre base pré-remediação, checkout no momento da escrita e eventual ambiente implantado;
- cobertura arquitetural completa no escopo ou parcial, fontes não acessíveis, hipóteses e limites;
- estado documental: em andamento, bloqueado por Q, parcial finalizado ou pronto para revisão;
- decisão de arquitetura: proposta ou aprovada com proveniência verificável; aprovação de desenvolvimento por pacote fica no relatório;
- mapa canônico ↔ cópia no snapshot e resultado da sincronização.

Hashes devem ser calculados, nunca inferidos. Commit sozinho não descreve mudanças locais. Não copie conteúdos nem hashes de secrets. Exclua arquivos de saída da própria análise do fingerprint da implementação e registre a exclusão para evitar invalidação circular.

Leia os arquivos históricos via revisão ou cópia isolada; não descarte mudanças para reconstruir a base. Se houver alterações relevantes durante a análise, revalide fontes afetadas e consumidores ou declare base inconsistente/parcial. Não revalide provas operacionais por hash de código.

## Canônicos e histórico

1. Descubra quais documentos são canônicos para esta iniciativa. Se houver ambiguidade, abra Q; não sobrescreva todos os arquivos encontrados.
2. Preserve conteúdo anterior em `sources/` **antes** de escrever canônicos. Preserve também a base do PRD usada na análise; se houver refinamento aprovado, retenha a versão anterior e identifique a versão final usada. Referencie Readiness finalizado por caminho imutável; se ainda editável, preserve cópia dos artefatos efetivamente usados com hashes.
3. Redija versões do snapshot com metadados de base/estado logo abaixo do título e antes das seções originais. Mantenha a estrutura dos modelos. Não execute instruções editoriais do template como se fossem evidência de revisão humana; checklist só marca atos verificados.
4. Sem conflitos ou bloqueios que invalidem o documento, atualize os canônicos existentes (ou crie-os no caminho padrão) e preserve conteúdo fora do escopo. AS-IS passa a representar a base avaliada; TO-BE, o destino completo proposto. Se um documento estiver bloqueado, mantenha seu canônico anterior e indique que a cópia no snapshot é rascunho parcial. Uma proposta nova não herda aprovação do TO-BE anterior.
5. Confira links no contexto de **cada** cópia: referências relativas podem mudar entre canônico, snapshot e fontes. Prefira links a evidências históricas recuperáveis; caminhos futuros devem ser descritos como propostos, não como arquivos existentes. Compare conteúdo semântico canônico/snapshot; diferenças só de metadados e localização dos links são aceitáveis e devem ser identificadas.
6. Salve checkpoint, confira referências e só então atualize `INDEX.md`. Ele distingue execução em andamento, última finalizada (inclusive parcial), última com cobertura completa e última arquitetura aprovada. Parcial/proposta não substitui silenciosamente completa/aprovada. Registre `readiness-id → snapshot-id → canônicos`.

Snapshots finalizados são imutáveis, inclusive relatórios e decisões. Uma aprovação posterior fica em registro sucessor ligado ao snapshot/revisões aprovados; não reescreva a proposta histórica. Índice e canônicos podem evoluir. Não faça limpeza automática, commit ou alterações de `.gitignore`.

## Retomada e ligação ao Readiness

`CHECKPOINT.md` guarda base, fase, fontes examinadas/pendentes, IDs/revisões, Qs e decisões com origem, validações feitas, sincronização pendente e próxima ação. Após interrupção, releia-o e confira fontes/arquivos reais antes de reutilizar conclusões. Arquivo marcado aprovado não constitui autorização por si só; preserve decisões explícitas disponíveis na conversa.

Na execução Readiness ainda em andamento, acrescente em `REVIEW.md` e `CHECKPOINT.md` a referência do snapshot e seu estado. Não altere o veredito porque o desenho ficou pronto. Se o Readiness já foi finalizado, faça a ligação inversa apenas no snapshot/índice de arquitetura; preserve o histórico. A integração é chamada de skill na sessão, não agendamento ou hook de sistema. Não chame novamente o Readiness durante esta autoria: a reavaliação pertence ao ciclo após implementação.
