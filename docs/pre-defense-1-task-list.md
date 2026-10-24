# Pre-defense 1 task list

Target: 24 October 2026. Source: [committee checklist](committee-checklist.md).

## 1. Project proposal

- [x] Turn the preliminary scope in [`approximate.md`](../approximate.md) into a [complete proposal](proposal.md).
- [x] State the project title, team members and their responsibilities, supervisor, problem statement, target users, aim, objectives, expected outcomes, and project scope in one document. The supervisor's Latin spelling still needs confirmation.
- [x] Distinguish the required first-stage scope from research extensions and optional features.

## 2. Relevance evidence

- [x] [Record what repository sources support and what remains an assumption](relevance-evidence.md); prepare a discussion guide and anonymised findings register.
- [ ] Record 3–5 actual user-representative discussions or a substantive agreement with the actual client, then revise affected requirements. An exception counts only if the committee explicitly accepts it.

## 3. Research and comparisons

- [x] Add the [original review](research/original-literature-review.docx) and a [critical synthesis](literature-review.md) relevant to EClever's approach.
- [x] The review analyses 20 scientific publications in a structured table; draft-only details are flagged for full-text verification before the final thesis.
- [x] Compare [five systems](existing-systems-comparison.md) against the same nine criteria, citing capability claims and marking undocumented features as such.
- [x] Document [six technology decisions](technology-comparison.md), each comparing alternatives against requirements, alongside the [architecture decision](adr/0001-modular-monolith-schema-per-module.md).

## 4. Requirements, architecture, and prototype

- [x] Write [functional and non-functional requirements](requirements-specification.md) with priorities and verifiable acceptance criteria for every mandatory requirement.
- [x] Create [context](diagrams/context.svg), [use case](diagrams/use-cases.svg), and [component](diagrams/components.svg) diagrams with [editable sources](diagrams/README.md) and readable exports.
- [ ] Commit the diagram sources and exports through the reviewed repository workflow.
- [x] Cross-check diagrams against the [requirements](requirements-specification.md), [scenarios and data flow](architecture.md); diagram sources and exports use the same node/edge definitions.
- [x] Add an [interactive HTML prototype](prototype/key-screens.html) for five Student and Teacher screens.

## 5. Verification and evaluation

- [x] Write a [testing plan](verification-evaluation-plan.md) covering the mandatory requirements and their acceptance criteria.
- [x] Define outcome metrics, conditions, data/participant assumptions, and baselines in that plan, building on the [preliminary evaluation notes](../approximate.md#8-evaluation-scope-для-диплома).
- [x] Explain how technical results demonstrate the project aim and what cannot be concluded without a Student study.

## 6. Project management, review, and repository submission

- [x] Add a complete [README](../README.md) with the requested project information and the known YouTrack workspace; the live task records are still pending verification.
- [x] Prepare the [15-task YouTrack creation worksheet](youtrack-tasks.csv) from the local ledger, with proposed owner, priority, due date, outcome and acceptance criterion for each item.
- [ ] Create and verify the assigned, prioritized tasks in the [existing DEMO YouTrack project](https://eclever.youtrack.cloud/issues/DEMO?preview=ESL-3), then replace the [local task references](project-management.md#people-milestones-and-task-ledger) with actual issue links.
- [x] Document [milestones, responsibilities, risks, dependencies, and next steps](project-management.md).
- [ ] Record substantive supervisor feedback on key deliverables and the decisions or revisions made in response.
- [ ] Record meaningful work in commits by each team member; link tasks to branches, commits or pull requests, and reviews.
- [ ] Before submission, commit the deliverables and create the `pre-defense-1` tag for the exact submitted version. Provide the repository link, tag, completed-work summary, known limitations, and outstanding tasks.
