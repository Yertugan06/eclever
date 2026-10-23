# EClever project proposal

**Title:** Development of an AI-Based Adaptive and Personalized Learning Platform for Teaching Programming to Students in Grades 6–8<br>
**Stage:** initial proposal for pre-defense 1, 24 October 2026<br>
**Team:** Yertugan Toktal (AI engineering and frontend) and Ruslan Tsoy (backend engineering). Document ownership is planned in [project management](project-management.md) and requires each student's own contribution.<br>
**Supervisor:** Aliya D. Katyetova (Катьетова А.Д.; spelling to confirm with her).

## Problem and evidence

Kazakhstan's current informatics curriculum names Python in grade 6 linear algorithms, grade 7 branching and files, and grade 8 loops and tracing. It allocates one informatics lesson per week, 34 per year; it does **not** specify how many lessons must be spent on Python. A proposed replacement curriculum may shift the Python start to grade 7, but its approval and rollout need confirmation. [Order 399, Appendix 55](https://zakon.uchet.kz/rus/docs/V2200029767); [draft curriculum](https://uba.edu.kz/storage/app/media/22%20QQ%20RS%20RS.pdf).

**Problem:** During limited classroom practice, a Teacher may not be able to identify each Student's difficulty and give timely, appropriately sized help. EClever proposes a teacher-led practice system that checks Python code, estimates mastery by Skill, recommends the next Exercise, and offers graduated AI Hints. The size of the classroom feedback gap is a **working assumption**, pending user-representative interviews; it is not presented as a measured local finding.

The [existing-system comparison](existing-systems-comparison.md) found documented pieces of this experience in other products, but no public evidence that one compared product combines knowledge-model-driven Python practice, graduated answer-withholding hints, a per-Skill Teacher view, and Kazakhstan curriculum alignment. This is a documentation finding, not proof that competitors lack undisclosed features. General-purpose LLM help can also reveal answers; the literature review and planned hint evaluation test that risk for EClever rather than assuming it is solved.

### Assumptions to validate

| ID | Working assumption | Planned check |
|---|---|---|
| A1 | A Teacher cannot respond individually to every Student during practice. | Teacher interviews or lesson observation. |
| A2 | A stuck Student may stop, copy, or avoid asking for help. | Student and Teacher interviews. |
| A3 | Students use general chatbots to obtain complete solutions. | Student and Teacher interviews. |
| A4 | Current class tools do not give the Teacher a useful per-Skill struggle view. | Teacher workflow walkthrough. |
| A5 | A Teacher would use curriculum-aligned Russian-language practice in class or for homework. | Teacher interview and prototype walkthrough. |
| A6 | Students have desktop browser access at school or home. | School access check. |

Interview findings and changes to requirements belong in [relevance evidence](relevance-evidence.md). No interviews are claimed yet.

## Users, aim and objectives

Primary users are Students aged approximately 11–14 in grades 6–8, starting with Russian-medium classes. Teachers create Classes, open course sections, and inspect progress. Parents or legal representatives and schools are stakeholders in consent and deployment. An Administrator from the project team provisions Teachers, publishes content, and exports anonymised research data. EClever complements lessons; it does not issue official school grades.

**Aim:** Develop and technically evaluate a web platform that complements school informatics lessons by teaching Python through per-Skill mastery estimation, adaptive selection of Exercises and reviews, and graduated AI Hints that do not reveal the current solution.

| Objective | Planned evidence of completion |
|---|---|
| O1. Build a curriculum-mapped course with at least 12 Skills and 60–80 authored Exercises at difficulties 1–3. | Skill-to-curriculum mapping; every code Exercise has tests and a passing reference solution. The five-Exercise minimum per Skill makes 60 the actual minimum. |
| O2. Check code in an isolated runner. | Hostile-code suite contained on gVisor; 30 simultaneous Submits all complete, median ≤ 3 s and p95 ≤ 6 s including waiting time. |
| O3. Implement rule-based and BKT Knowledge Estimators behind one interface. | Reproducible student-separated CSEDM 2019 and synthetic-data comparison with AUC, Brier, log loss and calibration; no predetermined winning model. |
| O4. Implement Mastery Decision Policy and recommendations. | Scenario tests for Prerequisites, transfer, 7/21-day reviews and Continue order; simulated false mastery ≤ 10% after threshold tuning. |
| O5. Implement four Hint Levels with child-safety and solution-leak checks. | 30 authored buggy cases, adversarial cases, two blinded raters; raw leak ≤ 5% at L1–L3, ≤ 10% at L4, displayed leak 0%, shown-Hint correctness ≥ 80%. |
| O6. Give Teachers a per-Student × per-Skill view. | Acceptance scenarios with seeded Class data, including Struggling and Safety Flags. |

The expected outputs are a working Student/Teacher web platform; a curriculum-aligned Skill Graph and pedagogical model; a rule-based/BKT adaptation engine and comparative report; an AI Tutor with guarded Hints; and a **technical evaluation report**. A study with Students is optional. Without one, the project will make no claim that EClever improves learning outcomes.

## Scope

| Tier | Included |
|---|---|
| **Core, required** | Teacher-created accounts and Classes; Russian UI; Python course; Worked Examples and Predict/Fix/Modify/Write Exercises; editor and sandboxed checking; Skill Graph; rule-based and BKT estimators; Mastery Decision Policy; recommendations and 7/21-day review; L1–L4 Hints with fallback and guardrails; Student progress and Teacher dashboard; Learning Events; technical evaluation. |
| **Research extension, contingent** | School pilot with pre/post and adaptive-vs-fixed-path comparison; Kazakh UI and Hints; Teacher Exercise authoring. |
| **Future work** | Self-study, English UI, generated Exercises, near-duplicate detection, BKT refitting on EClever logs, a durable runner job queue, a locally hosted LLM, mascot, voice, computer-vision engagement analysis, DKT. |
| **Out of scope** | Other programming languages, official grading or school-system integration, native mobile apps, Kubernetes microservices, an autonomously generated curriculum. |

The first course targets 12–16 Skills, at least five Exercises per Skill and 60–80 Exercises overall. One Skill has a Predict, a Fix or Modify, a Write, a transfer, and a retention Exercise; both Fix and Modify appear in the course. Content maps to Order 399 and records the grade placement proposed in the draft curriculum. The initial deployment is desktop first. Initial 7/21-day intervals, estimator thresholds and difficulty changes are hypotheses subject to the [evaluation plan](verification-evaluation-plan.md).

## Engineering substance and constraints

The core challenge is keeping a probability estimate separate from an evidence-based Mastery Status, then using it safely to choose the next action. A second challenge is validating LLM output before a child sees it. A third is securely running untrusted Python while keeping Submit responsive. These require defined module interfaces, privacy boundaries, repeatable tests, and explicit trade-offs. The architecture and technology choices are in [architecture](architecture.md) and [technology comparison](technology-comparison.md). For a real-Student deployment, [Kazakhstan’s personal-data law, Article 12(2)](https://old.adilet.zan.kz/rus/docs/Z1300000094) requires in-country storage of personal data; the host and any cross-border LLM processing still need legal and operational review.
