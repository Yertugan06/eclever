# EClever

**Development of an AI-Based Adaptive and Personalized Learning Platform for Teaching Programming to Students in Grades 6–8**

EClever is a planned web platform for curriculum-aligned Python practice in Kazakhstan. A Student works through short Exercises, sees code-checking feedback and graduated AI Hints, and receives the next Exercise based on a per-Skill mastery estimate. A Teacher creates a Class, opens course sections and sees where Students need help. The platform complements informatics lessons; it does not replace a Teacher or assign official grades.

## Problem, users and intended outcomes

Kazakhstan's current informatics curriculum includes Python in grades 6–8, while classroom practice time is limited. The project will test the assumption that Teachers need more timely individual feedback and a per-Skill view of progress. Primary users are Students about 11–14 years old; Teachers are the second user group. Parents or legal representatives and schools are stakeholders for consent and deployment. See the [proposal](docs/proposal.md) for the evidence/assumption distinction.

The intended outcomes are a working Python practice platform, a curriculum-mapped Skill Graph and mastery policy, an adaptive engine comparing rule-based and BKT estimators, a guarded four-level AI Tutor, Teacher dashboards, and a technical evaluation report. A school study is optional; the technical evaluation alone will not establish improved learning.

## Team, scope and status

- **Yertugan Toktal:** AI engineering, frontend and evaluation.
- **Ruslan Tsoy:** backend engineering and code runner.
- **Supervisor:** Aliya D. Katyetova (Катьетова А.Д.; Latin spelling to confirm).

This repository is in the **pre-defense 1 design stage** as of 24 October 2026. It contains documents, diagrams and an interactive HTML mockup; there is **no runnable EClever application or automated test suite yet**. Document task ownership and review status are in [project management](docs/project-management.md).

The Core release covers a teacher-led Russian-language Python course, generated Student accounts, safe code checking, mastery estimation, adaptive recommendations, graduated checked Hints, dashboards and technical evaluation. A school pilot, Kazakh-language experience and Teacher Exercise authoring are contingent extensions. Voice, mascot, computer vision, DKT, generated Exercises and a durable runner queue are future work. See [scope tiers](docs/proposal.md#scope).

## Selected design and technology

The planned client is React + TypeScript with Monaco. The backend is a FastAPI modular monolith with nine bounded modules, one PostgreSQL database with a schema per module, and a separate Docker + gVisor Code Runner. The planned external LLM is accessed through a provider adapter with prompt scrubbing and output checks. These are decisions, **not deployed capabilities**; a Kazakhstan host and legal basis for real-child data still need to be confirmed. The [technology comparison](docs/technology-comparison.md) explains alternatives and trade-offs.

## Documentation and preview

| Deliverable | Link |
|---|---|
| Committee source checklist and working task list | [Checklist](docs/committee-checklist.md) · [Task list](docs/pre-defense-1-task-list.md) |
| Project proposal and relevance evidence | [Proposal](docs/proposal.md) · [Evidence status](docs/relevance-evidence.md) |
| Research | [Literature review](docs/literature-review.md) · [Existing systems](docs/existing-systems-comparison.md) · [Technology choices](docs/technology-comparison.md) |
| System design | [Requirements](docs/requirements-specification.md) · [Architecture](docs/architecture.md) · [ADR 0001](docs/adr/0001-modular-monolith-schema-per-module.md) |
| Diagrams | [Context](docs/diagrams/context.svg) · [Use cases](docs/diagrams/use-cases.svg) · [Components](docs/diagrams/components.svg) · [Editable sources](docs/diagrams/README.md) |
| Student and Teacher mockups | [Open the HTML prototype](docs/prototype/key-screens.html) — use its screen buttons; Exercise variant A is selected. |
| Evaluation and management | [Verification plan](docs/verification-evaluation-plan.md) · [Milestones/risks](docs/project-management.md) · [Supervisor feedback status](docs/supervisor-feedback.md) |
| Submission | [Pre-defense 1 record](docs/submissions/pre-defense-1.md) |
| Domain terms | [Glossary](GLOSSARY.md) |

**YouTrack:** [EClever issues](https://eclever.youtrack.cloud/issues/ECL). All 15 tasks in the [task ledger](docs/project-management.md#people-milestones-and-task-ledger) have verified `ECL-*` issue links, priorities, acceptance criteria, and planned owners and deadlines in their descriptions. The students do not yet have YouTrack accounts, so actual student assignment remains pending. The repository is [github.com/Yertugan06/eclever](https://github.com/Yertugan06/eclever).

## Repository and working with this draft

`docs/` holds the committee package, `docs/diagrams/` has editable JSON sources and standalone SVG exports, and `docs/prototype/` has a static interactive mockup. `approximate.md` is the earlier technical scope and [the original review draft](docs/research/original-literature-review.docx) is preserved. The prototype can be opened directly in a desktop browser; it uses example data and does not contact a backend. Regenerate diagrams with `python3 docs/diagrams/render.py` (Python standard library only). Application setup, execution and tests will be documented when implementation starts. No credentials or Student personal data belong in the repository.

The planned workflow is one branch per YouTrack task (`ECL-<number>-short-name`), a descriptive task-ID commit, and a PR reviewed by the other student. The current documentation snapshot is tagged [`prob-period-1`](https://github.com/Yertugan06/eclever/tree/prob-period-1); the [submission record](docs/submissions/pre-defense-1.md) distinguishes this snapshot from the pending reviewed `pre-defense-1` milestone.
