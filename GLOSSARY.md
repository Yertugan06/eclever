# EClever

An adaptive, AI-assisted platform that teaches Python programming to students in grades 6–8 in Kazakhstan. It estimates how well each student has mastered each skill and uses that to choose what they practise next and how much help they get.

## People

**Student**:
A learner in grades 6–8 (about 11–14 years old) who solves exercises on the platform.
_Avoid_: User, pupil, learner (when the role is meant)

**Teacher**:
An informatics teacher who follows the progress of the students in their class.
_Avoid_: Instructor, tutor (reserved for the AI Tutor)

## Curriculum

**Skill**:
One narrowly defined programming ability (e.g. writing a `for` loop over `range()`) whose mastery is tracked per student.
_Avoid_: Topic, concept, competency

**Skill Graph**:
The set of Skills together with their Prerequisite relationships.
_Avoid_: Knowledge graph, curriculum tree

**Prerequisite**:
A Skill that must be mastered before another Skill is meaningfully practised.

**Exercise**:
A programming task with a primary Skill, a difficulty level (1–3), and Test Cases that decide whether a solution is correct.
_Avoid_: Task, problem, assignment

**Test Case**:
One input/expected-output check of an Exercise; it is either visible to the Student or hidden.

**Submission**:
One piece of code a Student sends to be checked against an Exercise's Test Cases.
_Avoid_: Attempt (when the stored code + result is meant)

## Knowledge and adaptation

**Mastery Probability**:
The Knowledge Estimator's numeric estimate (0–1) that a Student has mastered a Skill.
_Avoid_: Mastery, score, level

**Mastery Status**:
The pedagogical state of a Skill for a Student (NOT_STARTED, LEARNING, PRACTICING, MASTERED, REVIEW_DUE), decided by the Mastery Decision Policy from evidence. It is distinct from Mastery Probability.
_Avoid_: Progress, level

**Independent Success**:
A correct Submission that counts as evidence the Student solved the Exercise without substantial help.

**Transfer Assessment**:
A check of whether a Student can apply a Skill in an unfamiliar Exercise.

**Retention Assessment**:
A delayed check of whether a Student still holds a Skill they previously mastered.

**Knowledge Estimator**:
The component that produces Mastery Probability from a Student's history; it is either rule-based (the baseline) or BKT.

**Mastery Decision Policy**:
The pedagogical rules that turn evidence (Independent Successes, Transfer and Retention Assessments) into a Mastery Status.

**Adaptive Recommendation Engine**:
The component that chooses a Student's next Exercise, difficulty change, review, or offer of help.
_Avoid_: Recommender, adaptive engine (when the whole adaptation pipeline is meant)

## Help

**AI Tutor**:
The LLM-backed assistant that explains errors and gives Hints but never decides a Student's mastery.
_Avoid_: Chatbot, assistant

**Hint**:
One piece of help from the AI Tutor at a given Hint Level.

**Hint Level**:
How strong a Hint is: L1 guiding question, L2 conceptual hint, L3 local diagnosis, L4 step-by-step walkthrough of an analogous example.

**Learning Event**:
A timestamped record of something a Student did (submitted, requested a Hint, opened an Exercise) used for adaptation, dashboards and research.
