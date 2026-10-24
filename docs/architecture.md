# Initial architecture

EClever is a React + TypeScript web client, a FastAPI modular monolith, a separate Code Runner, and one PostgreSQL database hosted in Kazakhstan for any real Student data. The external LLM provider receives only minimised, scrubbed prompts. The [context](diagrams/context.svg), [use case](diagrams/use-cases.svg), and [component](diagrams/components.svg) diagrams show these boundaries. [ADR 0001](adr/0001-modular-monolith-schema-per-module.md) explains the modular monolith.

## Actors and boundaries

Students use a Teacher-generated login; Teachers own Classes and confirm externally collected consent before adding Students. An Administrator from the team uses a server-side CLI to create Teachers, publish course content and export pseudonymous research events. There is no self-registration, student email, free-text Tutor chat, or admin web UI in the first release. The Code Runner is inside the EClever system boundary but outside the backend process; the LLM provider is outside both. Parent/legal-representative consent is collected outside the product.

## Components and data ownership

| Component | Owns | Main interface |
|---|---|---|
| Identity & Classes | Accounts, roles, Classes, rosters, Consent Confirmations, opened sections, deletion | `Accounts`, `ClassAccess`, `StudentDataOwner` |
| Course Content | Sections, Skills, Prerequisites, Exercises, Test Cases, Worked Examples, Fallback Hints | `ContentReader`, `ContentPublisher` |
| Submissions | Run, Submit, result storage, duplicate checks, sandbox call | `CodeEvaluation`, `SubmissionHistory` |
| Knowledge Model | Rule-based/BKT estimator, Mastery Status and Struggling | `KnowledgeUpdates`, `KnowledgeReader` |
| Adaptive Recommendation Engine | Continue, unlock and difficulty policy | `Recommendations`, `ExerciseStart` |
| AI Tutor | Hint gating, prompt assembly, fallback, Hint records and daily cap | `HintService`, `HintHistory` |
| LLM Gateway | Provider adapter, prompt scrubbing, pseudonym, monthly cap | `Generate`, `Moderate` |
| Safety | Independent checks and Safety Flags | `SafetyCheck`, `Flags` |
| Learning Analytics | Learning Events, progress and dashboard views, export | `Events`, `Dashboard`, `Export` |

Each backend module owns a PostgreSQL schema and exposes its public interface; no cross-module table reads. Student-bearing modules implement `StudentDataOwner.delete_student(id)` and are called within one transaction on removal. Identity checks access to every Student and Class view. Analytics assembles dashboard data through interfaces and exports only pseudonymous Learning Events. The Code Runner gets code, stdin and limits only, with no expected outputs, names, database, credentials or network access.

## Main flows

1. **Exercise:** Recommendation checks opened sections and Prerequisites, records whether Continue or free choice started the Exercise, then the client shows a Worked Example or the Exercise. Predict is formative and logs a Learning Event only.
2. **Run:** Submissions calls the runner with visible Test Cases, returns visible expected/actual output and plain-Russian error explanations, and logs the Run. Run does not update mastery.
3. **Submit:** Submissions sends all tests to the runner. Hidden inputs stay server-side. It stores a nonduplicate Submission, updates primary-Skill evidence in Knowledge Model, then appends Learning Events in one transaction. Secondary-Skill review credit is handled by the Mastery Decision Policy. A background Safety check may flag Submission content after the response.
4. **Hint:** AI Tutor gates the next level after a new attempt. LLM Gateway removes identity strings and generic identifiers; Safety moderates the result. Submissions evaluates any proposed code as a leak test without storing evidence. A rejected or unavailable answer becomes the authored Fallback Hint. Only the checked Hint is displayed. The Tutor pushes Hint use to Knowledge Model.
5. **Teacher view:** Analytics reads authorised Class, Skill state, Submission and Hint histories, and Safety Flags. A Teacher can only see their own Classes.

All client calls are REST/JSON. Runner calls are synchronous internal HTTP with a bounded in-memory FIFO wait line and one-use gVisor sandboxes. The full Hint is validated before display, so no streaming. The Submission Safety check alone is asynchronous. A durable queue is future work. The runner waiting-line cap, maximum wait and pool size are set by the 30-Submit and 150-Submit tests. An overload response does not create mastery evidence. [Requirements](requirements-specification.md) and [verification plan](verification-evaluation-plan.md) define observable behavior.

## Unsettled implementation choices

The detailed Skill Graph, physical schema, scrubber rules, Kazakhstan host and final runner sizing remain design tasks. Their absence is recorded in [project management](project-management.md). Diagrams are a draft of the agreed boundaries, not evidence that components are built.
