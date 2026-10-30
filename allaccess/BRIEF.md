# Team brief: ALL access in the CUnicorn pre-acceleration program

Read this before doing any task in this repo. It is the single source of truth for every subagent.

## The program and the tasks

CUnicorn Pre-Acceleration (CU, 2026), Georgian-language course. Source decks (read them if a task needs detail):
- `პრეზენტაციები-20261030T115705Z-1-001/მასალები-პრეზენტაციები/ Week 1/CUnicorn_Week1 (1).pdf`: problem to idea.
  Tasks: Problem Statement in one sentence ("[სეგმენტი] აწყდება [პრობლემა]-ს მაშინ, როცა [კონტექსტი]", no solution
  named), WHO/WHAT/WHEN/WHY, User/Buyer/Decision-maker/Beneficiary, JTBD, current alternatives, 30-minute workshop
  (1 pick a problem, 2 fit it in the formula, 3 customer + pain + current alternative, 4 three evidence questions,
  5 five possible solutions, 6 pick one + next validation steps), Desirability x Feasibility x Viability filter.
- `.../Week 2/Problem Solution Fit, CU.pdf`: THE MAIN GRADED ASSIGNMENT, file name `AllAccess_PSF.pdf`.
  Sections: 0 startup passport, 1 interviews (min 2 per team member, one card each: interviewer, respondent role/age/
  where found, last time the problem happened in their words, best quote, what surprised us, notes photo/audio
  timestamp), 2 six-frame comic of one real respondent's day (product must NOT appear, at least one real quote,
  name the interview #), 3 paper prototype + test with 3 segment testers (what built, task given, per tester: what
  they did / where stuck / quote, what we change), 4 poster/story with a single CTA + real test (prediction written
  BEFORE publishing, where and how long, views, actions, did the prediction hold), 5 Value Proposition Canvas before
  and after, three biggest surprises with sources, problem statement now, next step (continue / change segment /
  change problem / change solution, 2-3 sentences). Checklist at the end of that deck.
- `.../Week 2/Problem_Solution_Fit_v2.pdf`: the lecture. In-class: problem formula v2 ("[ვინ] როცა [სიტუაცია],
  ცდილობს [სამუშაო], მაგრამ [დაბრკოლება]. ახლა იყენებს [არსებულ გამოსავალს], რაც [რატომ არ არის საკმარისი]."),
  VP Canvas (job, 3 pains, 3 gains, our answer to each), devil's-advocate 7 critical questions scored 0/1/2
  (11-14 ready, 6-10 weak spots, 0-5 back to problem), riskiest assumption, XYZ hypothesis ("at least X% of Y will
  do Z"), experiment types (landing/smoke, explainer video, concierge, Wizard of Oz, fake door, pre-sale),
  earlyvangelist levels 1-5, evidence strength ladder, PSF checklist (6-7 of 7 = ready for MVP).
- `.../Week 3/CUnicorn_Week2_Customer_Discovery_Validation_GE.pptx` (plain-text extracts of ALL four decks are in
  `allaccess/_sources/*.txt`, read those instead of the binaries). Worksheets:
  Interview Guide (segment, research problem, core hypothesis, 5 open questions about past behaviour, questions we
  must NOT ask), Interview Notes (quote/fact, context, frequency/impact, current alternative, insight/new question),
  Assumption Map (risk x uncertainty quadrants), Customer Profile (5 pillars + fill-in sentence), Persona (research
  based), Validation Experiment (hypothesis, test, evidence, threshold, decision), Team Sprint (riskiest hypothesis,
  who, 5 questions or steps, what counts as evidence, next 7 days), 60-second team update (WHO / WHAT / HOW /
  EVIDENCE, not a pitch), Homework (min 5 interviews, 3 quotes or behavioural facts, 3 insights; bring updated
  segment, what was / was not confirmed, one new hypothesis or experiment, next step).

The per-startup folders under `დავალებები -20261030T115704Z-1-001/დავალებები /` are empty upload slots (other
teams: Glaince, KORPUS, PAIgo, Salu, SilkHire, TERRAMIND, Verax). Ours is `ALL Access`. Do not touch the others.

## The product: ALL access (repo codename AEGIS), allaccess.ge

One system for the doors AND the people behind them: cards, doors, schedules, attendance and leave, on the
controllers the company already has, every action audited. Georgian, English, Russian. Multi-tenant SaaS.
Honest capability facts (do not claim more):
- Access control: drives S4A/ACB controller panels end to end today. Dahua, Suprema, ZKTeco, Hikvision are planned.
  Give a person a door in one sheet; access groups; live feed with a "why denied" explanation; offboarding preview
  that revokes cards + login in one audited action; hash-chained audit log; visitors + muster roll-call PDF.
- Workforce: phone check-in in the browser PWA `/my` (single-device binding + Wi-Fi/IP allow-list, NO GPS),
  attendance today board graded against schedules, monthly attendance table, leave with balances, one approvals
  inbox, shifts/rotations/rosters, overtime report with premium rates, timesheet exports (CSV/XLSX), payroll API.
- Pricing (owner decision 2026-10-11): permanent Free plan (phone check-in, up to 10 employees, 0 doors, 5 CSV
  exports a month), 14-day trial, then a paid "Team" plan plus add-ons (access control per door, shifts, visitors,
  documents, API) and Enterprise by quote. GEL prices are not public ("Contact sales"). Hardware quoted per site.
- Customer segments the sales team already described (hypotheses, NOT validated): micro cafe/shop owners; office
  SMEs 20-100 staff (owner signs, HR/office manager uses daily); multi-site retail; construction/field crews;
  gym/school/clinic; enterprise facility managers.

## Our chosen focus for this course (manager decision)

Primary segment (narrow, testable): **HR or office managers at Tbilisi companies with 20-100 employees that already
have a door/fob system, who prepare the monthly timesheet for payroll.** Problem hypothesis: the door log and the
attendance spreadsheet do not talk, so every month they re-type or reconcile hours by hand, argue with staff about
late arrivals and missed punches, and are never sure a leaver's fob was switched off.
Secondary probe segment (for surprises and contrast): micro business owners (cafe, shop, workshop, under 10 staff)
who track hours from WhatsApp messages and a notebook.

Team members are unknown: use placeholders `[წევრი 1]`, `[წევრი 2]`, `[წევრი 3]` (3 members assumed, so 6
interviews = 2 each).

## Rules for every deliverable

1. Write deliverables in **Georgian** (the course language). Code, file names and this brief may be English.
2. **Never use the em dash character** anywhere. Use a colon, comma, parentheses, or a plain hyphen.
3. **Simulation honesty.** The course says quotes, photos and numbers without a real interview do not count. Every
   simulated item must carry a visible label `სიმულაცია` (simulation) and the README must tell the team which parts
   they must redo with real people before submitting. Never present a simulated quote or number as real.
4. Follow The Mom Test: past behaviour, specific last time, no pitching, ask for a commitment at the end.
5. Stay consistent with the product facts above; do not invent features (no GPS, no non-S4A hardware today).
6. Markdown for working docs. Visual deliverables as self-contained HTML (inline CSS/SVG, font stack
   `"Noto Sans Georgian", "Noto Serif Georgian", sans-serif`, these fonts are installed locally). PDF rendering uses
   Playwright Chromium (installed under ~/.cache/ms-playwright) or `/usr/bin/google-chrome --headless --print-to-pdf`.

## Layout

```
allaccess/
  BRIEF.md                 this file
  week1/                   problem statement + workshop + DFV filter
  week3/                   interview guide, assumption map, profile/persona, validation plan, sprint, 60s update, homework
  week2-psf/
    interviews/            01..06 simulated transcripts + cards (persona subagents)
    synthesis.md           patterns, surprises, VPC before/after, passport, problem statement now, next step
    comic/                 6-frame comic (HTML/SVG)
    prototype/             paper-style clickable prototype (HTML) + simulated usability test results in tests/
    poster/                poster/story with one CTA + simulated distribution test
    AllAccess_PSF.html/.pdf  the assembled submission
```
