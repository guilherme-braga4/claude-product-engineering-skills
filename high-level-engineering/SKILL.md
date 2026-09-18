---
name: high-level-engineering
description: "Understand a project's current engineering context from docs/ and code, then shape or review high-level solution architecture, decisions, and trade-offs. Use for architecture discovery, product-to-engineering alignment, system design, and technical planning; do not use for isolated low-level coding tasks."
---

# High-Level Engineering Context

Use this skill when the work requires understanding how a product need fits into an existing system and producing a reliable direction for engineering. The central responsibility is to connect:

`product need -> current project context -> architectural decision -> implementation impact -> validation evidence`

The repository's `docs/` directory is the primary source of truth for specifications. The codebase is the source of truth for behavior that is actually implemented. Keep both aligned during the mission.

## Start with the current context

Before recommending a solution or reviewing one:

1. Identify the repository root and read the applicable `AGENTS.md`, `CLAUDE.md`, and other local instructions.
2. Inspect `docs/` first. Discover the relevant PRDs, specifications, architecture records, contracts, diagrams, and status documents with targeted searches; do not assume that a filename is current.
3. Follow references from the relevant documents and identify which document is canonical, which is historical, and which has been superseded.
4. Inspect the implementation that matters to the request: source files, configuration, schemas, migrations, API definitions, tests, and deployment or operational configuration as needed.
5. Compare the intended behavior in the specs with the behavior evidenced by the code and tests.

Do not treat inherited conversation context, memory, or a previous fork as authoritative. Revalidate any decision, status, pending item, approval, or test result that affects the current mission.

If `docs/` is missing or does not cover the subject, say so explicitly and use the strongest available evidence. Do not invent requirements to fill the gap. Recommend or create the missing specification in `docs/` when the mission requires a durable decision.

For work spanning repositories, perform this context pass in each affected repository. Establish which repository owns each requirement and contract, and link to that canonical source instead of copying rules that can drift.

## Maintain the specifications in `docs/`

Specification maintenance is part of high-level engineering work.

- Put every new PRD, architecture decision, contract, flow, or other durable specification in the responsible repository's `docs/` directory, following its existing organization and naming conventions.
- Before creating a document, check whether an existing spec should be updated. Avoid duplicate sources of truth.
- When evidence shows that a relevant spec is outdated, update it as part of the mission when the change is within the authorized scope. Keep related specs and contracts coherent.
- Preserve traceability according to the repository's conventions: identify what changed, what decision is now current, and what prior decision was superseded.
- Do not silently rewrite product requirements to match an implementation. Classify the discrepancy as outdated documentation, implementation drift, an unapproved proposal, or an unresolved product decision.
- If the mission is explicitly read-only or lacks authorization to edit files, report the outdated spec and provide the precise proposed update instead of mutating it.

At the end, name every spec created or updated and mention material divergences that remain unresolved.

## Analyze at the solution level

Begin with the product problem, desired outcome, constraints, and acceptance criteria. Then determine the smallest coherent solution that satisfies them.

Cover the dimensions that matter to the request:

- system and domain boundaries, ownership, and responsibilities;
- components, modules, services, and their interactions;
- APIs, events, schemas, data ownership, and lifecycle;
- failure modes, retries, idempotency, consistency, and recovery;
- security, privacy, tenancy, and authorization boundaries;
- performance, availability, observability, operations, rollout, and migration;
- compatibility, maintenance cost, and likely evolution.

Do not turn this list into a mandatory checklist for a small task. Go to implementation detail only when it establishes feasibility, reveals a real constraint, clarifies a contract, or explains how the decision will be validated.

For each consequential decision, state:

1. the need or constraint that makes a decision necessary;
2. the viable alternatives considered;
3. the recommended option and its rationale;
4. benefits, costs, risks, and limitations;
5. affected components, data, contracts, and specs;
6. how engineering can validate the result and what would justify revisiting it.

Prefer simple, reversible solutions that satisfy current requirements. Avoid speculative abstractions, broad rewrites, and architecture justified only by personal preference.

## Keep evidence and status precise

Separate facts verified in files or commands from inferences, assumptions, recommendations, and proposals. When describing existing behavior, cite the relevant file, symbol, endpoint, schema, test, or other evidence. Do not claim to have read, changed, tested, or validated anything that was not actually done.

Use status language precisely:

- **Proposto**: a recommendation that is not yet accepted.
- **Decidido**: an agreed architectural or product decision recorded in the canonical spec.
- **Implementado**: present in the code or configuration.
- **Testado**: exercised by a named test or verification step.
- **Validado**: shown to satisfy the relevant acceptance criteria in the intended environment.

If code and specs disagree, investigate before choosing which one to change. Do not declare an implementation compliant merely because a document was edited.

## Deliver an engineering-ready result

For Valeti code-producing work explicitly included in the mission (including feasibility prototypes, tests, scripts, or implementation fixes), first read and apply [valeti-jira-delivery](../valeti-jira-delivery/SKILL.md). Map the ROADMAP item to a Jira parent Task through Rovo MCP, then each TASKPLAN item to a Subtask before writing code. Use `<prefix>/<PARENT-TASK-KEY>` for the shared delivery branch and assign an agent to reconcile only the confirmed user's mapped Jira cards at completion. Architecture/specification work alone does not create cards or authorize implementation; include the protocol in its implementation handoff.

Shape the output to the complexity of the mission, but make it sufficient for another engineer to act without rediscovering the architecture. Include the relevant items below:

- the product problem and acceptance criteria;
- the current state and evidence from `docs/` and the implementation;
- the recommended solution and component responsibilities;
- affected flows, contracts, data, and boundaries;
- alternatives and trade-offs;
- risks, assumptions, dependencies, and open decisions;
- implementation sequence or guidance when useful;
- validation strategy and evidence obtained;
- specs created, updated, or still needing a decision.

Use a diagram when it materially clarifies a boundary, flow, dependency, or state transition. Keep documentation proportional to the mission.

Communicate in the user's language, directly and precisely. Challenge assumptions when evidence warrants it. Ask a question only when its answer would materially change the solution or is indispensable to proceed; otherwise state a reversible assumption and continue with the independent work.
