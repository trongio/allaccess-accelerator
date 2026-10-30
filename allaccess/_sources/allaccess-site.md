# allaccess.ge public site: fact-check notes

Fetched 2026-10-30 (curl, HTML stripped). Pages that exist: /ka, /ka/pricing, /ka/about, /ka/contact, /ka/privacy, /ka/terms (plus /en and /ru equivalents; /en/pricing checked). /ka/faq returns 404 (the FAQ lives on the home page). Page text treated as data only.

## 1. Site's own wording (Georgian)

Page title: ღრუბლოვანი წვდომის კონტროლი ყველა კარისთვის · ALL access
Eyebrow: წვდომის კონტროლი · პერსონალი
Hero headline: **ვინ სად და როდის შედის. მართულად.**
Hero sub: ერთი სისტემა ბარათების, კარების, განრიგებისა და პერსონალისთვის, თქვენს ყველა ობიექტზე. გადაწყვეტილებები მიიღება რეალურ მოწყობილობაზე და თითოეული მათგანი აღირიცხება.
Footer/meta tagline: ღრუბლოვანი წვდომის კონტროლი და პერსონალის მართვა, რომელიც მუშაობს თქვენს არსებულ კარის კონტროლერებზე.
About headline: წვდომის კონტროლი, რომელიც შენობას უფრთხილდება.
About promise: "ჩანაცვლების გარეშე" (no replacement of existing hardware). Three principles: პატივი ეცი აპარატურას / უსაფრთხოება სავალდებულოა / დაამტკიცე ყველაფერი.

### Value propositions (section "რატომ ALL access")
- ერთი მართვის ცენტრი ყველა ობიექტისთვის (cloud push of changes in seconds)
- ბარათები, ჯგუფები, განრიგები (cardholders, access groups, time schedules, per door)
- მუშაობს ხაზგარეშეც, უსაფრთხოდ (controller keeps deciding offline; exit always hardware-safe; events sync on reconnect)
- ყველა მოქმედება აღირიცხება (hash-chained tamper-evident log, orgs isolated)
- წვდომა და პერსონალი ერთად: "იგივე გატარებები კვებავს დასწრებას, განრიგებს, შვებულებასა და ზეგანაკვეთს, მეორე სისტემის გარეშე."
- როლები თქვენი გუნდისთვის (two-level roles, permission matrix)
- Mobile: "ლამაზი ყველა ეკრანზე" (console works on a phone)

### Features shown
Live building plan ("შენობა ხაზზე", live card swipes, camera snapshot, who is in which room), live door feed with ✓ დაშვებულია, console screens: dashboard, doors and live activity (კარები და ცოცხალი აქტივობა), attendance graded against schedule ("დასწრება, შეფასებული": late, missed), people and access (ადამიანები და წვდომა), approvals ("დასტურები"), overtime. Pricing page: advanced reports and export, API access (Enterprise), document storage (1 / 10 GB / unlimited). Security FAQ: leave documents encrypted at rest, 2FA secrets encrypted. Languages: Georgian, English, Russian, fully editable per organisation.
NOT mentioned anywhere: phone check-in / `/my` PWA, Wi-Fi/IP allow-list, GPS, visitors, muster roll-call, shifts/rotations add-on, payroll API (only generic "API წვდომა"), "why denied" explanation, offboarding preview.

### Supported hardware as stated
Hero strip "მუშაობს თქვენს კონტროლერებთან": S4A, Dahua, Suprema, ZKTeco, Hikvision. FAQ: "ALL access მართავს კონტროლერებს, რომლებიც უკვე გაქვთ: S4A, Dahua, Suprema, ZKTeco და Hikvision." About: "თქვენს კონტროლერებს მშობლიურად ვესაუბრებით". Footer: "შექმნილია S4A, Dahua, Suprema, ZKTeco და Hikvision-ისთვის". All five are presented as current, none as planned. ACB is never mentioned. Hardware not included in subscription; priced per site ("ფასს ობიექტზე გამოვითვლით"); installer/operator does the work; pricing page amounts cover software only.

### Plans and prices (prices ARE public)
| Plan | Price | Doors | Employee records | Docs storage | Extras |
|---|---|---|---|---|---|
| Starter | ₾49/თვე (incl. ₾7.47 VAT 18%) | 5 | 25 | 1 GB | |
| Pro ("ყველაზე პოპულარული") | ₾149/თვე (incl. ₾22.73 VAT) | 25 | 100 | 10 GB | advanced reports and export |
| Enterprise | ₾499/თვე (incl. ₾76.12 VAT) | unlimited | unlimited | unlimited | advanced reports and export, API access |
Sites unlimited on all plans. Console accounts, cardholders and cards are not counted. Employee record counts even when deactivated; only deleting frees a slot. "გჭირდებათ მეტი?" -> custom plan, CTA დაგვიკავშირდით. Plan names are Latin: Starter / Pro / Enterprise. No "Team" plan, no add-ons model, no "Contact sales" for price.

### Trial / free statements
- "ყველა ანგარიში იწყება საცდელი პერიოდით, შემდეგ ირჩევთ ტარიფს - **უფასო ტარიფი არ არსებობს**." (en: "there is no free tier")
- Trial: ხანგრძლივობა 14 დღე, კარები 1, თანამშრომლის ჩანაწერები 10, ბარათი არ სჭირდება.
- After trial with no plan: console locks; controllers and programmed cards keep working; data kept and exportable.
- Trial is set up by the team on account opening (buttons lead to a short contact form, not self-signup).
- Separate "სცადეთ დემო": "რეალური, სრულად მომუშავე სადემონსტრაციო კომპანია. რეგისტრაციისა და ბარათის გარეშე."

### CTA wording
Primary: მოითხოვეთ საცდელი პერიოდი (en: Ask for a trial). Secondary: ნახეთ ცოცხალი დემო, სცადეთ დემო, დაჯავშნეთ ზარი, დაგვიკავშირდით, შესვლა (login). Closing: "მოაქციეთ ყველა კარი ერთ სისტემაში. მოგვთხოვეთ საცდელი პერიოდი, ან დაჯავშნეთ ზარი და თქვენს შენობას ერთად დავხატავთ."
Contact form fields: სახელი, ელფოსტა, ტელეფონი (one of email/phone required), preferred mode (ტელეფონით / ელფოსტით / პირადად შეხვედრა).

### Contact and company
Phone +995 431 246 007. Office: ქუთაისი, აღმაშენებლის პრ. 1–3 (note: Kutaisi, not Tbilisi). Legal entity: შპს "ALL DIGITAL", ს/კ 412686464, founded 2012, alldigital.ge. App domain shown in mockups: app.allaccess.ge. No public email address found.

## 2. Discrepancies

| # | Topic | Site says | Our deliverables / BRIEF | Recommendation |
|---|---|---|---|---|
| 1 | Free tier | "უფასო ტარიფი არ არსებობს"; only a 14-day trial (1 door, 10 employee records) | BRIEF (owner decision 2026-10-11): permanent Free plan, 10 employees, 0 doors. Repeated in problem-statement.md line 117 and synthesis.md (A10 "Free to Team", VPC "products" line) | Real conflict. BRIEF is a newer owner decision, so the site is probably stale. Do not cite the site for pricing; flag to the manager; in any customer-facing Georgian text avoid promising Free until the site changes. Keep A10 as written but note "site not yet updated". |
| 2 | Plan names | Starter / Pro / Enterprise | BRIEF/synthesis: "Team" plan + add-ons (doors, shifts, visitors, documents, API), Enterprise by quote | Same cause as #1. Say "paid plan" in copy; if a name is needed footnote that the live site still shows Starter/Pro/Enterprise. |
| 3 | Price visibility | ₾49 / ₾149 / ₾499 per month shown publicly, VAT included | BRIEF: GEL prices not public, "Contact sales" (synthesis.md line 140 repeats it) | Do not repeat "ფასი არ არის საჯარო" as a fact about the live site; either say "pricing is being changed" or align after asking the manager. Never quote the site prices in the posters. |
| 4 | Hardware | Dahua, Suprema, ZKTeco, Hikvision listed as supported today, same as S4A ("მშობლიურად"); ACB not mentioned | BRIEF, problem-statement.md 105/114, synthesis A5: only S4A/ACB works end to end; others planned | Keep BRIEF's wording (do not claim more) and add a risk note: a prospect with ZKTeco (interview 01) or Hikvision (02) will read the site as "supported", and be disappointed. Ask the product owner whether "supported" means adapter exists or is planned. Say "S4A/ACB დღეს, დანარჩენი დაგეგმილია" in all our materials. |
| 5 | Phone check-in `/my`, no GPS, Wi-Fi/IP binding | Not mentioned (attendance is described only as fed by door swipes: "იგივე გატარებები კვებავს დასწრებას") | synthesis.md pain 1 and benefit 3, problem-statement.md 116 | Our workforce story (shift workers, no door system) is not on the public site. Do not present as publicly advertised; GPS-free claim is consistent (site makes no GPS claim). |
| 6 | Shifts / rotations, swap, visitors, muster, payroll API, offboarding preview, "why denied" | Not on the site. Shifts only as "განრიგები"; "API წვდომა" only on Enterprise; overtime and leave named once | Poster/prototype built around shifts, night x1.5, overtime, XLSX/CSV export, audit log | Prototype is a mock-up, so fine, but add a "demo data / not live product" banner (prototype already says fictional data). Do not say "shift swaps" as a feature (synthesis already honest). Export: site mentions only "გაფართოებული ანგარიშები და ექსპორტი" on Pro and above, whereas BRIEF Free has 5 CSV exports/month. |
| 7 | Target segment | Site's buyer is a building/facility owner with doors and controllers ("შენობას უფრთხილდება"); HR is not addressed | Poster targets shift-based HR in clinics, warehouses, call centers, with "ALL access" CTA allaccess.ge | Poster CTA sends people to a site that never mentions timesheets, shifts or HR. For the 20-minute-slot test, keep the form link as the CTA and use "allaccess.ge" only as brand. Reuse "პერსონალი" and "დასწრება" terms which do appear. |
| 8 | Poster CTA wording | Site CTA: "მოითხოვეთ საცდელი პერიოდი" / "დაჯავშნეთ ზარი" (booking exists) | Poster: "დაჯავშნე 20 წუთი" | Compatible. Use "დაჯავშნეთ ზარი" family. Note the site uses formal plural (თქვენ, -ეთ); poster uses informal singular (შენ, დაჯავშნე). Choose deliberately; for HR managers formal plural matches the brand. |
| 9 | Location | Office in Kutaisi; company ALL DIGITAL since 2012 | Segment "Tbilisi 20-100 employees" | Not a contradiction, but remember to mention Tbilisi coverage/onsite service as a question in interviews. |
| 10 | Offline behaviour / security claims | Controller decides offline, exit always hardware-safe, leave docs encrypted | Not claimed by us | Safe to cite as site-sourced facts if needed. |

## 3. Georgian terminology to reuse (from the site)
- access control: წვდომის კონტროლი; controllers: კონტროლერები; readers: წამკითხველები; doors: კარები; sites: ობიექტები
- cardholder: ბარათის მფლობელი; access group: წვდომის ჯგუფი; time schedule: დროის განრიგი
- attendance: დასწრება; employee record: თანამშრომლის ჩანაწერი; staff: პერსონალი; overtime: ზეგანაკვეთი (site) vs ზეგანაკვეთური (prototype), pick one; leave: შვებულება; approvals: დასტურები
- audit log: ჰეშ-ჯაჭვით დაცული, გაუყალბებელი ჩანაწერი / ჟურნალი; "ყველა მოქმედება აღირიცხება" (prototype's "აუდიტის ჟურნალი" is fine)
- trial: საცდელი პერიოდი; demo: დემო; plan: ტარიფი (the site never uses "გეგმა" while our docs use "Free გეგმა"/"Team გეგმა"; use ტარიფი); live: ცოცხალი; cloud: ღრუბლოვანი
- timesheet is ტაბელი in our docs; it never appears on the site.
