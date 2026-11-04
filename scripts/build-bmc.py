#!/usr/bin/env python3
"""Build the week 4 Business Model Canvas (HTML + Markdown) from one data set. Stdlib only.

Output: allaccess/week4/AllAccess_BMC.html and allaccess/week4/business-model-canvas.md
PDF: chromium --headless --no-sandbox --print-to-pdf (see CLAUDE.md).
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "allaccess" / "week4"

SEGMENTS = {
    "a": "A: ცვლებიანი სერვისის ბიზნესი (ფოკუსი)",
    "b": "B: კომპანიები S4A/ACB პანელებით",
    "c": "C: მიკრო ბიზნესი",
    "g": "საერთო",
}
TAG_FACT = "ფაქტი"
TAG_HYP = "ჰიპოთეზა"
TAG_TODO = "შესავსები"

# Each note: (segment, text, source). Source is an interview code, TAG_FACT, TAG_HYP or TAG_TODO.
BLOCKS = {
    "kp": ("8", "ძირითადი პარტნიორები", [
        ("g", "S4A/ACB კონტროლერების მომწოდებლები: დღეს მხოლოდ ამ აპარატურას ვმართავთ ბოლომდე", TAG_FACT),
        ("b", "ინსტალატორები და გადამყიდველები: მონტაჟი ობიექტზე; საოპერატორო კონსოლი მათზეა აწყობილი", TAG_FACT),
        ("b", "Suprema, Dahua, Hikvision, ZKTeco: დაგეგმილი ინტეგრაცია, დღეს არ მუშაობს (R01-ს სწორედ ეს აპარატურა აქვს)", "R01"),
        ("a", "ბუღალტრები: ტაბელს ისინი იღებენ, შეიძლება გაგვაცნონ კლიენტები", TAG_HYP),
        ("a", "სასტუმროებისა და რესტორნების ასოციაციები: ერთი კონტაქტით ბევრ ბიზნესამდე მისვლა", TAG_HYP),
        ("g", "ღრუბლოვანი ინფრასტრუქტურის მომწოდებელი", TAG_FACT),
    ]),
    "ka": ("7", "ძირითადი აქტივობები", [
        ("g", "პროდუქტის განვითარება: დასწრება, ცვლები, კარები, აუდიტი", TAG_FACT),
        ("a", "Concierge: ფურცლის ფოტოდან ტაბელის ხელით აწყობა, ახალი კოდის გარეშე", "გეგმა"),
        ("g", "პირდაპირი გაყიდვა მფლობელთან და ჩართვა ობიექტზე", TAG_FACT),
        ("b", "ახალი კონტროლერების დრაივერები, მოთხოვნის მიხედვით", TAG_FACT),
        ("g", "მხარდაჭერა ქართულად, ინგლისურად, რუსულად", TAG_FACT),
    ]),
    "kr": ("6", "ძირითადი რესურსები", [
        ("g", "ინტელექტუალური: SaaS პლატფორმა, S4A/ACB დრაივერი, ჰეშ-ჯაჭვით დაცული ჟურნალი", TAG_FACT),
        ("g", "ადამიანური: დეველოპერები, გაყიდვები, აპარატურის ცოდნა", TAG_FACT),
        ("g", "ბრენდი: ALL access, შპს ALL DIGITAL (2012 წლიდან), ოფისი ქუთაისში", TAG_FACT),
        ("g", "მონაცემი: 4 რეალური ინტერვიუ, ხელფასების ანონიმური ფაილი", "R01-R04"),
        ("g", "ფინანსური: ბიუჯეტი და runway", TAG_TODO),
    ]),
    "vp": ("1", "შეთავაზებული ფასეულობა", [
        ("a", "ქაღალდის ფურცლის ნაცვლად ყოველდღიური ჩანაწერი: check-in ტელეფონით (ერთი მოწყობილობა + Wi-Fi/IP, GPS-ის გარეშე)", TAG_FACT),
        ("a", "დავისას პასუხი ჩანაწერშია: აღარ გჭირდებათ 1-2 საათი კამერის გადახვევაზე თითო შემთხვევაში", "R03"),
        ("a", "გრაფიკი და რეალურად ნამუშევარი ერთ დაფაზე; შეცვლილი ცვლა ხელმძღვანელი გრაფიკში ასწორებს და ცვლილება აღირიცხება", "R01, R02, R03"),
        ("a", "ტაბელი ბუღალტრისთვის (XLSX/CSV, ზეგანაკვეთური პრემიით): ფურცლიდან Excel-ში გადატანის გარეშე", "R03"),
        ("a", "მონაცემები ღრუბელშია: არ არის დამოკიდებული ერთ დისკზე", "R03"),
        ("b", "კარები და ადამიანები ერთ სისტემაში, არსებული S4A/ACB პანელების შეცვლის გარეშე: წვდომა ერთ ფურცელზე, „რატომ უარყო“, ბარათი + ანგარიში ერთ მოქმედებაში ითიშება", TAG_FACT),
        ("c", "უფასო ტელეფონით დასწრება 10 თანამშრომლამდე, WhatsApp-ისა და რვეულის ნაცვლად", TAG_HYP),
    ]),
    "cr": ("4", "ურთიერთობა მომხმარებელთან", [
        ("a", "თანაშექმნა: 2 ხელმძღვანელთან concierge, შედეგს ერთად ვაუმჯობესებთ", "გეგმა"),
        ("g", "პირადი მომსახურება: ზარი, ჩართვა, 14-დღიანი საცდელი პერიოდი", TAG_FACT),
        ("c", "Self-service: უფასო ტარიფი დამოუკიდებელი რეგისტრაციით (დაგეგმილია)", TAG_FACT),
        ("a", "მფლობელთან ხელმძღვანელი თავად აჩვენებს შედეგს: მფლობელი ტკივილს დღეს ვერ ხედავს", "R03"),
    ]),
    "ch": ("3", "არხები", [
        ("a", "ინფორმაცია: პირადი გაცნობა, პირდაპირი მიმართვა სასტუმროებსა და რესტორნებს", "R01-R04"),
        ("g", "ინფორმაცია: allaccess.ge, ცოცხალი დემო (ტაბელს საიტი ჯერ არ ახსენებს)", TAG_FACT),
        ("g", "გაყიდვა: პირდაპირ მფლობელთან ან GM-თან; გადაწყვეტა: ყოველკვირეული შეხვედრა, ბორდი", "R01, R02"),
        ("g", "მიწოდება: ბრაუზერი და ტელეფონის PWA", TAG_FACT),
        ("b", "მიწოდება: აპარატურა ინსტალატორით", TAG_FACT),
    ]),
    "cs": ("2", "მომხმარებელთა სეგმენტები", [
        ("a", "A. 20-100 თანამშრომლიანი სერვისის ბიზნესი, ცვლებით და საათობრივი/დღიური ანაზღაურებით (სასტუმრო, რესტორანი, კაზინო), თბილისის გარეთაც", "R01, R03"),
        ("a", "მომხმარებელი: დეპარტამენტის ხელმძღვანელი. მყიდველი: მფლობელი ან GM", "R01, R03"),
        ("b", "B. კომპანიები, რომლებსაც უკვე აქვთ S4A/ACB პანელები", TAG_HYP),
        ("c", "C. მიკრო ბიზნესი, 10 კაცამდე (კაფე, მაღაზია)", TAG_HYP),
        ("g", "არ ვემიზნებით: ფიქსირებული ხელფასის ოფისებს და 300+ ორგანიზაციებს საკუთარი სისტემით", "R02, R04"),
    ]),
    "co": ("9", "ხარჯების სტრუქტურა", [
        ("g", "პოლიტიკა ახლა: ხარჯის შემცირებაზე ორიენტირებული. ახალ კოდს ვწერთ მხოლოდ გადახდის სიგნალის შემდეგ", "გადაწყვეტა"),
        ("g", "მუდმივი: გუნდის ხელფასები, ღრუბლოვანი ინფრასტრუქტურა, ოფისი", TAG_TODO),
        ("g", "ცვლადი: გაყიდვა და ჩართვა ობიექტზე, მხარდაჭერა, concierge-ის საათები, ახალი დრაივერები", TAG_TODO),
        ("c", "უფასო ტარიფი: ინფრასტრუქტურა და მხარდაჭერა შემოსავლის გარეშე", TAG_FACT),
        ("b", "აპარატურა გამოწერაში არ შედის: ფასი ობიექტზე ითვლება", TAG_FACT),
    ]),
    "re": ("5", "შემოსავლის წყაროები", [
        ("g", "გამოწერა (Subscription): ფასიანი ტარიფი თვიურად", TAG_FACT),
        ("g", "Upsell: დამატებები (კარი, ცვლები, სტუმრები, დოკუმენტები, API); Enterprise ინდივიდუალურად", TAG_FACT),
        ("a", "გზა ფასიანზე: უფასოდ ერთი დეპარტამენტი (R03-ში დასუფთავება 7 კაცია), გადახდა 10 კაცის გადაცილებისას ან როცა ცვლები სჭირდებათ", TAG_HYP),
        ("b", "ერთჯერადი: აპარატურა და მონტაჟი, ობიექტის მიხედვით", TAG_FACT),
        ("a", "ღია კითხვა: გადახდა ამ სეგმენტში არ დასტურდება. R03-ის მფლობელებმა ბარათის სისტემაზე თქვეს „არ გვაქვს ფული“; R02-ის ~35 000 ₾ მოსწავლეების ამოცანაზეა", "R02, R03"),
    ]),
}

LOGIC = (
    "ხელმძღვანელი იწყებს ერთ დეპარტამენტში, ფურცელს ტელეფონით ანაცვლებს და დავას ჩანაწერით აგვარებს. "
    "როცა ეს მთელ ბიზნესს სჭირდება, მფლობელი გამოწერას იხდის; კარები მოგვიანებით ემატება დამატების სახით."
)

RISKS = [
    ("1. მფლობელი გადაიხდის?",
     "R03: „არ გვაქვს ფული“; R02: ბიუჯეტი სხვა ამოცანაზეა; R01: არავის უცდია",
     "Pre-sale: concierge-ის ბოლოს მფლობელს ვთხოვთ ფასიან პირველ თვეს (Zappos: ვზომავთ გაყიდვას, არა ინტერესს)",
     "2 მფლობელიდან მინიმუმ 1 იხდის ან ხელს აწერს",
     "ვცვლით სეგმენტს ან შემოსავლის მოდელს"),
    ("2. ხელმძღვანელი ხარჯავს კვირაში 1 სთ-ზე მეტს (H-B1)",
     "ხელმძღვანელთან ჯერ არ გვისაუბრია; GM-ის დონეზე <1 სთ თვეში (R03)",
     "Concierge: ფურცლის ფოტო ყოველ საღამოს, 2 კვირა",
     "14-დან მინიმუმ 10 ფოტო შეხსენების გარეშე; 1 ხელმძღვანელი იყენებს ჩვენს XLSX-ს",
     "ვამოწმებთ, არის თუ არა ღირებულება მხოლოდ დავისას"),
    ("3. ცვლის პერსონალი ტელეფონით დარეგისტრირდება?",
     "რეალური მტკიცებულება: 0",
     "1 დეპარტამენტი, რეალური /my, 2 კვირა, ფურცელთან პარალელურად",
     "ცვლების მინიმუმ 80%-ს აქვს check-in, შეხსენების გარეშე",
     "ჩანაწერს ხელმძღვანელი აკეთებს, ან მხოლოდ კარებით"),
    ("4. არხი: სეგმენტამდე მისვლა შეგვიძლია?",
     "4 რესპონდენტიდან 1 დაგვთანხმდა გაცნობაზე (R02), 1 „ჰკითხავს“ (R01)",
     "20 პირდაპირი მიმართვა სასტუმროებსა და რესტორნებს",
     "მინიმუმ 3 შეხვედრა ხელმძღვანელთან ან მფლობელთან",
     "ვცდით ბუღალტრებს, ასოციაციებს, ინსტალატორებს"),
]

INNOVATION = [
    ("შემოსავალი", "ერთჯერადი დიდი შესყიდვა (R02: ~35 000 ₾) ან საერთოდ არაფერი (R03)",
     "უფასო დასაწყისი, შემდეგ გამოწერა და დამატებები", "Free/ფასიანი საფეხურები (სლაიდები 37, 56)"),
    ("არხი", "ყიდვა ზემოდან იწყება და მფლობელთან ჩერდება (R03)",
     "ქვემოდან: ერთი ხელმძღვანელი, ერთი დეპარტამენტი, შემდეგ მფლობელი", "ინოვაცია არხებში (სლაიდები 51-53)"),
    ("რესურსი", "ახალი სისტემა ნიშნავს აპარატურის შეცვლას (R01: „ძალიან ძვირია“)",
     "დასწრებას კარი არ სჭირდება; კარები არსებულ S4A/ACB პანელებზე მუშაობს", "რესურსის გარეშე მოდელი (Airbnb: 0 property, სლაიდი 58)"),
]

CONFLICTS = [
    "**უფასო ტარიფი და ფასები:** BRIEF და `demo-plans.md`: მუდმივი უფასო ტარიფი და დამალული ფასები. საიტი დღეს: „უფასო ტარიფი არ არსებობს“, Starter/Pro/Enterprise საჯარო ფასებით (ცვლილება დაგეგმილია, #841-#843). კანვასი BRIEF-ს მიჰყვება და თანხებს არ ასახელებს.",
    "**ტარიფის სახელი:** BRIEF წერს „Team“, `demo-plans.md` და საიტი: Starter/Pro/Enterprise. აქ წერია „ფასიანი ტარიფი“.",
    "**აპარატურა:** საიტი Dahua, Suprema, ZKTeco, Hikvision-ს მხარდაჭერილად ასახელებს; რეალურად მუშაობს მხოლოდ S4A/ACB.",
    "**უცნობია, გუნდმა შეავსოს:** თანხები ხარჯებში, runway, ამჟამინდელი გადამხდელი კლიენტები, პარტნიორებთან რეალური შეთანხმებები.",
]

HONESTY = (
    "კანვასი ეყრდნობა 4 რეალურ ინტერვიუს (R01-R04, 2026-10-31, ციტატები პარაფრაზია), მათგან პირველადი მტკიცებულებაა მხოლოდ R03. "
    "Week 2-ის სიმულირებული მასალა აქ არ გამოყენებულა."
)


def tag_class(src: str) -> str:
    return {TAG_HYP: "hyp", TAG_TODO: "todo", TAG_FACT: "fact"}.get(src, "ev")


def notes_html(key: str) -> str:
    num, title, notes = BLOCKS[key]
    items = "".join(
        f'<li class="n s-{seg} t-{tag_class(src)}">{escape(text)} <span class="tag">{escape(src)}</span></li>'
        for seg, text, src in notes
    )
    return f'<section class="b {key}"><h2><i>{num}</i>{escape(title)}</h2><ul>{items}</ul></section>'


def rows(data) -> str:
    return "".join("<tr>" + "".join(f"<td>{escape(c)}</td>" for c in r) + "</tr>" for r in data)


def bold(s: str) -> str:
    out, on = "", False
    for part in escape(s).split("**"):
        out += (f"<b>{part}</b>" if on else part)
        on = not on
    return out.replace("`", "")


CSS = """
@page{size:420mm 297mm;margin:0}
*{box-sizing:border-box}
:root{--ink:#17212b;--mut:#5d6b78;--line:#17212b;--a:#0f766e;--b:#b45309;--c:#6d28d9;--g:#64748b;--paper:#fff}
html,body{margin:0;background:#e9edf0;color:var(--ink);font-family:"Noto Sans Georgian","Noto Serif Georgian",sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:420mm;height:297mm;padding:10mm 11mm;background:var(--paper);margin:0 auto;display:flex;flex-direction:column;overflow:hidden;page-break-after:always}
.page:last-child{page-break-after:auto}
header{display:flex;justify-content:space-between;align-items:flex-end;gap:10mm;margin-bottom:4mm}
h1{font-size:25pt;margin:0;line-height:1.1;font-weight:800}
.sub{font-size:11pt;color:var(--mut);margin-top:1mm}
.meta{display:flex;gap:6mm;font-size:9.5pt;color:var(--mut);white-space:nowrap}
.meta b{display:block;color:var(--ink);font-size:10.5pt}
.grid{flex:1;min-height:0;display:grid;grid-template-columns:repeat(10,minmax(0,1fr));grid-template-rows:minmax(0,1fr) auto;border:1.2mm solid var(--line)}
.stack{display:flex;flex-direction:column;min-height:0}.stack .b{flex:0 0 auto}.stack .b:last-child{flex:1 1 auto}
.b{padding:2.2mm 2.4mm;border:.25mm solid var(--line);min-height:0;overflow:hidden}
.kp{grid-column:1/3}.s1{grid-column:3/5}
.vp{grid-column:5/7;background:#f6faf9}.s2{grid-column:7/9}
.cs{grid-column:9/11}.co{grid-column:1/6}.re{grid-column:6/11}
.co ul,.re ul{columns:2;column-gap:3mm}.co li,.re li{break-inside:avoid}
h2{font-size:12pt;margin:0 0 1.6mm;display:flex;align-items:center;gap:1.8mm;font-weight:700;line-height:1.15}
h2 i{font-style:normal;flex:none;width:6mm;height:6mm;border-radius:50%;background:var(--ink);color:#fff;font-size:9.5pt;display:flex;align-items:center;justify-content:center}
ul{list-style:none;margin:0;padding:0}
.n{font-size:9.8pt;line-height:1.28;padding:1mm 1.6mm;margin-bottom:1.25mm;border:.3mm solid #cbd5dc;border-left:1.3mm solid var(--g);border-radius:.8mm;background:#fff}
.s-a{border-left-color:var(--a)}.s-b{border-left-color:var(--b)}.s-c{border-left-color:var(--c)}
.t-hyp,.t-todo{border-style:dashed;border-left-style:solid;background:#fafafa}
.tag{display:inline-block;font-size:7.8pt;line-height:1.2;font-weight:600;padding:.15mm 1mm;border-radius:.7mm;white-space:nowrap;vertical-align:.2mm;background:#e8edf1;color:#334155}
.t-ev .tag{background:var(--ink);color:#fff}
.t-hyp .tag{background:#fff;border:.25mm dashed #475569;color:#334155}
.t-todo .tag{background:#fef3c7;color:#854d0e}
footer{display:flex;justify-content:space-between;gap:8mm;align-items:center;margin-top:3mm;font-size:9pt;color:var(--mut)}
.lg{display:flex;gap:4mm;flex-wrap:wrap;align-items:center}
.lg span.k{display:inline-flex;align-items:center;gap:1mm;white-space:nowrap}
.sw{width:3mm;height:3mm;display:inline-block;border-radius:.5mm}
.logic{font-size:14pt;line-height:1.4;font-weight:600;margin:0 0 6mm;padding:4mm 5mm;background:#f0f7f6;border-left:1.6mm solid var(--a)}
h3{font-size:14pt;margin:0 0 2.5mm}
table{width:100%;border-collapse:collapse;font-size:10.5pt;line-height:1.35;margin-bottom:6mm}
th{text-align:left;font-weight:700;border-bottom:.5mm solid var(--ink);padding:1.5mm 2mm;vertical-align:bottom}
td{border-bottom:.2mm solid #cbd5dc;padding:1.8mm 2mm;vertical-align:top}
td:first-child{font-weight:600}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:9mm}
.con{margin:0;padding-left:4.5mm;font-size:10.5pt;line-height:1.4}.con li{margin-bottom:1.6mm}
.hon{font-size:10.5pt;line-height:1.4;margin:0}
@media screen{.page{margin:6mm auto;box-shadow:0 1px 8px rgba(0,0,0,.2)}}
"""


def build_html() -> str:
    n = notes_html
    canvas = (n("kp") + f'<div class="stack s1">{n("ka")}{n("kr")}</div>' + n("vp")
              + f'<div class="stack s2">{n("cr")}{n("ch")}</div>' + n("cs") + n("co") + n("re"))
    conflicts = "".join(f"<li>{bold(c)}</li>" for c in CONFLICTS)
    return f"""<!doctype html>
<html lang="ka"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ALL access BMC</title><style>{CSS}</style></head><body>
<div class="page">
<header><div><h1>ბიზნეს მოდელის კანვასი: ALL access</h1>
<div class="sub">ერთი სისტემა ცვლების, დასწრებისა და კარებისთვის. ვერსია 1: ჰიპოთეზები, არა დამტკიცებული მოდელი.</div></div>
<div class="meta"><div>გუნდი<b>ALL access</b></div><div>პროგრამა<b>CUnicorn, კვირა 4</b></div><div>თარიღი<b>2026-11-04</b></div><div>ვერსია<b>v1</b></div></div></header>
<div class="grid">{canvas}</div>
<footer><div class="lg">
<span class="k"><i class="sw" style="background:var(--a)"></i>A: ცვლებიანი სერვისი (ფოკუსი)</span>
<span class="k"><i class="sw" style="background:var(--b)"></i>B: S4A/ACB პანელები</span>
<span class="k"><i class="sw" style="background:var(--c)"></i>C: მიკრო ბიზნესი</span>
<span class="k"><i class="sw" style="background:var(--g)"></i>საერთო</span>
<span class="k">R01-R04: რეალური ინტერვიუ</span><span class="k">ფაქტი: პროდუქტი დღეს</span><span class="k">ჰიპოთეზა: არ შემოწმებულა</span>
</div><div style="white-space:nowrap">BMC: Strategyzer, CC BY-SA</div></footer>
</div>
<div class="page">
<header><div><h1>რას ამოწმებს ეს კანვასი</h1><div class="sub">მოდელის ლოგიკა, ყველაზე სარისკო ვარაუდები და ღია საკითხები</div></div></header>
<p class="logic">{escape(LOGIC)}</p>
<h3>4 ყველაზე სარისკო ვარაუდი (ზღვრები შემოთავაზებულია, გუნდმა ტესტამდე უნდა დაადასტუროს)</h3>
<table><thead><tr><th style="width:21%">ვარაუდი</th><th style="width:23%">რა ვიცით დღეს</th><th style="width:21%">ტესტი</th><th style="width:19%">ზღვარი</th><th>თუ ვერ გავიდა</th></tr></thead><tbody>{rows(RISKS)}</tbody></table>
<h3>სად არის ინოვაცია ბიზნეს მოდელში</h3>
<table><thead><tr><th style="width:12%">ბლოკი</th><th style="width:31%">დღეს (ინტერვიუებიდან)</th><th style="width:33%">ჩვენი მოდელი</th><th>დეკის ანალოგი</th></tr></thead><tbody>{rows(INNOVATION)}</tbody></table>
<div class="cols"><div><h3>გასარკვევი გუნდთან</h3><ul class="con">{conflicts}</ul></div>
<div><h3>მტკიცებულების სიძლიერე</h3><p class="hon">{escape(HONESTY)}</p></div></div>
</div>
</body></html>
"""


def md_table(head, data) -> str:
    lines = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    lines += ["| " + " | ".join(r) + " |" for r in data]
    return "\n".join(lines)


def build_md() -> str:
    parts = [
        "# ბიზნეს მოდელის კანვასი: ALL access (კვირა 4, v1)\n",
        f"> {HONESTY}\n> ვიზუალური ვერსია: [AllAccess_BMC.pdf](AllAccess_BMC.pdf). წყარო-დეკები: ამავე საქაღალდეში; ტექსტი: `../_sources/week4-*.txt`. ფაილი გენერირებულია: `scripts/build-bmc.py`.\n",
        f"**მოდელის ლოგიკა:** {LOGIC}\n",
    ]
    for key in ("vp", "cs", "ch", "cr", "re", "kr", "ka", "kp", "co"):
        num, title, notes = BLOCKS[key]
        parts.append(f"## {num}. {title}\n")
        parts.append(md_table(["სეგმენტი", "ჩანაწერი", "წყარო"], [(SEGMENTS[s], t, src) for s, t, src in notes]) + "\n")
    parts.append("## 4 ყველაზე სარისკო ვარაუდი\n\nზღვრები შემოთავაზებულია, გუნდმა ტესტამდე უნდა დაადასტუროს.\n")
    parts.append(md_table(["ვარაუდი", "რა ვიცით დღეს", "ტესტი", "ზღვარი", "თუ ვერ გავიდა"], RISKS) + "\n")
    parts.append("## სად არის ინოვაცია ბიზნეს მოდელში\n")
    parts.append(md_table(["ბლოკი", "დღეს (ინტერვიუებიდან)", "ჩვენი მოდელი", "დეკის ანალოგი"], INNOVATION) + "\n")
    parts.append("## გასარკვევი გუნდთან\n")
    parts.append("\n".join(f"- {c}" for c in CONFLICTS) + "\n")
    return "\n".join(parts)


def main() -> None:
    (OUT / "AllAccess_BMC.html").write_text(build_html(), encoding="utf-8")
    (OUT / "business-model-canvas.md").write_text(build_md(), encoding="utf-8")


if __name__ == "__main__":
    main()
