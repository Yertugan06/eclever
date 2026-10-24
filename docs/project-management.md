# Project management and risk register

**Pre-defense 1 target:** 24 October 2026. **Repository:** [Yertugan06/eclever](https://github.com/Yertugan06/eclever). **YouTrack:** [user-provided DEMO issue view](https://eclever.youtrack.cloud/issues/DEMO?preview=ESL-3). The team will use the existing `DEMO` project, per Yertugan's instruction. The `preview=ESL-3` URL parameter does not verify any DEMO task. The local task references below are **not YouTrack issue IDs**; live issue creation, membership, assignments and status are not verified. The [creation worksheet](youtrack-tasks.csv) carries the 15 proposed issue records.

## People, milestones and task ledger

Yertugan Toktal owns AI engineering, frontend and technical evaluation; Ruslan Tsoy owns backend engineering. Yertugan supplied both students' full names; the supervisor's Latin spelling remains to be confirmed. The planned pre-defense document split is in the ledger. Each student authors and commits their own contributions under their own Git identity. The other student reviews the PR. The Supervisor, Aliya D. Katyetova, reviews substance at agreed checkpoints.

`Critical` means needed for the committee's minimum 24 October package; `Major` supports presentation/review. Dates are 2026. These are **planned assignments**, not proof of completed YouTrack records, commits or PRs. YouTrack assigns the actual `DEMO-*` IDs when issues are created.

| Local ref | Priority / owner / due | Expected outcome | Acceptance criterion | Draft evidence |
|---|---|---|---|---|
| T01 | Critical / Ruslan / 10-23 | Repository overview | README includes problem, users, scope, team, stack, status and docs/YouTrack links. | [README](../README.md); review pending. |
| T02 | Critical / Yertugan / 10-22 | Initial requirements | FR/NFR priorities and acceptance criteria exist for every Must; each maps to a TP/EX. | [Requirements](requirements-specification.md); review pending. |
| T03 | Major / Ruslan / 10-24 | Frozen submission | Reviewed main commit has one annotated `pre-defense-1` tag; the submission note lists completed work, limitations and tasks, and the handoff records the resulting tag URL and SHA. | [Submission note](submissions/pre-defense-1.md); tag pending. |
| T04 | Critical / Yertugan / 10-22 | Project proposal | Title, people, problem, users, aim, six objectives, outcomes and scope tiers in one document. | [Proposal](proposal.md); review pending. |
| T05 | Critical / Ruslan / 10-23 | Draft component architecture | Nine modules, interfaces and data flows agree with source/export component diagram and ADR. | [Architecture](architecture.md), [diagram](diagrams/components.svg); owner review pending. |
| T06 | Critical / Ruslan / 10-22 | Management record | Milestones, ownership, dependencies, risks, mitigations and next steps are stated. | This document; owner review pending. |
| T07 | Critical / Yertugan / 10-21 | Repository structure | Checklist, glossary and ADR appear in reviewed commits without private material. | [Glossary](../GLOSSARY.md), [ADR](adr/0001-modular-monolith-schema-per-module.md); PR pending. |
| T08 | Critical / Ruslan / 10-23 | Critical literature review | Original draft retained; at least 12 meaningfully analysed sources, eight scientific, and publication table. | [Literature review](literature-review.md); owner review pending. |
| T09 | Critical / Ruslan / 10-23 | Relevance evidence | Record 3–5 user-representative discussions or a substantive actual-client agreement; link findings to A1–A6 and resulting decisions. An exception requires written committee acceptance. | [Evidence status](relevance-evidence.md); pending. |
| T10 | Major / both; Yertugan coordinates / 10-23 | Supervisor feedback record | Actual review request, substantive comments, decisions and linked revisions are logged. | [Feedback log](supervisor-feedback.md); pending. |
| T11 | Critical / Yertugan / 10-23 | Evaluation protocol | Musts trace to test procedures; metrics, host conditions, datasets, baselines and limits stated. | [Verification plan](verification-evaluation-plan.md); review pending. |
| T12 | Critical / Yertugan / 10-23 | Context and use-case diagrams | Editable source and readable exports match actors, external systems and FRs. | [Context](diagrams/context.svg), [use cases](diagrams/use-cases.svg); review pending. |
| T13 | Critical / Ruslan / 10-22 | Technology rationale | At least three decisions compare 2–3 options against requirements and state choice/trade-off. | [Technology comparison](technology-comparison.md); owner review pending. |
| T14 | Critical / Yertugan / 10-23 | Key screen mockups | Student map, code/Predict Exercise and Teacher dashboard/roster scenarios are viewable. | [HTML prototype](prototype/key-screens.html); review pending. |
| T15 | Critical / Yertugan / 10-22 | Existing-system comparison | Five systems use the same nine criteria with source links and honest undocumented cells. | [Existing systems](existing-systems-comparison.md); review pending. |

**Local draft status:** the temporary draft branch and its seven documentation commits were removed from branch history at Yertugan's request. `main` remains at the original baseline commit `387ad33`; the document package is uncommitted in the working tree. No task-linked contribution or cross-student review is claimed.

For each live YouTrack task, set owner, priority, due date, outcome and acceptance criterion from this table; link its branch, commit/PR and final review. The issue is complete only when its criterion and links are present. After issue creation, use the actual ID: branch `DEMO-<number>-short-name`; commit `DEMO-<number>: Imperative summary`; PR `DEMO-<number>: Task name`, with *What changed / YouTrack / How checked*. Merge commits preserve individual authorship. A substantive reviewer comment and addressed revision should be visible. Never assign another student's name to a commit that they did not make.

| Milestone | Target | Exit condition |
|---|---|---|
| Pre-defense 1 | 24 Oct 2026 | Reviewed docs, diagrams, prototype, YouTrack evidence, supervisor feedback or explicit pending note, immutable tag. |
| Pre-defense 2 | University date TBD | Phase 1 core course/checking and Phase 2 adaptation demonstration, with tests. |
| Final pre-defense | University date TBD | Phase 3 Tutor, Phase 4 dashboards and technical evaluation report. |

Implementation responsibilities remain Ruslan for backend and sandbox; Yertugan for AI, frontend and evaluation; both review content mapping and Hint labels. Dates after 24 October will be added when the university publishes them.

## Dependencies and next steps

Proposal and relevance findings feed requirements; requirements feed diagrams, prototype and tests; the Skill Graph and content contract feed implementation; a Kazakhstan host able to run gVisor and a legally cleared LLM path precede use with real Students. CSEDM access and independent Skill mapping precede EX-1. School access, legal-representative consent and a separate protocol precede any pilot. Supervisor review time and Ruslan's accepted repository access precede a credible two-person reviewed submission.

1. Confirm supervisor spelling and DEMO membership, create the 15 issues from the [worksheet](youtrack-tasks.csv), then populate their real links and verified assignments. The YouTrack API returned `Unauthorized` to an unauthenticated request on 22 October; the worksheet is preparation, not proof of issue creation.
2. Have each student review, revise, commit and link their assigned drafts through PRs. Preserve existing working-tree changes; do not backdate commits.
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
