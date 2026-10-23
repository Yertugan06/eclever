# Initial requirements specification — pre-defense 1

**Version:** 2026-10-22 draft. These are intended system behaviors, not implemented features. `Must` is the Core release obligation, `Should` is a Core improvement that may slip, `Could` is contingent research extension, and `Won't` is outside this release. IDs remain stable. Sources are [proposal objectives O1–O6 and assumptions A1–A6](proposal.md), use cases in the [use-case diagram](diagrams/use-cases.svg), and the [architecture](architecture.md). `A` in the Basis column means the requirement rests partly on an unvalidated user assumption; `D` means a team design decision; `E` means curriculum, research or policy evidence. The verification IDs resolve to procedures in the [verification plan](verification-evaluation-plan.md).

## Functional requirements

Each criterion is a concrete Given/When/Then check; `G/W/T` abbreviates those words. A successful test must also preserve role-based access. The diagram and architecture group use cases by actor, while these IDs group requirements by owning component.

| ID | Requirement | Priority / basis | Acceptance criterion | Verification |
|---|---|---|---|---|
| FR-ACC-01 | Authenticate generated Student and Teacher credentials. | Must / D | G a valid account; W credentials are submitted; T a role-scoped session opens; wrong credentials fail. | TP-01 |
| FR-ACC-02 | Let a Teacher create Classes and add Students only after Consent Confirmation. | Must / A1,D | G a Teacher and no confirmation; W they add a Student; T rejected. G confirmation; W they add one; T a unique login card is generated without email. | TP-02 |
| FR-ACC-03 | Let a Teacher reset a Student password and remove that Student with their data. | Must / D | G a Student in their Class; W reset; T old login fails. W removal; T all module records for that Student are absent. | TP-02, TP-14 |
| FR-ACC-04 | Let a Teacher open course sections for their Class. | Must / A5 | G a closed section; W the Teacher opens it; T eligible Exercises become available only to that Class. | TP-03 |
| FR-CNT-01 | Publish a Python Skill Graph with Prerequisites and curriculum mapping. | Must / E,O1 | G authored content; W published; T ≥12 Skills map to an Order 399 objective; invalid cycles and missing references are rejected. | TP-03 |
| FR-CNT-02 | Supply at least five Exercises per Skill and three difficulty levels. | Must / D,O1 | G published course; W audited; T 60–80 Exercises overall and every Skill has Predict, Fix/Modify, Write, transfer and retention; both Fix and Modify exist; each code Exercise's reference passes all tests. | TP-03 |
| FR-CNT-03 | Show a short Worked Example when a Skill starts; allow skip and reopen. | Must / E | G a first visit; W Skill opens; T example appears, can be skipped/reopened, and viewing it does not change mastery. | TP-03 |
| FR-EXR-01 | Run visible stdin/stdout Test Cases and show input, expected and actual output. | Must / O2 | G a code Exercise; W Run; T only visible cases execute and result is shown, with no mastery observation. | TP-04 |
| FR-EXR-02 | Submit against all Test Cases while hiding hidden inputs and outputs. | Must / O2 | G a code Exercise; W Submit; T all cases execute; visible details and hidden failure count appear; hidden cases are never in the response. | TP-04 |
| FR-EXR-03 | Explain common Python errors in plain Russian beside the original error. | Must / A2 | G syntax, indentation, name, type, division or timeout error; W check completes; T both original and child-readable explanation appear. | TP-04 |
| FR-EXR-04 | Store Runs and Submissions, mark identical normalized code as duplicate, and exclude Runs/duplicates from evidence. | Must / D | G repeat code with changed comments/spacing; W Submit; T stored with duplicate marker and no second mastery observation. | TP-04, TP-05 |
| FR-EXR-05 | Check a Predict answer against the program's output. | Must / E | G a Predict Exercise; W Student enters output and checks; T actual output is shown and only a formative event is logged. | TP-04 |
| FR-KNW-01 | Update Mastery Probability from nonduplicate code Submissions on the primary Skill only. | Must / O3 | G fixed history; W Submit; T chosen rule-based or BKT estimator updates consistently; Predict and Run do not. | TP-05, EX-1 |
| FR-KNW-02 | Track Mastery Status separately from Probability. | Must / O4 | G a Skill; W first Exercise, independent successes and transfer occur; T status follows NOT_STARTED → LEARNING → PRACTICING → MASTERED only when each rule is met. | TP-05, EX-2 |
| FR-KNW-03 | Require two Independent Successes on distinct code Exercises, one at difficulty ≥2, estimator threshold, and a transfer pass within three Submissions for MASTERED. | Must / D | G all but one condition; W evaluated; T not MASTERED. G all; W evaluated; T MASTERED. | TP-05, EX-2 |
| FR-KNW-04 | Schedule reviews at 7 and 21 calendar days from MASTERED; handle a late first review and failure. | Must / E,D | G fake clock; W due date arrives or review passes/fails; T REVIEW_DUE, next review, or PRACTICING follows the [policy](architecture.md#main-flows). A first pass on/after day 21 satisfies both. | TP-05, EX-2 |
| FR-KNW-05 | Credit a successful cumulative Exercise to a due secondary-Skill review without updating that Skill's Probability. | Must / D | G review due within three days; W independent success on a tagged Exercise; T one review stage advances; primary Probability alone updates. | TP-05, EX-2 |
| FR-ADP-01 | Unlock a Skill only when every Prerequisite is at least PRACTICING and its section is open. | Must / O4,A5 | G unmet Prerequisite or closed section; W Continue or free choice; T blocked and missing prerequisite shown. | TP-06, EX-2 |
| FR-ADP-02 | Recommend due review, eligible transfer, next current-Skill practice, then next unlocked Skill, in that order. | Must / O4 | G one candidate of each kind; W Continue; T highest-priority eligible action opens; source `continue` is logged. | TP-06, EX-2 |
| FR-ADP-03 | Allow self-choice among eligible Exercises, and log choice source. | Must / A5 | G eligible Exercise; W Student chooses it; T it opens and source `self` is logged; ineligible one remains blocked. | TP-06 |
| FR-ADP-04 | Adjust difficulty one step after Independent Success or sustained difficulty, bounded 1–3. | Should / D | G difficulty 1–3; W success or L3+ / three failures; T next level changes by ±1 with no underflow/overflow. Rule remains a hypothesis for EX-2. | TP-06, EX-2 |
| FR-TUT-01 | Unlock the next Hint Level only after a new nonduplicate Run or Submission; stop after L4. | Must / O5 | G no attempt or no new attempt; W Hint requested; T refused. G new attempt; T next of L1–L4; after L4 offer Teacher help. | TP-07 |
| FR-TUT-02 | Show AI disclosure and record acknowledgement before the first Hint. | Must / E | G no acknowledgement; W first Hint requested; T disclosure precedes any provider call; declining makes no call. | TP-07, TP-12 |
| FR-TUT-03 | Send only minimised task/code context and level, with no hidden tests or identifying strings. | Must / E | G seeded names, usernames, Class names, email, phone and IIN in metadata/code; W Hint call; T none appears in captured outgoing payload; only hidden failure count is sent. | TP-12 |
| FR-TUT-04 | Validate structured Hint output, child safety and answer leakage before display; use the authored Fallback Hint on any failure. | Must / O5 | G malformed, unsafe, leaking, timed-out or quota-blocked output; W Hint completes; T no rejected text is shown; fallback appears and required Safety Flag is raised. | TP-07, TP-13, EX-3 |
| FR-TUT-05 | Record Hint level/outcome and push hint use to Knowledge Model. | Must / O4 | G an accepted or fallback Hint; W shown; T history records level/outcome and a later assisted pass does not count as Independent Success after L2+. | TP-07, TP-05 |
| FR-DSH-01 | Show a Student's Skill map, Mastery Status and next action. | Must / O6 | G seeded states including REVIEW_DUE; W Student opens map; T only own states and next action appear. | TP-08 |
| FR-DSH-02 | Show Teacher Class × Skill status, Struggling and Safety Flag markers. | Must / O6,A4 | G seeded Class; W its Teacher opens dashboard; T correct cells/markers appear; another Teacher is denied. | TP-08, TP-11 |
| FR-DSH-03 | Give Teacher read-only Student detail with Submissions and Hint history. | Must / A4 | G own Student; W detail opens; T code/results and Hint levels/times appear without edit/grade actions. | TP-08 |
| FR-SAF-01 | Flag unsafe Submission/Hints for the own-Class Teacher and Administrator and allow review. | Must / E | G seeded unsafe content; W check completes; T one flag is shown to authorised roles and can be marked reviewed. | TP-13 |
| FR-EVT-01 | Record timestamped starts, Runs, Submissions, Hints, mastery/review transitions and disclosure. | Must / O3,O4 | G each action; W performed; T typed event with source and timestamp is committed with the action and no duplicate event on retry. | TP-09 |
| FR-EVT-02 | Export research events with pseudonymous IDs and no names or login credentials. | Must / E | G seeded identities; W Administrator exports; T no direct identifiers appear and export schema is reproducible. | TP-12 |
| FR-ADM-01 | Allow Administrator CLI to create Teachers, publish content, inspect flags/status and export events. | Must / D | G authorised server operator; W each command; T expected outcome and audit log; unauthorised browser cannot invoke it. | TP-10 |
| FR-ADM-02 | Delete Student data on withdrawal across every module. | Must / E | G Student with history; W Teacher removes Student; T no Student row remains in any module schema and subsequent views deny access. | TP-14 |

## Non-functional requirements

| ID | Requirement | Priority / basis | Measurable acceptance criterion | Verification |
|---|---|---|---|---|
| NFR-SEC-01 | Enforce role and Class isolation on every API route. | Must / E | Cross-Class Teacher and cross-Student requests are denied; server-side queries never return another subject's data. | TP-11 |
| NFR-SEC-02 | Hash passwords using Argon2 or bcrypt; protect server secrets. | Must / D | No plaintext password in DB/log/export; hashes verify; secrets absent from repository and runner. | TP-11 |
| NFR-SEC-03 | Run Student code in one-use gVisor sandboxes with no network, read-only root except 10 MB `/tmp`, ≤128 MB memory, ≤32 processes, ≤2 s CPU/test, ≤10 s wall/check and ≤64 KB output. | Must / O2 | Every hostile-suite case is contained; next check succeeds and a child-readable limit message appears. | TP-15 |
| NFR-PRV-01 | Keep all personal-data storage in a database physically in Kazakhstan for a real-Student deployment. | Must / E | Host contract/configuration and deployment inspection show the DB location; no foreign replica/backup. Legal review before live use. | TP-12 |
| NFR-PRV-02 | Collect no Student email, birth date or IIN; require external legal-representative consent confirmation. | Must / E | Form/schema inspection and negative onboarding test. | TP-02, TP-12 |
| NFR-PRV-03 | Prevent personal data from reaching the external LLM; record residual-risk assessment. | Must / E | Captured requests for seeded identifiers contain none; failures fail closed to Fallback Hint. | TP-12 |
| NFR-PRV-04 | Delete Student records on withdrawal and exclude direct identifiers from research export. | Must / E | Cross-schema deletion and export audit pass. | TP-14, TP-12 |
| NFR-PRV-05 | Delete data within 12 months after Class closure. | Should / D | Clock-controlled retention job removes expired Student data. | TP-14 |
| NFR-SAF-01 | Screen every generated Hint before display and replace rejected content. | Must / E | 100% of LLM outputs pass Safety and leak checks; any blocked item yields Fallback Hint and Flag. | TP-13 |
| NFR-SAF-02 | Meet the fixed Hint quality and leak thresholds. | Must / O5 | Raw leaks ≤5% L1–L3, ≤10% L4; shown leaks 0%; shown correctness ≥80%, kappa ≥0.6 per criterion on the frozen EX-3 set. | EX-3 |
| NFR-PRF-01 | Return code results promptly on the target host. | Must / O2 | 30 simultaneous five-test Submits ×10 bursts: all results; median ≤3 s, p95 ≤6 s including wait. | TP-16 |
| NFR-PRF-02 | Return safe Hints promptly. | Must / O5 | On EX-3 server runs, median ≤8 s, p95 ≤15 s from request to displayed Hint, including checks and retry. | EX-3 |
| NFR-PRF-03 | Navigate major pages promptly. | Should / D | Page transition ≤2 s on demo host with 1280×720 desktop browser. | TP-08 |
| NFR-AVL-01 | Degrade without losing evidence when LLM or runner is unavailable/overloaded. | Must / D | LLM failure shows fallback while Run/Submit work; runner queue-cap or wait timeout shows busy and counts no Submission; recovery succeeds. | TP-17 |
| NFR-AVL-02 | Back up the database daily and verify restoration. | Should / D | Daily backup exists and a sampled restore reproduces row counts. | TP-17 |
| NFR-LOC-01 | Provide Russian UI, exercise and Hint text. | Must / A5 | Main Student and Teacher journeys have no untranslated controls; EX-3 checks Russian Hints. | TP-08, EX-3 |
| NFR-LOC-02 | Externalise UI strings for later Kazakh support. | Should / D | No hard-coded Student-facing copy outside locale resources. | TP-08 |
| NFR-USE-01 | Support current desktop Chrome, Edge and Firefox at ≥1280×720. | Must / A6 | Main journeys complete in all three browsers and viewport. | TP-08 |
| NFR-USE-02 | Meet WCAG 2.2 AA contrast and keyboard interaction on Student screens. | Should / E | axe scan has no serious/critical issues and keyboard journeys complete. | TP-08 |
| NFR-MNT-01 | Keep Knowledge Estimator and LLM provider behind swappable interfaces. | Must / O3 | Same contract tests pass for rule/BKT and real/fake gateway; import-linter rejects cross-module private imports. | TP-18 |
| NFR-CST-01 | Enforce a hard $10/month LLM spend cap and alert at 80%. | Must / D | Simulated cost at 80% emits warning; at cap no external generation call occurs and fallback appears. | TP-17 |
| NFR-CST-02 | Limit each Student to 30 Hints per day. | Should / D | Hint 31 uses fallback or a clear limit message without provider call; next day resets. | TP-07 |

## Requirements at risk

A1 affects Class workflow and the urgency of dashboards; A2 affects error wording and optional help; A4 affects dashboard usefulness; A5 affects Teacher control, Russian copy and self-choice; A6 affects the desktop-only design. A3 informs the project motivation but does not justify a mandatory feature on its own. Interviews may change these requirements. The 7/21-day timing, difficulty ±1 and BKT threshold are also design hypotheses, to be examined in EX-2. The Kazakhstan hosting decision and LLM provider terms require fresh review before any real-Student deployment; the storage rule is in [Law 94-V, Article 12(2)](https://old.adilet.zan.kz/rus/docs/Z1300000094).

## Deferred requirements and traceability

Could: fixed-path Class mode for a school pilot, Kazakh UI/Hints, Teacher Exercise authoring and usability study. Won't for this release: free-text chat, self-registration, student email, live streaming Hints, a durable queue, other programming languages, native mobile app, DKT, voice/CV/mascot and official grading. See [proposal scope](proposal.md#scope).

The FR prefixes map to the identically named components in [architecture](architecture.md): `ACC→Identity`, `CNT→Content`, `EXR→Submissions`, `KNW→Knowledge`, `ADP→Recommendation`, `TUT→Tutor/Gateway`, `DSH/EVT→Analytics`, `SAF→Safety`, `ADM→Admin CLI`. `NFR` IDs are cross-cutting. Every Must row names a TP or EX procedure above; those procedures define test data and conditions. The [use-case diagram](diagrams/use-cases.svg) includes the Student, Teacher and Administrator journeys represented here. Changes to a requirement should update its criterion, procedure and affected diagram together.
