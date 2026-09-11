# Compactação segura de contexto

Use os prompts abaixo na conversa ativa, nesta ordem. Primeiro persista e reconcilie o estado. Envie o segundo prompt somente depois que o agente confirmar que a sessão está segura para compactar.

## 1. Antes de compactar

```text
Before compacting this session, persist the important state of the work to the repository.

Review the entire work completed in this session and reconcile it against the current filesystem, git diff, commits, Discovery, Spec, PRD and Implementation Plan.

Persist anything that would be expensive, ambiguous or dangerous to reconstruct after context compaction.

Specifically preserve:

- product/domain discoveries that are now considered true
- architectural decisions and their rationale
- definitions and invariants established during the session
- decisions explicitly rejected and why
- mappings between Discovery → Spec → PRD → implementation
- files/components affected
- implementation already completed
- current git/branch/commit state
- tests executed and their results
- known failures, gaps and technical debt discovered
- assumptions that still need validation
- unresolved questions
- exact remaining P0/P1 work
- next recommended action

Do not duplicate information that already exists correctly in canonical documents. Update the appropriate canonical artifact when the information belongs there.

If information is implementation/session state rather than a product requirement, persist it in an implementation progress/checkpoint document rather than modifying the canonical Spec.

Do not invent or reinterpret previous decisions. Cross-check persisted documentation against the actual code before finishing.

At the end, tell me:

1. what was persisted,
2. which files were updated,
3. what information intentionally remains only in session context,
4. whether the session is now safe to compact.
```

## 2. Compactar

```text
/compact Preserve only the operational context required to continue the current work correctly.

Prioritize:

- the current objective and success criteria
- the current stage of work and exact next action
- important decisions, constraints, invariants, and assumptions still relevant to execution
- unresolved questions, blockers, risks, and remaining work
- references and paths to canonical project artifacts, specs, plans, checkpoints, and other persisted sources of truth
- relevant git/branch/worktree state when applicable
- important verification or test status that affects the next steps

Treat the current filesystem, repository, persisted documentation, and committed project state as canonical. Prefer references to persisted artifacts over reproducing their contents.

Do not preserve information that can be reliably recovered by reading the repository or canonical artifacts again.

Discard:

- verbose tool outputs
- completed exploratory reasoning
- dead ends
- superseded hypotheses
- repeated explanations
- conversational noise
- implementation details already persisted and easily recoverable
- large code excerpts or document contents that can be reread from disk

Preserve enough context to understand why the project is in its current state, what remains to be done, and how to continue without repeating previous discovery or reopening settled decisions.
```

