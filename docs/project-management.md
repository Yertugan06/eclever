# Project management and risk register

**Pre-defense 1 target:** 24 October 2026. **Repository:** [Yertugan06/eclever](https://github.com/Yertugan06/eclever). **YouTrack:** [EClever issues](https://eclever.youtrack.cloud/issues/ECL). The live project key is `ECL`; all 15 planned tasks now have verified issue IDs in the ledger below. The [task worksheet](youtrack-tasks.csv) retains their source descriptions and planned assignments.

## People, milestones and task ledger

Yertugan Toktal owns AI engineering, frontend and technical evaluation; Ruslan Tsoy owns backend engineering. Yertugan supplied both students' full names; the supervisor's Latin spelling remains to be confirmed. The planned pre-defense document split is in the ledger. Each student authors and commits their own contributions under their own Git identity. The other student reviews the PR. The Supervisor, Aliya D. Katyetova, reviews substance at agreed checkpoints.

`Critical` means needed for the committee's minimum 24 October package; `Major` supports presentation/review. Dates are 2026. The 15 issue records and priorities were verified on 23 October 2026. The student names and deadlines are in issue descriptions because only the `admin` user exists and the project has no Due Date field. The seven earlier issues are assigned to `admin`; the eight newly created issues are unassigned. The table's student ownership is planned, not an actual YouTrack assignment or proof of completed work, commits, or PRs.

| Local ref | Priority / owner / due | Expected outcome | Acceptance criterion | Draft evidence |
|---|---|---|---|---|
| [T01 / ECL-27](https://eclever.youtrack.cloud/issue/ECL-27) | Critical / Ruslan / 10-23 | Repository overview | README includes problem, users, scope, team, stack, status and docs/YouTrack links. | [README](../README.md); review pending. |
| [T02 / ECL-20](https://eclever.youtrack.cloud/issue/ECL-20) | Critical / Yertugan / 10-22 | Initial requirements | FR/NFR priorities and acceptance criteria exist for every Must; each maps to a TP/EX. | [Requirements](requirements-specification.md); [PR #3](https://github.com/Yertugan06/eclever/pull/3) approved by collaborator `x4rd`. |
| [T03 / ECL-28](https://eclever.youtrack.cloud/issue/ECL-28) | Major / Ruslan / 10-24 | Frozen submission | Reviewed main commit has one annotated `pre-defense-1` tag; the submission note lists completed work, limitations and tasks, and the handoff records the resulting tag URL and SHA. | [Submission note](submissions/pre-defense-1.md); tag pending. |
| [T04 / ECL-21](https://eclever.youtrack.cloud/issue/ECL-21) | Critical / Yertugan / 10-22 | Project proposal | Title, people, problem, users, aim, six objectives, outcomes and scope tiers in one document. | [Proposal](proposal.md); [PR #2](https://github.com/Yertugan06/eclever/pull/2) approved by collaborator `x4rd`. |
| [T05 / ECL-29](https://eclever.youtrack.cloud/issue/ECL-29) | Critical / Ruslan / 10-23 | Draft component architecture | Nine modules, interfaces and data flows agree with source/export component diagram and ADR. | [Architecture](architecture.md), [diagram](diagrams/components.svg); owner review pending. |
| [T06 / ECL-30](https://eclever.youtrack.cloud/issue/ECL-30) | Critical / Ruslan / 10-22 | Management record | Milestones, ownership, dependencies, risks, mitigations and next steps are stated. | This document; owner review pending. |
| [T07 / ECL-22](https://eclever.youtrack.cloud/issue/ECL-22) | Critical / Yertugan / 10-21 | Repository structure | Checklist, glossary and ADR appear in reviewed commits without private material. | [Glossary](../GLOSSARY.md), [ADR](adr/0001-modular-monolith-schema-per-module.md); [PR #1](https://github.com/Yertugan06/eclever/pull/1) approved by collaborator `x4rd`. |
| [T08 / ECL-31](https://eclever.youtrack.cloud/issue/ECL-31) | Critical / Ruslan / 10-23 | Critical literature review | Original draft retained; at least 12 meaningfully analysed sources, eight scientific, and publication table. | [Literature review](literature-review.md); owner review pending. |
| [T09 / ECL-32](https://eclever.youtrack.cloud/issue/ECL-32) | Critical / Ruslan / 10-23 | Relevance evidence | Record 3–5 user-representative discussions or a substantive actual-client agreement; link findings to A1–A6 and resulting decisions. An exception requires written committee acceptance. | [Evidence status](relevance-evidence.md); pending. |
| [T10 / ECL-33](https://eclever.youtrack.cloud/issue/ECL-33) | Major / both; Yertugan coordinates / 10-23 | Supervisor feedback record | Actual review request, substantive comments, decisions and linked revisions are logged. | [Feedback log](supervisor-feedback.md); pending. |
| [T11 / ECL-23](https://eclever.youtrack.cloud/issue/ECL-23) | Critical / Yertugan / 10-23 | Evaluation protocol | Musts trace to test procedures; metrics, host conditions, datasets, baselines and limits stated. | [Verification plan](verification-evaluation-plan.md); [PR #5](https://github.com/Yertugan06/eclever/pull/5) approved by collaborator `x4rd`. |
| [T12 / ECL-24](https://eclever.youtrack.cloud/issue/ECL-24) | Critical / Yertugan / 10-23 | Context and use-case diagrams | Editable source and readable exports match actors, external systems and FRs. | [Context](diagrams/context.svg), [use cases](diagrams/use-cases.svg); [PR #6](https://github.com/Yertugan06/eclever/pull/6) approved by collaborator `x4rd`. |
| [T13 / ECL-34](https://eclever.youtrack.cloud/issue/ECL-34) | Critical / Ruslan / 10-22 | Technology rationale | At least three decisions compare 2–3 options against requirements and state choice/trade-off. | [Technology comparison](technology-comparison.md); owner review pending. |
| [T14 / ECL-25](https://eclever.youtrack.cloud/issue/ECL-25) | Critical / Yertugan / 10-23 | Key screen mockups | Student map, code/Predict Exercise and Teacher dashboard/roster scenarios are viewable. | [HTML prototype](prototype/key-screens.html); [PR #7](https://github.com/Yertugan06/eclever/pull/7) approved by collaborator `x4rd`. |
| [T15 / ECL-26](https://eclever.youtrack.cloud/issue/ECL-26) | Critical / Yertugan / 10-22 | Existing-system comparison | Five systems use the same nine criteria with source links and honest undocumented cells. | [Existing systems](existing-systems-comparison.md); [PR #4](https://github.com/Yertugan06/eclever/pull/4) approved by collaborator `x4rd`. |

**Snapshot status:** Yertugan's seven task PRs are merged into `main` at `e892d61` and have approval reviews from collaborator `x4rd`; the reviewer's student identity is not verified. Ruslan's seven documentation commits from `T01-T03-ruslan-pre-defense-docs` are included in the `prob-period-1` submission branch and tag without a verified PR review. The tag records the combined design package; it does not establish cross-student review or completion of the separate reviewed-main `pre-defense-1` milestone. The newer ECL issue links were reconciled for this snapshot.

Each issue has its priority, expected outcome and acceptance criterion; its planned owner and deadline are in the description. Once student accounts and a Due Date field exist, set the actual assignee and due date. Link each branch, commit/PR and final review. The issue is complete only when its criterion and links are present. Use the actual ID: branch `ECL-<number>-short-name`; commit `ECL-<number>: Imperative summary`; PR `ECL-<number>: Task name`, with *What changed / YouTrack / How checked*. Merge commits preserve individual authorship. A substantive reviewer comment and addressed revision should be visible. Never assign another student's name to a commit that they did not make.

| Milestone | Target | Exit condition |
|---|---|---|
| Pre-defense 1 | 24 Oct 2026 | Reviewed docs, diagrams, prototype, YouTrack evidence, supervisor feedback or explicit pending note, immutable tag. |
| Pre-defense 2 | University date TBD | Phase 1 core course/checking and Phase 2 adaptation demonstration, with tests. |
| Final pre-defense | University date TBD | Phase 3 Tutor, Phase 4 dashboards and technical evaluation report. |

Implementation responsibilities remain Ruslan for backend and sandbox; Yertugan for AI, frontend and evaluation; both review content mapping and Hint labels. Dates after 24 October will be added when the university publishes them.

## Dependencies and next steps

Proposal and relevance findings feed requirements; requirements feed diagrams, prototype and tests; the Skill Graph and content contract feed implementation; a Kazakhstan host able to run gVisor and a legally cleared LLM path precede use with real Students. CSEDM access and independent Skill mapping precede EX-1. School access, legal-representative consent and a separate protocol precede any pilot. Supervisor review time and Ruslan's accepted repository access precede a credible two-person reviewed submission.

1. Add Yertugan and Ruslan to the `ECL` project, assign their issues, and add a Due Date field so the dates in the [worksheet](youtrack-tasks.csv) can be set as structured values. Confirm the supervisor's spelling and any needed project access.
2. Have each student review the other's contributions, record substantive comments and revisions, link Ruslan's commits through a PR and connect the task and review links in YouTrack.
3. Seek supervisor review of proposal, requirements and technology comparison. Record actual comments and changed commit IDs.
4. Complete the [relevance-evidence plan](relevance-evidence.md) with 3–5 real discussions or an actual client agreement; record any committee-approved exception if that route is taken. Resolve the legal/hosting questions before any child data.
5. Merge the reviewed submission note, freeze main, create the annotated `pre-defense-1` tag once, and provide the repository/tag link and resulting SHA in the committee handoff.

## Risks

Likelihood and impact are planning judgements (L/M/H), not observed frequencies.

| ID | Risk (L/I) | Trigger, mitigation and owner |
|---|---|---|
| R1 | A1–A6 refuted (M/H) | Interviews disagree; update affected FRs and proposal. Ruslan/Yertugan. |
| R2 | No school access (H/M) | No interview/pilot permission; report technical evaluation only, seek external Teacher review. Ruslan. |
| R3 | Two-person capacity (H/H) | Deadlines slip; prioritise Critical minimum, reduce extensions, rebalance owner with explicit agreement. Both. |
| R4 | Thin individual commit/review evidence (H/H) | Missing owner PR/review; make real scoped contributions and link them before tag, never impersonate. Both. |
| R5 | LLM cap exhausted (M/M) | 80% monthly alert; use fallback, limit calls and budget experiments separately. Yertugan. |
| R6 | ZDR/provider access refused (M/H) | No approved terms for child data; keep only synthetic data, disable live tutor, assess in-country model. Yertugan. |
| R7 | Identifier slips into LLM prompt (M/H) | Seeded scrub test fails; block outgoing call and use fallback; audit pipeline. Yertugan. |
| R8 | Sandbox escape (M/H) | Hostile suite fails; disable Student code execution, fix isolation. Ruslan. |
| R9 | KZ host cannot run gVisor (M/H) | Deployment test fails; assess another KZ host or nsjail with stated limit. Ruslan. |
| R10 | CSEDM Skill mapping/data access delay (M/M) | Dataset inaccessible; complete synthetic evaluation and disclose missing external comparison. Both. |
| R11 | Hint gate or red Struggling label deters help (M/M) | Prototype/pilot feedback; revise wording or visibility. Yertugan. |
| R12 | Later dates unknown (H/L) | University publishes calendar; update milestone dates and YouTrack. Both. |
| R13 | Kazakh Hint quality inadequate (M/M) | Extension test fails; keep Kazakh outside Core. Yertugan. |
| R14 | Supervisor feedback absent before tag (H/H) | No response by 23 Oct; log requests and outstanding review honestly, address later. Both. |
