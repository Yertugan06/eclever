# Modular monolith with one database schema per module

Status: accepted

EClever's backend is one FastAPI process made of nine modules (Identity & Classes, Course Content, Submissions, Knowledge Model, Adaptive Recommendation Engine, AI Tutor, LLM Gateway, Safety, Learning Analytics). Modules call each other in-process, and only through each module's public interface. They share one PostgreSQL database, but each module owns its own schema, and no module reads or writes another module's tables. An import-linter contract in CI enforces these boundaries. Only the Code Runner runs as a separate service, because it executes untrusted Student code. We chose this because a two-person team and a pilot-scale load do not justify microservices, while the strict boundaries keep the Knowledge Estimator and the LLM provider swappable and the architecture readable.

## Considered options

- **Microservices** (Kubernetes): independent deployment and scaling we do not need at pilot scale, at the cost of network calls, distributed transactions and operations work a two-person team cannot carry. Listed as out of scope.
- **Plain monolith with shared tables**: simplest to start, but any module could query any table, so swapping the Knowledge Estimator or deleting a Student's data would mean finding every place that touches those tables.

## Consequences

- Submit runs in one database transaction (store the Submission, update the knowledge state, record Learning Events), which a split into services would lose.
- Deleting a Student cannot rely on cross-module joins. Identity defines a `StudentDataOwner` interface, and every module holding Student data implements it.
- The module call graph must stay acyclic. Hint usage is therefore pushed from the AI Tutor to the Knowledge Model, rather than the Knowledge Model asking the Tutor.
- Splitting a module out into a service later means turning its interface into an API. The data does not need to be untangled first.
