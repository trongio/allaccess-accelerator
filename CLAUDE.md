# CLAUDE.md

## Purpose

Work of the ALL access team (allaccess.ge, repo codename AEGIS) for the CUnicorn pre-acceleration program (CU, 2026), weeks 1-3. The main graded deliverable is `allaccess/week2-psf/AllAccess_PSF.pdf` (Problem-Solution Fit). Read `allaccess/BRIEF.md` first: it is the single source of truth for tasks, segment, product facts and rules. Human-facing overview and pre-submission checklist: `README.md`.

## Hard rules

- Deliverables are written in **Georgian**. Code, file names and this file may be English.
- **Never use the em dash character**, anywhere. Use a colon, comma, parentheses or a plain hyphen.
- **Simulation honesty.** Every simulated item (interviews, quotes, numbers, testers, audience panels, photos) carries a visible `სიმულაცია` label and is never presented as real. The course does not accept quotes, photos or numbers without a real interview.
- **The Mom Test**: ask about past behaviour and the specific last time, no pitching, ask for a commitment at the end.
- **Product claims only from BRIEF facts.** Access control drives S4A/ACB panels only today (Dahua, Suprema, ZKTeco, Hikvision are planned). Phone check-in has **no GPS** (device binding + Wi-Fi/IP allow-list). There is **no employee shift swap-request feature**: HR edits the schedule. Do not invent features or prices.
- Do not touch other teams' folders under `დავალებები -20261030T115704Z-1-001/დავალებები /`. Ours is `ALL Access`.

## Layout

```
README.md                    Georgian overview, task-to-file table, pre-submission checklist
index.html + site-data.js    local navigator (site-data.js is generated)
scripts/build-index.py       builds site-data.js (stdlib only)
vendor/fontawesome/          Font Awesome Pro 7.3.1 (see below)
allaccess/
  BRIEF.md                   team brief, read first
  _sources/*.txt             plain-text extracts of all four course decks (read these, not the binaries)
  week1/problem-statement.md
  week2-psf/
    interviews/              ROSTER.md + 01..06 simulated interviews and cards
    synthesis.md             passport, patterns, go/no-go, VPC before/after, devil's advocate, decision, design brief
    comic/ prototype/ poster/
    tests/                   prototype-tester-1..3 (+ screenshots), prototype-test.md, poster-test.md
    AllAccess_PSF.html/.pdf  assembled submission
  week3/                     interview-guide, assumption-map, customer-profile, validation-plan, team-update-60s, homework
პრეზენტაციები-20261030T115705Z-1-001/   course source decks (PDF/PPTX)
დავალებები -20261030T115704Z-1-001/     per-team upload slots
```

## Workflow

- A manager session plus subagents worked well: persona subagents play interview respondents and prototype testers, a panel subagent plays the poster audience. Give each subagent `allaccess/BRIEF.md` as context.
- After adding or renaming files, run `python3 scripts/build-index.py` to refresh the navigator.
- Render PDFs and PNGs with Playwright Chromium launched with `--no-sandbox`. Fallbacks: `~/.cache/ms-playwright/chromium_headless_shell-1243` or `/usr/bin/google-chrome --headless --print-to-pdf`. Georgian fonts Noto Sans Georgian and Noto Serif Georgian are installed locally.
- The navigator needs internet for Tailwind, Alpine and marked CDNs.

## Font Awesome

Font Awesome Pro 7.3.1 lives in `vendor/fontawesome` (commercial license). It is committed to this private repo for the owner's personal use only (owner decision 2026-10-30). Never make the repo public or publish pages that bundle it.

## Product context

For ALL access facts beyond the brief, see the sibling repo `../aegis-gtm` (especially `docs/sales/demo-plans.md`). If it conflicts with `BRIEF.md` on what the product does today, follow the brief and ask.

## Current state and next steps

All evidence so far is simulated. Decision in `synthesis.md` section 7: change the problem (shift-based companies, schedule vs actually worked shift), devil's advocate 9/14. Next: the concierge experiment and real interviews in `allaccess/week3/validation-plan.md`, then the pre-submission checklist in `README.md`.
