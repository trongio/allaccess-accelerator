# ALL access · CUnicorn წინასააქსელერაციო პროგრამა

> **English summary.** This repo holds the ALL access team's work for the CUnicorn pre-acceleration program (CU, 2026), weeks 1-3: the week 1 problem statement, the graded Problem-Solution Fit assignment (`AllAccess_PSF.pdf`) and the week 3 customer discovery worksheets. Deliverables are in Georgian. **Important:** all interviews, usability tests and the poster audience test in this repo are AI simulations, labelled `სიმულაცია`. They are practice material, not evidence, and must be replaced with real interviews and tests before submission (see the checklist below). Open `index.html` to browse everything.

---

## რა არის ეს რეპო

ALL access-ის (allaccess.ge) გუნდის ნამუშევარი CUnicorn-ის წინასააქსელერაციო კურსისთვის, კვირები 1-3:

- **კვირა 1:** პრობლემიდან იდეამდე (Problem Statement, WHO/WHAT/WHEN/WHY, JTBD, workshop, DFV ფილტრი).
- **კვირა 2:** მთავარი შესაფასებელი დავალება, Problem-Solution Fit (`AllAccess_PSF.pdf`): ინტერვიუები, კომიქსი, ქაღალდის პროტოტიპი, პოსტერი, Value Proposition Canvas.
- **კვირა 3:** Customer Discovery და Validation: Interview Guide, Assumption Map, Customer Profile, Validation Experiment, 60-წამიანი განახლება, საშინაო დავალება.

გუნდის ერთიანი ბრიფი (სეგმენტი, პროდუქტის ფაქტები, წესები): [`allaccess/BRIEF.md`](allaccess/BRIEF.md).

## როგორ გავხსნათ ნავიგატორი

1. ორჯერ დააწკაპუნეთ `index.html`-ზე (იხსნება ბრაუზერში, სერვერი არ სჭირდება).
2. ახალი ფაილების დამატების შემდეგ მონაცემები განაახლეთ:
   ```bash
   python3 scripts/build-index.py
   ```
   სკრიპტი (მხოლოდ stdlib) სკანირებს `allaccess/**`-ს და კურსის მასალებს და წერს `site-data.js`-ს.
3. ინტერნეტი საჭიროა: Tailwind, Alpine და marked იტვირთება CDN-იდან (ფონტი Google Fonts-იდან).
4. იკონები მოდის ლოკალური `vendor/fontawesome` საქაღალდიდან (Font Awesome Pro, git-ში ჯერ არ არის ჩადებული). ამ საქაღალდის გარეშე იკონები არ გამოჩნდება.

## კურსის დავალებები და ფაილები

| კვირა | დავალება | ფაილი |
|---|---|---|
| 1 | Problem Statement, WHO/WHAT/WHEN/WHY, User/Buyer/Decision-maker/Beneficiary, JTBD, ალტერნატივები, 30-წუთიანი workshop, DFV ფილტრი | [`allaccess/week1/problem-statement.md`](allaccess/week1/problem-statement.md) |
| 2 (PSF) | 0. სტარტაპის პასპორტი | [`allaccess/week2-psf/synthesis.md`](allaccess/week2-psf/synthesis.md), ნაწილი 0 |
| 2 (PSF) | 1. ინტერვიუები (მინ. 2 თითო წევრზე, ბარათები) | [`allaccess/week2-psf/interviews/01.md`](allaccess/week2-psf/interviews/01.md) ... `06.md`, რეკრუტინგის გეგმა [`ROSTER.md`](allaccess/week2-psf/interviews/ROSTER.md) |
| 2 (PSF) | 2. 6-კადრიანი კომიქსი | [`allaccess/week2-psf/comic/index.html`](allaccess/week2-psf/comic/index.html), `comic/comic.png` |
| 2 (PSF) | 3. ქაღალდის პროტოტიპი | [`allaccess/week2-psf/prototype/index.html`](allaccess/week2-psf/prototype/index.html), [`prototype/README.md`](allaccess/week2-psf/prototype/README.md), `prototype/screens/` |
| 2 (PSF) | 3. პროტოტიპის ტესტი 3 ტესტერზე | `allaccess/week2-psf/tests/prototype-test.md` (შეჯამება), [`prototype-tester-1.md`](allaccess/week2-psf/tests/prototype-tester-1.md), [`-2.md`](allaccess/week2-psf/tests/prototype-tester-2.md), [`-3.md`](allaccess/week2-psf/tests/prototype-tester-3.md) + ეკრანის ანაბეჭდები |
| 2 (PSF) | 4. პოსტერი/სთორი ერთი CTA-ით + პროგნოზი | [`allaccess/week2-psf/poster/README.md`](allaccess/week2-psf/poster/README.md), `poster/index.html`, `post-1080x1350.png`, `story-1080x1920.png` |
| 2 (PSF) | 4. პოსტერის ტესტი | [`allaccess/week2-psf/tests/poster-test.md`](allaccess/week2-psf/tests/poster-test.md) |
| 2 (PSF) | 5. VPC ადრე/შემდეგ, 3 სიურპრიზი, პრობლემა ახლა, შემდეგი ნაბიჯი | [`allaccess/week2-psf/synthesis.md`](allaccess/week2-psf/synthesis.md), ნაწილები 3, 5, 6, 7 |
| 2 (ლექცია) | ფორმულა v2, ეშმაკის ადვოკატი (7 კითხვა), go/no-go ზღვრები | [`allaccess/week2-psf/synthesis.md`](allaccess/week2-psf/synthesis.md), ნაწილები 2, 4, 6 |
| 2 (PSF) | აწყობილი ჩასაბარებელი ფაილი | `allaccess/week2-psf/AllAccess_PSF.html`, `allaccess/week2-psf/AllAccess_PSF.pdf` |
| 3 | Interview Guide + Interview Notes შაბლონი | [`allaccess/week3/interview-guide.md`](allaccess/week3/interview-guide.md) |
| 3 | Assumption Map | [`allaccess/week3/assumption-map.md`](allaccess/week3/assumption-map.md) |
| 3 | Customer Profile + Persona | [`allaccess/week3/customer-profile.md`](allaccess/week3/customer-profile.md) |
| 3 | Team Sprint + Validation Experiment | [`allaccess/week3/validation-plan.md`](allaccess/week3/validation-plan.md) |
| 3 | 60-წამიანი გუნდური განახლება | [`allaccess/week3/team-update-60s.md`](allaccess/week3/team-update-60s.md) |
| 3 | საშინაო დავალება | [`allaccess/week3/homework.md`](allaccess/week3/homework.md) |

კურსის წყარო-სლაიდები: `პრეზენტაციები-20261030T115705Z-1-001/`; მათი ტექსტური ამონაწერები: `allaccess/_sources/*.txt`. ჩასაბარებელი საქაღალდე: `დავალებები -20261030T115704Z-1-001/დავალებები /ALL Access/` (სხვა გუნდების საქაღალდეებს არ ვეხებით).

## მთავარი შედეგი ჯერჯერობით (ყველაფერი სიმულაცია)

> **სიმულაცია.** ქვემოთ მოცემული მიგნებები ეფუძნება 6 სიმულირებულ ინტერვიუს, 3 სიმულირებულ ტესტერს და სიმულირებულ აუდიტორიის პანელს. ეს არის ჰიპოთეზები შემდეგი რეალური ინტერვიუებისთვის, არა მტკიცებულება.

- **თავდაპირველი ჰიპოთეზა (კვირა 1):** თბილისის 20-100 თანამშრომლიანი კომპანიების HR/ოფის-მენეჯერები, რომლებსაც უკვე აქვთ კარის სისტემა, ყოველთვე ხელით ათანხმებენ კარის ლოგს და ტაბელს.
- **რა აჩვენა სიმულირებულმა ინტერვიუებმა:** კარის ლოგი ტაბელის წყარო თითქმის არსად არის (არასანდოა, მხოლოდ ზოგ კარზეა, ან არავინ გადმოწერს); კარის ლოგის შეჯერება 2/6, რეალური ექსპორტი 0/6, ანუ კვირა 1-ის go/no-go ზღვარმა ვერ გაიარა. ნამდვილი ტკივილი ცვლებიან კომპანიებშია: გრაფიკი Excel-შია, ხოლო გაცვლები, ღამის ცვლა, ზეგანაკვეთური და შვებულება WhatsApp/Viber-სა და ქაღალდზე იფანტება, რაც თვეში 1-2 სამუშაო დღეს ჭამს. თანამშრომლები ტელეფონით check-in-ს ეწინააღმდეგებიან; ფულის commitment 0/6.
- **გადაწყვეტილება (pivot):** **ვცვლით პრობლემას** და ვავიწროებთ ფილტრს: „აქვს კარის სისტემა“ ნაცვლად „მუშაობს ცვლებით ან ცვალებადი საათებით“ (კლინიკა 24/7, საწყობი, call center). გადაწყვეტას ჯერ არ ვცვლით.
- **პრობლემის ფორმულირება ახლა:** ცვლებიანი კომპანიის HR/ადმინისტრაციის მენეჯერი, როცა თვის ბოლოს ტაბელს ხურავს, ცდილობს გაარკვიოს, ვინ რეალურად იმუშავა თითოეული ცვლა, მაგრამ გაცვლები და გამონაკლისები ჩატებსა და ქაღალდზეა მიმოფანტული. ახლა იყენებს Excel-ს და ჩატების ხელით გადაკითხვას, რაც 1-2 სამუშაო დღეს ჭამს და დავას ფაქტის გარეშე ტოვებს.
- **ეშმაკის ადვოკატი: 9/14** („სუსტი წერტილები გაქვთ“). პრობლემის მხარე ძლიერია, გადაწყვეტისა და ფულის მხარე სუსტი. MVP-სთვის მზად არ ვართ. ეს ქულაც სიმულაციაზეა: რეალური ინტერვიუების გარეშე ყველა ქულა 0 ან 1 იქნებოდა.
- **ყველაზე სარისკო ჰიპოთეზა (H-A16):** HR-ის მიერ ჩაწერილი გამონაკლისებიდან აწყობილი ტაბელი, თანამშრომლების check-in-ის გარეშე, საკმარისად სანდოა ბუღალტრისთვის. შემოწმების გეგმა: [`allaccess/week3/validation-plan.md`](allaccess/week3/validation-plan.md).

### allaccess.ge და ჩვენი მასალის შეუსაბამობები

დეტალურად: [`allaccess/_sources/allaccess-site.md`](allaccess/_sources/allaccess-site.md) (საიტი შემოწმდა 2026-10-30).
- საიტზე წერია „უფასო ტარიფი არ არსებობს“ და ჩანს საჯარო ფასები (Starter ₾49, Pro ₾149, Enterprise ₾499). ჩვენი მასალა მიჰყვება მფლობელის 2026-10-11 გადაწყვეტილებას (Free ტარიფი, ფასები „Contact sales“). საიტი ჯერ არ არის განახლებული.
- საიტი Dahua, Suprema, ZKTeco, Hikvision-ს მხარდაჭერილად ასახელებს, რეალურად დღეს მხოლოდ S4A/ACB მუშაობს. ჩვენს მასალაში დანარჩენი „დაგეგმილია“.
- საიტზე არ ჩანს ტაბელი, ცვლები, ტელეფონით check-in, ანუ ის ამბავი, რომელსაც პოსტერი ჰყვება. პოსტერის რეალურ ტესტამდე ფორმის ბმული უნდა გადიოდეს ცალკე landing გვერდზე (`allaccess/week2-psf/poster/index.html`), არა მთავარ საიტზე.

## რა უნდა გააკეთოს გუნდმა ჩაბარებამდე

კურსის წესით ციტატა, ფოტო ან რიცხვი რეალური ინტერვიუს გარეშე არ ჩაითვლება. ამ რეპოში ყველა ინტერვიუ, ტესტი და პანელი სიმულაციაა, ამიტომ ჩაბარებამდე:

- [ ] **მინიმუმ 6 რეალური ინტერვიუ** (2 თითო წევრზე), ახალ სეგმენტში (ცვლებიანი კომპანიები), კითხვარით [`interview-guide.md`](allaccess/week3/interview-guide.md). არა მეგობრები და ნათესავები.
- [ ] **ჩაანაცვლეთ ინტერვიუს ბარათები, ციტატები და ფოტოები** რეალურით (`interviews/01.md`...`06.md`, სინთეზი, საშინაო დავალება, პასპორტი); ჩანაწერის ფოტო/აუდიოს დროის ნიშნული ყოველ ბარათზე. გადაამოწმეთ, გაუძლებს თუ არა გადაწყვეტილება და პრობლემის ფორმულირება რეალურ მონაცემებს.
- [ ] **კომიქსი თავიდან ააწყვეთ** ერთი რეალური რესპონდენტის დღიდან, მისი რეალური ციტატით და ინტერვიუს ნომრით (პროდუქტი კადრში არ უნდა ჩანდეს).
- [ ] **პროტოტიპი გატესტეთ 3 რეალურ ადამიანზე** სეგმენტიდან (ინსტრუქცია: [`prototype/README.md`](allaccess/week2-psf/prototype/README.md)), გადაიღეთ ფოტოები, ჩაწერეთ რა გააკეთეს, სად გაჭედეს, ციტატა და რას ვცვლით.
- [ ] **პოსტერი გამოაქვეყნეთ 7 დღით**: QR ჩაანაცვლეთ რეალური ფორმის ბმულით, **პროგნოზი არ შეცვალოთ** (3%, ~300 ნახვაზე 9 ჯავშანი), შემდეგ ჩასვით რეალური რიცხვები (ნახვები, ქმედებები, ჯავშნები) [`poster-test.md`](allaccess/week2-psf/tests/poster-test.md)-ის ბოლო ცხრილში და დაწერეთ, გამართლდა თუ არა.
- [ ] **VPC-ის ფოტოები ადრე და შემდეგ** (ქაღალდზე ან დაფაზე დახატული).
- [ ] **შეავსეთ გუნდის წევრების სახელები** ყველგან, სადაც წერია `[წევრი 1]`, `[წევრი 2]`, `[წევრი 3]`.
- [ ] **ხელახლა დაარენდერეთ PDF** (`allaccess/week2-psf/AllAccess_PSF.html` → `AllAccess_PSF.pdf`), შეამოწმეთ, რომ ჩასაბარებელ ფაილში არცერთი სიმულირებული ელემენტი რეალურად არ არის წარმოდგენილი, და ატვირთეთ `დავალებები .../ALL Access/`-ში.

## როგორ შეიქმნა ეს მასალა

ეს მასალა მოამზადა Claude Code-მა: მენეჯერი აგენტი + AI ქვე-აგენტები. ქვე-აგენტებმა ითამაშეს გამოგონილი რესპონდენტები (6 ინტერვიუ), პროტოტიპის ტესტერები (3) და პოსტერის აუდიტორიის პანელი (24 გამოგონილი ადამიანი). ამიტომ ყველა ასეთი ელემენტი მონიშნულია როგორც `სიმულაცია`. მისი დანიშნულებაა კითხვარის, პროტოტიპისა და პოსტერის გაწვრთნა და ჰიპოთეზების დაზუსტება. **არცერთი სიმულირებული ციტატა, რიცხვი, ფოტო ან შედეგი არ შეიძლება ჩაბარდეს როგორც რეალური.**
