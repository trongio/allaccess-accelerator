#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["python-docx", "python-pptx", "pypdf"]
# ///
"""Week 4 homework "Make your startup profitable": fill the course templates from one data set.

Inputs:  allaccess/week4/templates/{CUnicorn_Homework_Make_Your_Startup_Profitable.docx, Business_Model_Canvas.pptx}
Outputs: allaccess/week4/homework/
  AllAccess_Week4_Homework.docx   filled Word template
  AllAccess_Week4_BMC.pptx        filled canvas template
  homework.md                     same content for the repo/navigator
  AllAccess_Week4_Homework.html   print source -> .pdf (homework + ../AllAccess_BMC.pdf appended)
Run: uv run scripts/build-week4-homework.py
"""
import copy
import subprocess
from html import escape
from pathlib import Path

import docx
import pptx
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph
from pptx.util import Pt
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parent.parent
W4 = ROOT / "allaccess" / "week4"
TPL = W4 / "templates"
OUT = W4 / "homework"

TEAM = "ALL access (allaccess.ge)"
NAME = "ALL access გუნდი"
DATE = "09.11.2026"
PRICE = 99  # GEL per organisation per month, VAT included. HYPOTHESIS, not a published price.

# ---------------------------------------------------------------- content

PART1 = [
    ("ვინ არის ძირითადი მომხმარებელი?",
     "20-100 თანამშრომლიანი ბიზნესები ცვლებით და საათობრივი/დღიური ანაზღაურებით: საწარმოები, სასტუმროები, "
     "რესტორნები, კაზინოები, თბილისის გარეთაც. პირველი კლიენტი უკვე გვყავს: „კულინარი“, გაყინული საკვების "
     "საწარმო ქუთაისში, ~100 თანამშრომელი (ინსტალაცია მიმდინარეობს, ნოემბრის მე-2 კვირა). ყოველდღიური "
     "მომხმარებელი: დეპარტამენტის ან ცვლის ხელმძღვანელი, რომელიც დასწრების ფურცელს აწარმოებს, Excel-ში "
     "გადააქვს და დავებს არკვევს."),
    ("ვინ იხდის? იგივე პირია, ვინც იყენებს?",
     "არა. იხდის და წყვეტს მფლობელი ან გენერალური მენეჯერი; იყენებს ხელმძღვანელი, check-in-ს კი თავად "
     "თანამშრომლები აკეთებენ ტელეფონით. ეს მნიშვნელოვანია: სასტუმროს GM-მა (R03) ბარათის სისტემა მფლობელებს "
     "შესთავაზა და უარი მიიღო: „არ გვაქვს ფული“. ამიტომ მფლობელს შედეგი უნდა დავანახოთ, არა ფუნქციები."),
    ("რა პრობლემის გადაჭრაში გადაგვიხდიან?",
     "რეალურად ნამუშევარი ცვლა დღეს ქაღალდზე ან მეხსიერებაშია: ცვლის გაცვლა ზეპირად თანხმდება და არსად იწერება "
     "(R01, R02, R03), დავისას კი ერთადერთი შემოწმება კამერის გადახვევაა, 1-2 საათი თითო შემთხვევაზე (R03). "
     "დღიურ ანაზღაურებაზე (30-60 ₾ დღეში, R03-ის ხელფასების ფაილი) არასწორად ჩაწერილი დღე პირდაპირ არასწორი "
     "ხელფასია. გულწრფელად: ფოკუს სეგმენტში გადახდის მზადყოფნა ჯერ ერთი კლიენტით (კულინარი) დასტურდება."),
    ("რატომ აგვირჩევენ არსებული ალტერნატივის ნაცვლად?",
     "ალტერნატივები: ფურცელი + Excel, კამერის გადახვევა, ბარათის სისტემა აპარატურის შეცვლით („ძალიან ძვირია“, "
     "R01) ან ლოკალური პროგრამა. ჩვენთან: დასწრებას აპარატურა არ სჭირდება (check-in ტელეფონით, ერთ მოწყობილობაზე "
     "მიბმული და მხოლოდ ობიექტის Wi-Fi/IP-დან, GPS-ის გარეშე); გრაფიკი და ნამუშევარი ერთ დაფაზეა, ყოველი "
     "ცვლილება აღირიცხება; ბუღალტერი იღებს XLSX/CSV ტაბელს ზეგანაკვეთურით; ქართულ ენაზე; თუ S4A/ACB კარის "
     "პანელები აქვთ, კარებიც იმავე სისტემაში ერთვება; დაწყება უფასოა."),
    ("როგორ მივწვდებით და როგორ მივაწვდით?",
     "მიწვდომა: პირადი გაცნობა და პირდაპირი მიმართვა საწარმოებს, სასტუმროებს, რესტორნებს (ზღვარი: 20 მიმართვა, "
     "3 შეხვედრა), პარტნიორი ALL DIGITAL (alldigital.ge) კლიენტებს გვაწვდის, რეფერალი კულინარიდან, ბუღალტრები და დარგობრივი ასოციაციები (ჰიპოთეზა), allaccess.ge და "
     "ცოცხალი დემო. გაყიდვა: მფლობელთან ან GM-თან, მას შემდეგ, რაც ერთი დეპარტამენტი შედეგს აჩვენებს. მიწოდება: "
     "ბრაუზერი და ტელეფონის PWA, ჩართვის ზარი, 14-დღიანი საცდელი პერიოდი; კარის აპარატურას ამონტაჟებს პარტნიორი ALL DIGITAL."),
]

MODELS = [
    ("გამოწერა უფასო დასაწყისით (Freemium + Subscription)",
     f"ერთი დეპარტამენტი იწყებს უფასო ტარიფზე (10 თანამშრომლამდე, ტელეფონით check-in). როცა მთელ ბიზნესს "
     f"სჭირდება ან ცვლები სჭირდებათ, მფლობელი იხდის თვიურ გამოწერას: ჰიპოთეზა {PRICE} ₾/თვე ორგანიზაციაზე. "
     f"დამატებით: კარები, სტუმრები, დოკუმენტები, API.",
     "უპირატესობა: პროგნოზირებადი განმეორებადი შემოსავალი; დაბალი შესვლის ბარიერი პასუხობს „არ გვაქვს ფულს“ "
     "(R03); ყიდვა ქვემოდან იწყება. შეზღუდვა: უფასო მომხმარებლები ხარჯია შემოსავლის გარეშე; მცირე თვიური თანხის "
     "გამო ბევრი კლიენტი გვჭირდება; კლიენტის დაკარგვის (churn) რისკი; ფასი ჯერ შემოწმებული არ არის."),
    ("B2B გაყიდვა: პროექტი + წლიური კონტრაქტი",
     "უფრო დიდ ორგანიზაციებთან და კარის სისტემის მქონე კომპანიებთან: ერთჯერადი გადახდა აპარატურასა და "
     "მონტაჟზე ობიექტზე (მონტაჟს აკეთებს პარტნიორი ALL DIGITAL) + პროგრამის წლიური კონტრაქტი (Enterprise ინდივიდუალური "
     "ფასით). ასეთი გზით მიდის კულინარის ინსტალაცია (~100 თანამშრომელი).",
     "უპირატესობა: დიდი ჩეკი; ასეთ ორგანიზაციებში ბიუჯეტი არსებობს (R02: სკოლამ დაშვების სისტემისთვის "
     "~35 000 ₾ გამოყო). შეზღუდვა: გრძელი ციკლი (წლიური ბიუჯეტი, ბორდი); აპარატურიდან დღეს მხოლოდ S4A/ACB "
     "პანელებს ვმართავთ, Dahua, Suprema, ZKTeco, Hikvision დაგეგმილია; ბევრი გაყიდვის შრომა."),
]
MODELS_NOTE = ("შედარება: ფოკუს სეგმენტისთვის (20-100 თანამშრომელი) ძირითადია მოდელი 1, რადგან ფულის ბარიერს "
               "ამცირებს. მოდელი 2 ერთჯერად შემოსავალს იძლევა კარის სისტემის მქონე და დიდ კლიენტებთან.")

PART3 = [
    ("რისთვის იხდის მომხმარებელი?",
     "ორგანიზაციის თვიური წვდომა ALL access-ზე: check-in ტელეფონით (მოწყობილობის მიბმა + Wi-Fi/IP, GPS-ის "
     "გარეშე), გრაფიკი და ცვლები, დასწრების დაფა გრაფიკთან შედარებით, ცვლილებების ჟურნალი, დასტურების ერთი "
     "ყუთი, ტაბელის ექსპორტი XLSX/CSV ზეგანაკვეთური პრემიით. აპარატურა გამოწერაში არ შედის: კარის კონტროლერი "
     "და მონტაჟი ერთჯერადად, ობიექტის მიხედვით."),
    ("რა ფასს გვთავაზობთ?",
     f"ჰიპოთეზა (ჯერ შესამოწმებელი): {PRICE} ₾/თვე ორგანიზაციაზე, დღგ-ს ჩათვლით, განმეორებადი თვიური გადახდა, "
     f"50 თანამშრომლამდე (დასწრება + ცვლები). წლიური წინასწარი გადახდა: {PRICE * 10} ₾ (2 თვე საჩუქრად, "
     "ჰიპოთეზა). 10 თანამშრომლამდე უფასო ტარიფი, 14-დღიანი საცდელი პერიოდი. კარები და 50+ თანამშრომელი: "
     "დამატებით, ინდივიდუალურად."),
    ("რატომ არის ეს ფასი გონივრული?",
     f"R03-ის ხელფასების ფაილში 36 ადამიანია, დიდი ნაწილი დღიურ ანაზღაურებაზე, 30-60 ₾ დღეში. {PRICE} ₾ არის "
     f"ერთი თანამშრომლის 2-3 დღის ხელფასი თვეში, ან თვიური ხელფასის ფონდის დაახლოებით 0,2% (შეფასება: "
     "36 x ~45 ₾ x ~26 დღე = ~42 000 ₾). ერთი არასწორად ჩაწერილი დღე 30-60 ₾ ღირს, ერთი დავა GM-ს 1-2 საათს "
     "კამერაზე უჯდება (R03). აპარატურა არ სჭირდება, ამიტომ ბარათის სისტემის დიდი ერთჯერადი ხარჯი, რაზეც R03-ის "
     "მფლობელებმა უარი თქვეს, აქ არ არის."),
    ("რას ვეტყვით, თუ გვითხრეს „ძალიან ძვირია“?",
     "„გასაგებია. ბოლოს როდის მოგიწიათ კამერის გადახვევა ან ფურცლის გადამოწმება ცვლის გამო და რამდენი დრო "
     "წაიღო?“ შემდეგ: „დაიწყეთ უფასოდ ერთ დეპარტამენტში, 10 კაცამდე. თვის ბოლოს თავად ნახეთ, რამდენი დავა და "
     "საათი დაიზოგა, და მხოლოდ მაშინ გადაწყვიტეთ. აპარატურის ყიდვა არ გჭირდებათ.“ ფასს არ ვამცირებთ, "
     "რისკს ვამცირებთ."),
]

SCEN = [("Conservative", 20), ("Realistic", 50), ("Optimistic", 100)]
RAMP = (10, 30, 50)


def gel(n):
    return f"{n:,.0f}".replace(",", " ") + " ₾"


ramp_total = sum(RAMP) * PRICE
P4_TOTAL = (
    f"თუ კლიენტები 1-ლივე თვიდან გვყავს: {gel(20 * PRICE * 3)} / {gel(50 * PRICE * 3)} / {gel(100 * PRICE * 3)} "
    f"(კონს. / რეალ. / ოპტ., თვიური x 3). რეალისტური სცენარი ზრდით ({RAMP[0]} -> {RAMP[1]} -> {RAMP[2]} კლიენტი): "
    f"({RAMP[0]} + {RAMP[1]} + {RAMP[2]}) x {PRICE} ₾ = {gel(ramp_total)}; დღგ-ს (18%) გარეშე "
    f"{gel(ramp_total)} / 1,18 = {gel(ramp_total / 1.18)}."
)
P4_ASSUMPTIONS = [
    f"ფასი: საშუალოდ {PRICE} ₾ კლიენტზე (ჰიპოთეზა), დამატებებისა და აპარატურის გარეშე; გადახდა 14-დღიანი "
    "საცდელის შემდეგ; 3 თვეში კლიენტის დაკარგვა 0 (ოპტიმისტური დაშვება).",
    "ამოსავალი: დღეს 1 კლიენტი (კულინარი, ინსტალაცია მიმდინარეობს). ფოკუს სეგმენტში გადახდა სხვაგან ჯერ არ "
    "დასტურდება.",
    "პარტნიორი ALL DIGITAL აპარატურის მონტაჟს აკეთებს და კლიენტებს გვაწვდის; მისი არხიდან კლიენტების რაოდენობა "
    "ჯერ უცნობია, ამიტომ პროგნოზში ცალკე არ ვითვლით (ზედა რისკი ჩვენს სასარგებლოდ).",
    "ძაბრი (ჰიპოთეზა): 20 მიმართვიდან 3 შეხვედრა (15%), შეხვედრიდან ფასიანი კლიენტი 2-დან 1 (50%), ანუ "
    "მიმართვიდან ~7,5%. 50 კლიენტს 3 თვეში სჭირდება ~670 მიმართვა (~55 კვირაში). 3-კაციანი გუნდისთვის რეალურია "
    "20-30 კვირაში, ამიტომ ჩვენთვის „კონსერვატიული“ 20 კლიენტიც ამბიციურია. ცხრილის რიცხვები დავალების "
    "მოცემულობაა.",
    "შემოსავალი არ არის მოგება. მოგება = შემოსავალი - ხარჯები. ხარჯები: გუნდის ხელფასები, ღრუბლოვანი "
    "ინფრასტრუქტურა, გაყიდვა და ჩართვა (2-3 საათი კლიენტზე, შეფასება), მხარდაჭერა, უფასო ტარიფის "
    "მომხმარებლები. დღგ ჩვენი შემოსავალი არ არის. ხარჯების თანხებს გუნდი ავსებს; პირველ 3 თვეში მოგება, "
    "სავარაუდოდ, უარყოფითია: გუნდის ხარჯი შემოსავალზე მეტია.",
]

P5_INTRO = ("ჯერჯერობით გვაქვს 4 რეალური ინტერვიუ (R01-R04, 2026-10-31, The Mom Test, ციტატები პარაფრაზია). "
            "მათში ფასზე პირდაპირ არ გვიკითხავს, ამიტომ ქვემოთ არის ის, რაც ფულზე თავად თქვეს, და 5 ახალი "
            "ფასის ინტერვიუს სტრიქონი (P1-P5), რომლებსაც გუნდი 12 ნოემბრამდე ავსებს. კითხვებს ვსვამთ წარსულ "
            "ქცევაზე: „ამ პროცესზე დღეს რას იხდით?“, „ბოლოს რაზე დახარჯეთ ფული ამ მიზნით?“, ბოლოს კი ვითხოვთ "
            "ვალდებულებას (ფასიანი პირველი თვე).")
P5_HEAD = ["#", "რესპონდენტი", "გადაიხდის? რატომ?", "გონივრული ფასი", "გადახდის მოდელი", "რა შეუშლის ხელს"]
P5_ROWS = [
    ["R01", "გიგა, დეველოპერი, კაზინო (~100 ცვლის თანამშრომელი), მეორადი", "არ გვიკითხავს; „ჰკითხავს“ მენეჯერს",
     "არ გვიკითხავს", "-", "აპარატურის შეცვლა „ძალიან ძვირია“; მათ Suprema/Dahua-ს დღეს ვერ ვმართავთ"],
    ["R02", "ნიკა, დეველოპერი, კერძო სკოლა (~1000), მეორადი", "ბიუჯეტი არსებობს: ~35 000 ₾ დაშვების სისტემაზე",
     "არ გვიკითხავს", "ერთჯერადი პროექტი, წლიური ბიუჯეტი (ბორდი)", "მიზეზი მოსწავლეებია, არა პერსონალის დრო; ზომით სეგმენტის გარეთ"],
    ["R03", "ნინო, GM, სასტუმრო ლაგოდეხში (~36), პირველადი", "მფლობელებმა ბარათის სისტემაზე: „არ გვაქვს ფული“",
     "არ გვიკითხავს", "ნინოს აზრით, გამოწერაზე შეიძლება დათანხმებულიყვნენ (ჰიპოთეტური)", "ფული; მფლობელი ტკივილს ვერ ხედავს; თვის დახურვა <1 სთ"],
    ["R04", "გიორგი, ყოფილი ტესტერი, IT კომპანია (~600)", "არა: ფიქსირებული ხელფასი, დრო ხელფასს არ ცვლის",
     "-", "-", "საჭიროება არ არის"],
    ["P1", "კულინარი (რეალური კლიენტი): ვინც ყიდვა გადაწყვიტა", "", "", "", ""],
    ["P2", "ცვლებიანი საწარმოს ან სასტუმროს მფლობელი/GM", "", "", "", ""],
    ["P3", "რესტორნის მფლობელი ან მენეჯერი", "", "", "", ""],
    ["P4", "დეპარტამენტის/ცვლის ხელმძღვანელი", "", "", "", ""],
    ["P5", "ბუღალტერი, რომელიც ასეთ ბიზნესს ემსახურება", "", "", "", ""],
]
P5_SUMMARY = (
    "4 ინტერვიუდან გადახდა არცერთში არ დადასტურებულა. ძლიერი ფულის სიგნალები: R02-ის 35 000 ₾ (სხვა "
    "ამოცანაზე) და R03-ის უარი („არ გვაქვს ფული“) აპარატურაზე დაფუძნებულ ბარათის სისტემაზე. გადახდის "
    "მოდელზე: R03 გამოწერისკენ (ჰიპოთეტური), R02 ერთჯერადი პროექტისკენ. ბარიერები: ფული, მფლობელი ტკივილს ვერ "
    "ხედავს, აპარატურის შეცვლის ფასი. ყველაზე ძლიერი მტკიცებულება ინტერვიუს გარეთაა: კულინარი (~100 "
    "თანამშრომელი) უკვე კლიენტია. დასკვნა: გადახდის მზადყოფნა ყველაზე სარისკო ვარაუდია, {p} ₾ შეუმოწმებელია; "
    "P1-P5 ავსებს ამ ხარვეზს."
).format(p=PRICE)
P5_CHANGES = [
    "პროგრამა აპარატურისგან გამოვყავით: დასწრებას კარი არ სჭირდება, ამიტომ შეთავაზება აპარატურის ყიდვით აღარ "
    "იწყება (R01, R03).",
    "დიდი ერთჯერადი შესყიდვის ნაცვლად: უფასო დასაწყისი ერთ დეპარტამენტში და თვიური გამოწერა (R03).",
    "მყიდველი მფლობელია, ამიტომ მასთან მივდივართ ხელმძღვანელის შედეგით, არა ფუნქციების სიით (R03).",
    f"ფასი {PRICE} ₾ ჰიპოთეზად რჩება: ვამოწმებთ P1-P5-ით და concierge ტესტის ბოლოს ფასიანი პირველი თვის თხოვნით "
    "(ზღვარი: 2 მფლობელიდან მინიმუმ 1 იხდის). კულინარისგან ვიგებთ, რატომ იყიდეს და რა გადაიხადეს.",
]

PITCH = (
    "საწარმოებში, სასტუმროებსა და რესტორნებში ცვლის პერსონალის დიდი ნაწილი დღიურ ანაზღაურებაზეა: ნამუშევარი "
    "დღე პირდაპირ ხელფასია. დღეს ეს დღე ქაღალდის ფურცელზე იწერება, ცვლის გაცვლა ზეპირად თანხმდება, დავისას კი "
    "მენეჯერი 1-2 საათს კამერის გადახვევას ახმარს. ALL access ამას ტელეფონით ცვლის: თანამშრომელი check-in-ს "
    "საკუთარი ტელეფონიდან აკეთებს, მიბმულია ერთ მოწყობილობაზე და მუშაობს მხოლოდ ობიექტის Wi-Fi-დან; გრაფიკი და "
    "რეალურად ნამუშევარი ერთ დაფაზეა, თვის ბოლოს კი ბუღალტერი მზა ტაბელს იღებს. აპარატურის ყიდვა საჭირო არ არის. "
    f"ფულს ასე ვაკეთებთ: ერთი დეპარტამენტი 10 კაცამდე უფასოდ იწყებს, მთელი ბიზნესი თვიურ გამოწერას იხდის, ჩვენი "
    f"ჰიპოთეზით {PRICE} ლარს, ერთი თანამშრომლის 2-3 დღის ხელფასს. კარები და აპარატურა ცალკე იყიდება. პირველი "
    "კლიენტი უკვე გვყავს: კულინარი, 100-კაციანი საწარმო ქუთაისში, სისტემა ამ კვირაში ინსტალირდება. ახლა "
    "ვამოწმებთ, გადაიხდიან თუ არა სხვა მფლობელებიც: concierge ტესტის ბოლოს პირველ ფასიან თვეს ვთხოვთ."
)

CHECK = [
    (True, "ბიზნეს მოდელის კანვასი, 9 ბლოკი: AllAccess_Week4_BMC.pptx + დეტალური ვერსია წყაროებით (AllAccess_BMC.pdf)"),
    (True, "2 შემოსავლის მოდელი შედარებულია"),
    (True, f"ფასის სტრატეგია და დასაბუთება ({PRICE} ₾/თვე, ჰიპოთეზა)"),
    (True, "3-თვიანი პროგნოზი, 3 სცენარი, გამოთვლებით"),
    (False, "5 ინტერვიუ: 4 რეალური (R01-R04) + კულინარი; 5 ფასის ინტერვიუ (P1-P5) მიმდინარეობს"),
    (True, "60-წამიანი პიჩი"),
]

# Canvas: (template box title, font pt, bullets)
CANVAS = {
    "KEY PARTNERS": (8, [
        "ALL DIGITAL (alldigital.ge): აპარატურის მონტაჟი და კლიენტების მოყვანა",
        "S4A/ACB კონტროლერების მომწოდებლები (დღეს მხოლოდ ამ აპარატურას ვმართავთ)",
        "ბუღალტრები: ტაბელს იღებენ, შეიძლება კლიენტები გაგვაცნონ (ჰიპოთეზა)",
        "სასტუმროების, რესტორნების, მწარმოებლების ასოციაციები (ჰიპოთეზა)",
        "ღრუბლოვანი ინფრასტრუქტურის მომწოდებელი",
    ]),
    "KEY ACTIVITIES": (7.5, [
        "პროდუქტის განვითარება: დასწრება, ცვლები, კარები, აუდიტი",
        "პირდაპირი გაყიდვა მფლობელთან, ჩართვა ობიექტზე (კულინარი)",
        "Concierge ტესტი: ფურცლის ფოტოდან ტაბელი, ახალი კოდის გარეშე",
        "მხარდაჭერა ქართულად, ინგლისურად, რუსულად",
    ]),
    "KEY RESOURCES": (7.5, [
        "SaaS პლატფორმა, S4A/ACB დრაივერი, დაცული აუდიტის ჟურნალი",
        "დეველოპერები, გაყიდვები, აპარატურის ცოდნა",
        "ბრენდი ALL access, ოფისი ქუთაისში",
        "4 რეალური ინტერვიუ, პირველი კლიენტი",
    ]),
    "VALUE PROPOSITIONS": (8, [
        "ფურცლის ნაცვლად check-in ტელეფონით: ერთი მოწყობილობა + ობიექტის Wi-Fi/IP, GPS-ის გარეშე, აპარატურის ყიდვის გარეშე",
        "დავისას პასუხი ჩანაწერშია, არა 1-2 საათი კამერის გადახვევაზე (R03)",
        "გრაფიკი და რეალურად ნამუშევარი ერთ დაფაზე; ცვლილება აღირიცხება",
        "ტაბელი ბუღალტრისთვის XLSX/CSV, ზეგანაკვეთური პრემიით",
        "კარები და ადამიანები ერთ სისტემაში არსებულ S4A/ACB პანელებზე",
        "დაწყება უფასოა: ერთი დეპარტამენტი, 10 კაცამდე",
    ]),
    "CUSTOMER RELATIONSHIPS": (7.5, [
        "პირადი: ზარი, ჩართვა, 14-დღიანი საცდელი პერიოდი",
        "თანაშექმნა: concierge 2 ხელმძღვანელთან",
        "ხელმძღვანელი მფლობელს თავად აჩვენებს შედეგს",
        "Self-service უფასო ტარიფი (დაგეგმილი)",
    ]),
    "CHANNELS": (7.5, [
        "პარტნიორი ALL DIGITAL, პირადი გაცნობა, პირდაპირი მიმართვა, რეფერალი კულინარიდან",
        "allaccess.ge, ცოცხალი დემო",
        "გაყიდვა მფლობელთან ან GM-თან",
        "მიწოდება: ბრაუზერი + ტელეფონის PWA; აპარატურა ALL DIGITAL-ით",
    ]),
    "CUSTOMER SEGMENTS": (8, [
        "ფოკუსი: 20-100 თანამშრომლიანი ბიზნესი ცვლებით და საათობრივი/დღიური ანაზღაურებით (საწარმო, სასტუმრო, რესტორანი, კაზინო), თბილისის გარეთაც",
        "პირველი კლიენტი: კულინარი, გაყინული საკვების საწარმო, ქუთაისი, ~100",
        "მომხმარებელი: დეპარტამენტის/ცვლის ხელმძღვანელი; მყიდველი: მფლობელი ან GM",
        "კომპანიები S4A/ACB კარის პანელებით",
        "მიკრო ბიზნესი 10 კაცამდე: უფასო ტარიფი",
        "არა: ფიქსირებული ხელფასის ოფისები, 300+ საკუთარი სისტემით",
    ]),
    "COST STRUCTURE": (8, [
        "მუდმივი: გუნდის ხელფასები, ღრუბლოვანი ინფრასტრუქტურა, ოფისი",
        "ცვლადი: გაყიდვა და ჩართვა ობიექტზე (2-3 სთ კლიენტზე, შეფასება), მხარდაჭერა, concierge-ის საათები, ახალი დრაივერები",
        "უფასო ტარიფი: ხარჯი შემოსავლის გარეშე; აპარატურა გამოწერაში არ შედის",
        "პოლიტიკა: ახალ კოდს ვწერთ მხოლოდ გადახდის სიგნალის შემდეგ",
    ]),
    "REVENUE STREAMS": (8, [
        f"გამოწერა: {PRICE} ₾/თვე ორგანიზაციაზე, დღგ-ს ჩათვლით, 50 თანამშრომლამდე (ჰიპოთეზა)",
        "შესვლა: უფასო ტარიფი 10 კაცამდე, 14-დღიანი საცდელი პერიოდი",
        "დამატებები: კარები, სტუმრები, დოკუმენტები, API; Enterprise ინდივიდუალურად",
        "ერთჯერადი: აპარატურა და მონტაჟი ობიექტზე ALL DIGITAL-თან ერთად (B2B პროექტი, მაგ. კულინარი)",
    ]),
}

# ---------------------------------------------------------------- docx


def insert_after(par, text="", bold_prefix=None, style_from=None):
    new = OxmlElement("w:p")
    par._p.addnext(new)
    p = Paragraph(new, par._parent)
    src = style_from if style_from is not None else par
    if src._p.pPr is not None:
        new.insert(0, copy.deepcopy(src._p.pPr))
    if bold_prefix:
        p.add_run(bold_prefix).bold = True
    if text:
        p.add_run(text)
    return p


def set_runs(par, label, value):
    """Keep the first run as a bold label, put value in the second."""
    for r in par.runs[1:]:
        r._r.getparent().remove(r._r)
    par.runs[0].text = label
    par.runs[0].bold = True
    par.add_run(value)


def table_after(doc, par, rows, template_tbl, size=16):
    tbl = doc.add_table(rows=len(rows), cols=len(rows[0]))
    tbl._tbl.remove(tbl._tbl.tblPr)
    tbl._tbl.insert(0, copy.deepcopy(template_tbl._tbl.tblPr))
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = tbl.cell(i, j)
            c.text = ""
            run = c.paragraphs[0].add_run(val if val else ("შესავსები" if i and j > 1 else ""))
            run.font.size = docx.shared.Pt(size / 2)
            if i == 0:
                run.bold = True
    par._p.addnext(tbl._tbl)
    return tbl


def build_docx():
    d = docx.Document(TPL / "CUnicorn_Homework_Make_Your_Startup_Profitable.docx")
    P = list(d.paragraphs)
    for p in P:
        for r in p.runs:
            if "\u2014" in r.text:
                r.text = r.text.replace("\u2014", ": ")
    t0 = d.tables[0].rows[0].cells
    for c, (lab, val) in zip(t0, [("STARTUP / TEAM: ", TEAM), ("NAME: ", NAME), ("DATE: ", DATE)]):
        set_runs(c.paragraphs[0], lab, val) if len(c.paragraphs[0].runs) > 1 else (
            c.paragraphs[0].runs[0].__setattr__("text", lab), c.paragraphs[0].add_run(val))
    for idx, (_, ans) in zip((7, 9, 11, 13, 15), PART1):
        P[idx].runs[0].text = "Your answer: "
        P[idx].runs[0].bold = True
        P[idx].add_run(ans)
    for base, (name, how, pros) in zip((19, 22), MODELS):
        set_runs(P[base], P[base].runs[0].text, name)
        set_runs(P[base + 1], P[base + 1].runs[0].text, how)
        set_runs(P[base + 2], P[base + 2].runs[0].text, pros)
    insert_after(P[24], MODELS_NOTE)
    for idx, (_, ans) in zip((28, 30, 32, 34), PART3):
        P[idx].runs[0].text = "Your answer: "
        P[idx].runs[0].bold = True
        P[idx].add_run(ans)
    for row, (_, n) in zip(d.tables[2].rows[1:], SCEN):
        row.cells[2].paragraphs[0].runs[0].text = f"{PRICE} ₾ / თვე"
        row.cells[3].paragraphs[0].runs[0].text = f"{n} x {PRICE} = {gel(n * PRICE)}"
    set_runs(P[37], P[37].runs[0].text, P4_TOTAL)
    set_runs(P[38], P[38].runs[0].text, "")
    for a in reversed(P4_ASSUMPTIONS):
        insert_after(P[38], "- " + a)
    # Part 5
    intro = insert_after(P[44], P5_INTRO, style_from=P[40])
    table_after(d, intro, [P5_HEAD] + P5_ROWS, d.tables[1])
    set_runs(P[45], P[45].runs[0].text, P5_SUMMARY)
    set_runs(P[46], P[46].runs[0].text, "")
    for c in reversed(P5_CHANGES):
        insert_after(P[46], "- " + c)
    insert_after(P[50], PITCH, bold_prefix="ჩვენი პასუხი (60 წამი): ")
    for p, (done, txt) in zip(P[52:58], CHECK):
        p.runs[0].text = p.runs[0].text.replace("☐", "☑" if done else "☐") + "  (" + txt + ")"
    d.save(OUT / "AllAccess_Week4_Homework.docx")


# ---------------------------------------------------------------- pptx


def build_pptx():
    prs = pptx.Presentation(TPL / "Business_Model_Canvas.pptx")
    slide = prs.slides[0]
    for sh in slide.shapes:
        if not sh.has_text_frame:
            continue
        tf = sh.text_frame
        head = tf.paragraphs[0].text.strip()
        if head.startswith("VENTURE / TEAM"):
            tf.paragraphs[0].runs[0].text = f"VENTURE / TEAM: {TEAM}"
            continue
        if head not in CANVAS:
            continue
        size, bullets = CANVAS[head]
        paras = tf.paragraphs
        answer_tpl = paras[-1]._p
        for p in paras[1:]:
            p._p.getparent().remove(p._p)
        for b in bullets:
            np_ = copy.deepcopy(answer_tpl)
            tf._txBody.append(np_)
        for p, b in zip(tf.paragraphs[1:], bullets):
            p.runs[0].text = "• " + b
            p.runs[0].font.size = Pt(size)
            p.runs[0].font.color.rgb = RGBColor(0x1F, 0x2D, 0x3A)
            p.space_after = Pt(2)
    prs.save(OUT / "AllAccess_Week4_BMC.pptx")


# ---------------------------------------------------------------- md + html


def md():
    L = [f"# საშინაო დავალება, კვირა 4: Make your startup profitable ({TEAM})", "",
         f"> {DATE}. წყარო: CUnicorn-ის შაბლონები `../templates/`. ფაილები: [Word](AllAccess_Week4_Homework.docx), "
         "[კანვასი PPTX](AllAccess_Week4_BMC.pptx), [PDF](AllAccess_Week4_Homework.pdf). "
         f"ფასი {PRICE} ₾ ჰიპოთეზაა, არა გამოქვეყნებული ფასი. გენერირებულია: `scripts/build-week4-homework.py`.", "",
         "## ნაწილი 1: ბიზნეს მოდელი", ""]
    for i, (q, a) in enumerate(PART1, 1):
        L += [f"**{i}. {q}** {a}", ""]
    L += ["## ნაწილი 2: შემოსავლის მოდელები", ""]
    for i, (n, h, p) in enumerate(MODELS, 1):
        L += [f"**{i}. {n}.** {h}", "", f"{p}", ""]
    L += [MODELS_NOTE, "", "## ნაწილი 3: ფასი", ""]
    for q, a in PART3:
        L += [f"**{q}** {a}", ""]
    L += ["## ნაწილი 4: 3 თვის შემოსავლის პროგნოზი", "",
          "| სცენარი | ფასიანი კლიენტი | ფასი / კლიენტი | თვიური შემოსავალი |", "|---|---|---|---|"]
    L += [f"| {s} | {n} | {PRICE} ₾ | {n} x {PRICE} = {gel(n * PRICE)} |" for s, n in SCEN]
    L += ["", f"**3 თვის ჯამი:** {P4_TOTAL}", "", "**დაშვებები:**", ""] + [f"- {a}" for a in P4_ASSUMPTIONS]
    L += ["", "## ნაწილი 5: ვარაუდების ვალიდაცია", "", P5_INTRO, "",
          "| " + " | ".join(P5_HEAD) + " |", "|" + "---|" * len(P5_HEAD)]
    L += ["| " + " | ".join(c or "შესავსები" for c in r) + " |" for r in P5_ROWS]
    L += ["", f"**მიგნებები:** {P5_SUMMARY}", "", "**რა შევცვალეთ:**", ""] + [f"- {c}" for c in P5_CHANGES]
    L += ["", "## 60-წამიანი პიჩი ინვესტორისთვის", "", PITCH, "", "## ჩაბარების სია", ""]
    L += [f"- [{'x' if d else ' '}] {t}" for d, t in CHECK]
    (OUT / "homework.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def html():
    e = escape
    S = []
    S.append(f"<header><h1>Make your startup profitable</h1><p class=sub>CUnicorn, კვირა 4: ბიზნეს მოდელი და შემოსავლის წყაროები</p>"
             f"<table class=meta><tr><td><b>გუნდი:</b> {e(TEAM)}</td><td><b>ავტორი:</b> {e(NAME)}</td><td><b>თარიღი:</b> {DATE}</td></tr></table></header>")
    S.append("<h2>ნაწილი 1: ბიზნეს მოდელი</h2><ol class=qa>" + "".join(
        f"<li><p class=q>{e(q)}</p><p>{e(a)}</p></li>" for q, a in PART1) + "</ol>")
    S.append("<h2>ნაწილი 2: შემოსავლის მოდელები</h2>" + "".join(
        f"<div class=card><h3>{i}. {e(n)}</h3><p><b>როგორ მუშაობს:</b> {e(h)}</p><p><b>უპირატესობა / შეზღუდვა:</b> {e(p)}</p></div>"
        for i, (n, h, p) in enumerate(MODELS, 1)) + f"<p>{e(MODELS_NOTE)}</p>")
    S.append("<h2>ნაწილი 3: ფასი</h2><p class=badge>ფასი " + str(PRICE) + " ₾ ჰიპოთეზაა, ჯერ შესამოწმებელი</p>" + "".join(
        f"<p class=q>{e(q)}</p><p>{e(a)}</p>" for q, a in PART3))
    rows = "".join(f"<tr><td>{s}</td><td>{n}</td><td>{PRICE} ₾</td><td>{n} x {PRICE} = <b>{gel(n * PRICE)}</b></td></tr>" for s, n in SCEN)
    S.append("<h2>ნაწილი 4: 3 თვის შემოსავლის პროგნოზი</h2><p>შემოსავალი = ფასიანი კლიენტები x ფასი კლიენტზე</p>"
             f"<table class=grid><tr><th>სცენარი</th><th>ფასიანი კლიენტი</th><th>ფასი / კლიენტი</th><th>თვიური შემოსავალი</th></tr>{rows}</table>"
             f"<p><b>3 თვის ჯამი:</b> {e(P4_TOTAL)}</p><p class=q>დაშვებები</p><ul>" + "".join(f"<li>{e(a)}</li>" for a in P4_ASSUMPTIONS) + "</ul>")
    trs = "".join("<tr>" + "".join(f"<td class={'todo' if not c else ''}>{e(c or 'შესავსები')}</td>" for c in r) + "</tr>" for r in P5_ROWS)
    S.append(f"<h2>ნაწილი 5: ვარაუდების ვალიდაცია</h2><p>{e(P5_INTRO)}</p><table class='grid small'><tr>"
             + "".join(f"<th>{e(h)}</th>" for h in P5_HEAD) + f"</tr>{trs}</table>"
             f"<p><b>მიგნებები:</b> {e(P5_SUMMARY)}</p><p class=q>რა შევცვალეთ ინტერვიუების შემდეგ</p><ul>"
             + "".join(f"<li>{e(c)}</li>" for c in P5_CHANGES) + "</ul>")
    S.append(f"<h2>60-წამიანი პიჩი ინვესტორისთვის</h2><p class=q>„როგორ გამოიმუშავებს თქვენი სტარტაპი ფულს და რატომ გადაიხდიან მომხმარებლები?“</p><blockquote>{e(PITCH)}</blockquote>")
    S.append("<h2>ჩაბარების სია</h2><ul class=check>" + "".join(
        f"<li>{'☑' if d else '☐'} {e(t)}</li>" for d, t in CHECK) + "</ul><p class=foot>ბიზნეს მოდელის კანვასი (9 ბლოკი, წყაროებით) მოცემულია შემდეგ გვერდზე.</p>")
    css = """@page{size:A4;margin:16mm 15mm}body{font-family:"Noto Sans Georgian","Noto Serif Georgian",sans-serif;font-size:10pt;line-height:1.5;color:#1f2d3a}
header{border-bottom:3px solid #2c6087;margin-bottom:10px}h1{margin:0;color:#2c6087;font-size:20pt}.sub{margin:2px 0 6px;color:#5a6c78}
.meta{width:100%;font-size:9pt;margin-bottom:6px}h2{color:#2c6087;font-size:13pt;border-bottom:1px solid #c9d6e0;padding-bottom:2px;margin-top:16px;break-after:avoid}
h3{font-size:10.5pt;margin:0 0 4px}.q{font-weight:700;margin:8px 0 2px}.qa li{margin-bottom:6px}.qa p{margin:0}.card{border:1px solid #c9d6e0;border-radius:6px;padding:8px 10px;margin:8px 0;break-inside:avoid}
.card p{margin:3px 0}.badge{display:inline-block;background:#fff4d6;border:1px solid #e6c35c;border-radius:4px;padding:1px 8px;font-size:9pt}
table.grid{border-collapse:collapse;width:100%;margin:6px 0}.grid th,.grid td{border:1px solid #c9d6e0;padding:4px 6px;text-align:left;vertical-align:top}.grid th{background:#eaf1f7}
.small{font-size:8.5pt}.todo{color:#9aa5ae;font-style:italic}tr{break-inside:avoid}blockquote{margin:6px 0;padding:8px 12px;background:#f3f7fa;border-left:4px solid #2c6087}
.check{list-style:none;padding-left:0}.foot{color:#5a6c78;font-size:9pt}"""
    doc = f"<!doctype html><html lang=ka><head><meta charset=utf-8><title>ALL access: კვირა 4</title><style>{css}</style></head><body>{''.join(S)}</body></html>"
    path = OUT / "AllAccess_Week4_Homework.html"
    path.write_text(doc, encoding="utf-8")
    return path


def pdf(src):
    body = OUT / "_body.pdf"
    subprocess.run(["/usr/bin/google-chrome", "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={body}", src.as_uri()], check=True, capture_output=True)
    from pypdf import PdfWriter
    w = PdfWriter()
    w.append(str(body))
    w.append(str(W4 / "AllAccess_BMC.pdf"))
    w.write(str(OUT / "AllAccess_Week4_Homework.pdf"))
    body.unlink()


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_docx()
    build_pptx()
    md()
    pdf(html())
    print("ok:", *sorted(p.name for p in OUT.iterdir()))
