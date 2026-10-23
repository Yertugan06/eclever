# EClever

An adaptive, AI-assisted platform that teaches Python programming to students in grades 6–8 in Kazakhstan. It estimates how well each student has mastered each skill and uses that to choose what they practise next and how much help they get.

## People

**Student**:
A learner in grades 6–8 (about 11–14 years old) who solves exercises on the platform.
_Avoid_: User, pupil, learner (when the role is meant)

**Teacher**:
An informatics teacher who follows the progress of the students in their class.
_Avoid_: Instructor, tutor (reserved for the AI Tutor)

**Administrator**:
A member of the project team who creates Teacher accounts, publishes course content and exports anonymised research data.
_Avoid_: Admin user, superuser, content author

**Class**:
A group of Students that one Teacher creates and follows on the platform. The Teacher adds each Student to it; Students never register on their own. A Student belongs to exactly one Class; a Teacher may have many Classes.
_Avoid_: Group, course (a Course is the content, not the people)

**Consent Confirmation**:
A Teacher's recorded statement that the legal representatives of the Students in a Class have consented to their data being processed; the consent itself is collected outside the platform.
_Avoid_: Parental consent (that is the paper document, not the platform record)

## Curriculum

**Skill**:
One narrowly defined programming ability (e.g. writing a `for` loop over `range()`) whose mastery is tracked per student.
_Avoid_: Topic, concept, competency

**Skill Graph**:
The set of Skills together with their Prerequisite relationships.
_Avoid_: Knowledge graph, curriculum tree

**Prerequisite**:
A Skill a Student must have at least practised (one Independent Success) before Exercises of a dependent Skill open to them.

**Exercise**:
A programming task with a primary Skill, optional secondary Skills (earlier Skills it also needs), and a difficulty level (1–3). Write, Fix and Modify Exercises are checked with stdin/stdout Test Cases; Predict Exercises compare a typed output answer with the given program's output.
_Avoid_: Task, problem, assignment

**Predict Exercise**:
An Exercise where the Student reads a given program, types its expected output, then checks the prediction and sees the actual output. The answer is formative practice, not mastery evidence.

**Worked Example**:
A short, annotated program with labelled steps, shown when a Student starts a Skill. The Student may skip it or reopen it later. Viewing it is a Learning Event, not mastery evidence.

**Test Case**:
One input/expected-output check of a Write, Fix or Modify Exercise; it is either visible to the Student or hidden.

**Run**:
A check of a Student's code against an Exercise's visible Test Cases only; it gives feedback but is not evidence of mastery.
_Avoid_: Test run, attempt

**Submission**:
A Student's code sent with Submit and checked against all of a Write, Fix or Modify Exercise's Test Cases; it is the only kind of check that counts as evidence of mastery. A Submission whose code is identical to an earlier one on the same Exercise is a duplicate and adds no new evidence.
_Avoid_: Attempt (when the stored code + result is meant), Run (a Run is not a Submission)

## Knowledge and adaptation

**Mastery Probability**:
The Knowledge Estimator's numeric estimate (0–1) that a Student has mastered a Skill.
_Avoid_: Mastery, score, level

**Mastery Status**:
The pedagogical state of a Skill for a Student (NOT_STARTED, LEARNING, PRACTICING, MASTERED, REVIEW_DUE), decided by the Mastery Decision Policy from evidence. It is distinct from Mastery Probability.
_Avoid_: Progress, level

**Struggling**:
Said of a Student on a Skill when their last three Submissions on it all failed, or they reached the strongest Hint Level and still did not solve the Exercise.
_Avoid_: At risk, weak

**Independent Success**:
A Submission that passes all Test Cases when the Student used no Hint above L1 on that Exercise beforehand; a pass after a stronger Hint is an assisted success, not an Independent Success.

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

**Fallback Hint**:
A short hint written in advance for an Exercise, shown instead of an AI Tutor Hint when the AI Tutor's output is unavailable or rejected.
_Avoid_: Static hint, default hint

**Hint Level**:
How strong a Hint is: L1 guiding question, L2 conceptual hint, L3 local diagnosis, L4 step-by-step walkthrough of an analogous example.

**Leak**:
A Hint that gives away a working solution to the Student's current Exercise, judged by what its Hint Level allows (e.g. any stated fix at L1, an L4 example that also solves the current Exercise). A leaking Hint is never shown.
_Avoid_: Spoiler, giving the answer

**Safety Flag**:
A marker on a Submission or Hint whose content may be unsafe for a child, shown to that Class's Teacher and to the Administrator.
_Avoid_: Alert, report

**Learning Event**:
A timestamped record of something a Student did (submitted, requested a Hint, opened an Exercise) used for adaptation, dashboards and research.
