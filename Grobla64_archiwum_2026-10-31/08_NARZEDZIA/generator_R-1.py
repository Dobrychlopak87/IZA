import base64, io
from PIL import Image

OUT = '/home/user/report/Raport_Grobla64_etap3.html'
FIG = []


def img(path, w=780, q=80):
    im = Image.open(path).convert('RGB')
    if im.width > w:
        im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=q, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()


def fig(path, num, title, meta, desc, src=None):
    u = img(path)
    FIG.append(f"""<figure>
  <img src="{u}" alt="{num}">
  <figcaption><h4><span class="num">{num}</span>{title}</h4>
  <div class="meta">{meta}</div>
  <p>{desc}</p>
  {f'<div class="src">Źródło: {src}</div>' if src else ''}
  </figcaption></figure>""")
    return '{{FIG%d}}' % len(FIG)


F1 = fig('/home/user/work/dossier/w01_redbox.jpg', 'W-01', 'Zdjęcie wyjściowe z zaznaczonym obiektem',
         'Landesarchiv NRW, RW 0229 Nr. 46002 (Hansa Luftbild), bez daty, ok. 1925–1932',
         'Obiekt w czerwonym prostokącie: biały dom z kominem + duża ciemna połać dachowa, w sadzie nad wodą. Od etapu II wiadomo, że chodzi o działkę <strong>61/6 przy ul. Grobla 64</strong>.',
         'archivportal-d.de, sygn. RW 0229 Nr. 46002')

F2 = fig('/home/user/work/dossier/d01_detail.jpg', 'W-02', 'Powiększenie obiektu (ok. ×6)',
         'wycinek z RW 0229 Nr. 46002',
         'Dwie bryły: dom i szeroki budynek gospodarczy. Ten sam układ — dom + warsztat — potwierdza najnowsze źródło: ogłoszenie sprzedaży nieruchomości z 2022 r. (karta N-01).')

F3 = fig('/home/user/work/g64/g64_tight.jpg', 'D-01', 'Działka 61/6 dziś — ortofoto',
         'GUGiK, ORTO HighResolution (WMS), 2026-10-28; kadr ok. 200 m; środek: 52,046242 N / 15,096015 E',
         'Duży budynek gospodarczy o ciemnym dachu przy wale, nieutwardzony plac, niżej dwa mniejsze obiekty. Działka leży na <strong>końcu ulicy</strong> — za nią Grobla już się nie numeruje: dalej zaczyna się teren starego ujścia Bobru.')

F4 = fig('/home/user/work/g64/comp_tight.jpg', 'D-02', 'Granice ewidencyjne na ortofoto',
         'KIEG (WMS: „dzialki”, „numery_dzialek”) na ortofoto GUGiK, 2026-10-28',
         'Etykieta <strong>61/6</strong> w obrębie ogrodzonego placu z halą. Działka: 1 684 m², klasoużytek Bi, 309 m² zabudowy, 3 budynki, grupa rejestrowa 5.')

F5 = fig('/home/user/work/g64/off1.jpg', 'N-01', 'Makieta oferty sprzedaży: obrys oferowanej nieruchomości',
         'ogłoszenie prywatne, nieruchomosci-online.pl, oferta nr 23258112, aktualizacja 07.04.2022',
         'Zrzut z serwisu e-mapa użyty przez sprzedającego: zielony obrys obejmuje halę przy wale i zespół budynków w głębi działki. Widać też sąsiednie numery (61/4, 61/5, 61/6, 66…). <strong>To pierwszy materiał, w którym sam właściciel wskazuje granice i zabudowę tej posesji.</strong>',
         'krosno-odrzanskie.nieruchomosci-online.pl/dzialka,budowlana,ogrodzona/23258112.html')

F6 = fig('/home/user/work/g64/hal/p05_Im9.jpg', 'H-01', '„Amtsfischerei mit Silberberg” — kanał rybacki z łodziami',
         'pocztówka kolorowana, reprodukcja w: B. Halicka, <em>Krosno Odrzańskie</em>, rozdz. 5',
         'Drewniane łodzie rybackie przy brzegu kanału, na prawym brzegu stelaż (suszenie sieci/sprzętu). Najlepszy znany widok wnętrza kwartału rybackiego — tego samego, w którym leży działka 61/6.',
         'beatahalicka.pl, PDF rozdz. 5')

F7 = fig('/home/user/work/g64/hal/p22_Im36.jpg', 'H-02', 'Siedziba Klubu Wioślarskiego 1885',
         'fotografia, reprodukcja w: B. Halicka, rozdz. 5 (podpis oryg.: „Sitz des Ruderclubs 1885”)',
         'Biały, dwukondygnacyjny dom z okiennicami, latarnią przy drzwiach i pergolą w ogrodzie. Bryła łudząco podobna do domu z czerwonego prostokąta — ale <strong>adresy klubu (Boberstr. 39 w 1926 r., Klosterplatz 8 w 1938 r.) nie odpowiadają działce 61/6</strong>, więc nie utożsamiam tych obiektów. Materiał ma wartość porównawczą: pokazuje, jak wyglądała nadwodna architektura klubowa w tym kwartale.')

F8 = fig('/home/user/work/g64/hal/p23_Im37.jpg', 'H-03', 'Chrzest łodzi na 25-leciu Klubu Wioślarskiego 1913',
         'fotografia, ok. 1938; reprodukcja w: B. Halicka, rozdz. 5 („Bootstaufe anläßlich der 25-Jahr-Feier des Ruderclubs 1913”)',
         'Pomost, trybuna i publiczność — dokumentacja infrastruktury wodnej (pomosty, rampy) kwartału. Klub „1913” miał w 1938 r. adres Uferstr. 2.')

F9 = fig('/home/user/work/g64/p45_w.jpg', 'P-01', 'Plan Crossen 1:5000 (stan 1945) — zachodni skraj starówki',
         'plan niemiecki, reprod. Heimatkreis Crossen/Oder (za: Fotopolska)',
         'Czytelne <strong>Grabenstr.</strong> i <strong>Westpromenade</strong>. To potwierdza — niezależnie od opisu polska-org — że południowy odcinek dzisiejszej Grobli nosił nazwę Westpromenade.')

CSS = """
:root{--ink:#16181d;--mut:#5c6270;--line:#dfe3ea;--acc:#8c1c13;--bg:#f6f4ef}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.62 Georgia,'Times New Roman',serif}
.wrap{max-width:1020px;margin:0 auto;padding:0 22px 90px}
header{background:linear-gradient(160deg,#101317,#232a33);color:#fff;padding:50px 22px 38px;margin-bottom:32px;border-bottom:5px solid var(--acc)}
header .in{max-width:1020px;margin:0 auto}
header .kicker{font:600 12px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#e0b7b1}
h1{font:700 33px/1.15 Georgia,serif;margin:.35em 0 .2em}
header p{color:#c8ced8;max-width:72ch;margin:.4em 0 0}
h2{font:700 25px/1.2 Georgia,serif;margin:50px 0 6px;padding-bottom:8px;border-bottom:2px solid var(--ink)}
h3{font:700 19px/1.3 Georgia,serif;margin:28px 0 6px}
h4{font:700 16.5px/1.35 Georgia,serif;margin:0 0 4px}
p{margin:.55em 0}a{color:#7a1710}
.lead{font-size:17.5px;color:#2a2f38}
.note{font:13.5px/1.55 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);border-left:3px solid var(--line);padding-left:12px;margin-top:10px}
figure{margin:26px 0;background:#fff;border:1px solid var(--line);border-radius:6px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.04)}
figure img{display:block;width:100%;height:auto;background:#000}
figcaption{padding:14px 18px 16px}
.num{display:inline-block;font:700 11.5px/1 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.1em;color:#fff;background:var(--acc);padding:5px 8px;border-radius:3px;margin-right:9px;vertical-align:2px}
.meta{font:13px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin:5px 0 8px}
.src{font:12.5px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;word-break:break-word}
table{width:100%;border-collapse:collapse;margin:16px 0;background:#fff;font:14.5px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;border:1px solid var(--line)}
th{background:#eceff4;text-align:left;padding:9px 11px;font-weight:700;border-bottom:1px solid #cfd6e0}
td{padding:8px 11px;border-bottom:1px solid #eef1f5;vertical-align:top}
tr:last-child td{border-bottom:0}
.box{background:#fff;border:1px solid var(--line);border-left:5px solid var(--acc);border-radius:5px;padding:16px 20px;margin:22px 0}
.box.ok{border-left-color:#1d6b3f}.box.warn{border-left-color:#b06a00}
ul,ol{margin:.5em 0 .9em;padding-left:1.3em}li{margin:.3em 0}
.tag{display:inline-block;font:600 11px/1 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border-radius:3px;margin-right:6px}
.t-fakt{background:#1d6b3f;color:#fff}.t-wn{background:#1f4e79;color:#fff}.t-hip{background:#8a5b00;color:#fff}.t-brak{background:#6b7280;color:#fff}.t-kor{background:#8c1c13;color:#fff}
.small{font-size:14px}
footer{margin-top:56px;padding-top:18px;border-top:1px solid var(--line);font:13px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut)}
@media(max-width:760px){h1{font-size:26px}}
"""

HTML = f"""<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grobla 64 / dz. 61/6 — etap III</title><style>{CSS}</style></head><body>
<header><div class="in">
<div class="kicker">Kwerenda archiwalna · etap III · nowe źródła</div>
<h1>Grobla 64, dz. 61/6 — co przyniosła trzecia tura</h1>
<p>Trzy nowe, niezależne źródła: ogłoszenie sprzedaży nieruchomości (2022), drukowana monografia Beaty Halickiej (rozdz. 5–6) oraz adresy klubów wodnych w księgach adresowych 1926 i 1938. Do tego dwie korekty wcześniejszych ustaleń.</p>
</div></header>
<div class="wrap">

<div class="box warn">
<h3 style="margin-top:0"><span class="tag t-kor">korekta</span>Dwie rzeczy z etapu II były nieprecyzyjne</h3>
<ol>
<li><strong>Ujście Bobru przesunięto w latach 1908–1910</strong>, o około 2 km na zachód — nie w latach 30. (B. Halicka, rozdz. 5: <em>„podjęte w latach 1908–10 przedsięwzięcie przesunięcia o dwa kilometry na zachód ujścia Bobru”</em>). Stare koryto posłużyło do poprowadzenia wód rowu miejskiego.</li>
<li><strong>Westpromenade = południowy odcinek dzisiejszej Grobli</strong> — to już nie tylko opis w polska-org, ale zdanie z monografii: <em>„Promenada Zachodnia (Westpromenade — południowa część ulicy Grobla) powstała w wyniku zasypania rowów miejskich i posadzenia alei drzew oraz utworzenia terenów spacerowych”</em>. Dodatkowo: <em>„Pomiędzy pierwotnym ujściem Bobru a centrum starego miasta znajdują się Rybaki, ówczesna Fischerei”</em>.</li>
</ol>
</div>

<h2>1. Materiał bazowy (przypomnienie)</h2>
{F1}
{F2}
{F3}
{F4}

<h2>2. Nieruchomość wyszła na rynek — mamy jej opis od właściciela (2022)</h2>
<table>
<thead><tr><th>Parametr z ogłoszenia</th><th>Wartość</th></tr></thead>
<tbody>
<tr><td>Adres / oferta</td><td>Grobla 64, Krosno Odrzańskie — oferta nr 23258112 (prywatna), aktualizacja <strong>07.04.2022</strong></td></tr>
<tr><td>Powierzchnia</td><td><strong>1 792 m²</strong> (uwaga: EGiB dla dz. 61/6 podaje 1 684 m² — oferta może obejmować inną sumę działek lub dane sprzed zmiany)</td></tr>
<tr><td>Cena</td><td>450 000 zł (251,12 zł/m²)</td></tr>
<tr><td>Zabudowa — <strong>kluczowa informacja</strong></td><td><strong>„budynek mieszkalny do remontu i warsztat”</strong></td></tr>
<tr><td>Forma własności</td><td>„własność, księga wieczysta”</td></tr>
<tr><td>Media i kształt</td><td>prąd, woda miejska, kanalizacja (działka uzbrojona), teren płaski, kształt prostokąt, ogrodzenie całkowite, dojazd asfaltowy, wydane warunki zabudowy</td></tr>
<tr><td>Otoczenie (opis sprzedającego)</td><td>„w bezpośrednim sąsiedztwie i z dostępem do <strong>rewitalizowanego kanału Odry</strong>”; osiedle domów jednorodzinnych, rzeka</td></tr>
<tr><td>Stan oferty dziś</td><td>oznaczona jako <em>niedostępna</em> („OutOfStock”) — oferta wygasła lub nieruchomość sprzedana; nie ustaliłem tego na podstawie aktu, tylko statusu ogłoszenia</td></tr>
</tbody></table>
{F5}
<div class="box ok">
<p style="margin:0"><span class="tag t-wn">wniosek</span><strong>„Dom mieszkalny + warsztat” to dokładnie dwuczęściowy układ z czerwonego prostokąta</strong> (biały dom z kominem + duża ciemna hala). Nie jest to jeszcze identyfikacja funkcji historycznej, ale pierwsze źródło, które nazywa obie bryły i pochodzi od osoby znającej nieruchomość od środka. Różnica właścicielska (EGiB: grunt gminny, grupa 5 „w zbiegu z użytkowaniem wieczystym”; ogłoszenie: „własność, księga wieczysta”) wskazuje na typowy układ: <strong>grunt komunalny w użytkowaniu wieczystym, budynki — własność prywatna</strong>. Rozstrzygnie to dopiero odpis księgi wieczystej.</p>
</div>

<h2>3. Kluby wioślarskie — najlepiej udokumentowany zespół wodny w tym kwartale</h2>
<p>Monografia Halickiej (rozdz. 5) opisuje dwa crossneńskie kluby wioślarskie i ich infrastrukturę — z datami, funkcjami pomieszczeń i lokalizacją:</p>
<table>
<thead><tr><th>Klub</th><th>Co wiadomo (Halicka, rozdz. 5)</th><th>Adres w księdze adresowej</th></tr></thead>
<tbody>
<tr><td><strong>Ruderclub 1885</strong><br>(zalożony przez wydawcę Richarda Zeidlera)</td><td>W <strong>1919</strong> r. kupiono działkę <strong>na Rybakach w okolicach kładki do folwarku Klette</strong> (późniejsza siedziba Zarządu Dróg Wodnych). Najpierw pomieszczenie do przechowywania łodzi; w <strong>1924</strong> r. nowy budynek z kuchnią, stołówką, szatniami i łazienkami; dwa lata później dodatkowe pomieszczenia, <strong>schronisko dla kajakarzy, rampa dla łódek i nowy masywny pomost</strong>. W 1920 r. ok. 100 członków; od 1929 r. także kobiety.</td><td><strong>1926: „Ruder-Club Crossen a. O. von 1885 (E.V.)” — Boberstr. 39</strong><br><strong>1938: „Ruder-Klub v. 1885 E.V.” — Klosterplatz 8</strong> (dziś pl. Prusa)</td></tr>
<tr><td><strong>Ruderclub „1913”</strong></td><td>Założony przed I wojną; własne zaplecze wybudowane w <strong>1922</strong> r. Zdjęcie chrztu łodzi z 25-lecia klubu (ok. 1938) — karta H-03.</td><td><strong>1938: Uferstr. 2</strong></td></tr>
</tbody></table>
<div class="box">
<h3 style="margin-top:0">Łańcuch dowodowy, który udało się domknąć</h3>
<p>W księdze z 1926 r. pod adresem <strong>Boberstr. 39</strong> figurują <em>dwie</em> pozycje: klub wioślarski „von 1885” oraz <strong>Kommelt Fritz, <em>Bootshausverwalter</em></strong> — zarządca domu łodziowego. To znaczy, że dom łodziowy klubu działał pod tym samym adresem co siedziba, a jego istnienie potwierdza niezależnie słownik zawodów (etap II). Mamy więc w tym kwartale: <em>dom łodziowy z zarządcą</em>, <em>rampę</em>, <em>masywny pomost</em> i <em>schronisko kajakowe</em> — pełną infrastrukturę, jakiej wymaga obsługa ruchu łodziowego.</p>
</div>
{F7}
{F8}
<div class="box warn">
<p style="margin:0"><span class="tag t-brak">granica wniosku</span><strong>Nie utożsamiam działki 61/6 z siedzibą Ruderclubu 1885.</strong> Adresy klubu (Boberstr. 39 w 1926, Klosterplatz 8 w 1938) nie pokrywają się z południowym końcem Grobli. Klub jest tu wartością <em>porównawczą i kontekstową</em>: pokazuje, jak gęsta była nadwodna infrastruktura Rybaków i jakiego typu obiekty (dom + szeroka hala + pomost) w tym kwartale stawiano.</p>
</div>

<h2>4. Sam kwartał: co jeszcze mówi monografia</h2>
<ul>
<li><strong>Rybaki</strong> to „ówczesna Fischerei”, najstarsza metryka miejska (pierwsze podgrodzie), do połowy XX w. <strong>oddzielone od miasta odnogą rowu miejskiego</strong> (dawniej Bobru) — charakter wyspowy, ludność rybacka.</li>
<li>Po przesunięciu ujścia Bobru (1908–10) <strong>drewniana kładka do folwarku Klette została zachowana</strong> i jest widoczna na starych widokówkach.</li>
<li>Kąpielisko miejskie znad Bobru <strong>przeniesiono nad rów miejski w okolicy mostu Elizy</strong> — to obiekt sąsiadujący z naszym kwartałem od północy.</li>
<li>W 1926 r. w mieście działa jeszcze <strong>drugi klub wioślarski „1913”</strong>, a w 1938 r. księga branżowa notuje ulicę <strong>„Am Hafen”</strong> (przy porcie) — czyli port rzeczny funkcjonował jeszcze w końcu lat 30.</li>
</ul>
{F6}
{F9}

<h2>5. Co to zmienia w hipotezach o obiekcie z 1930 r.</h2>
<table>
<thead><tr><th>Hipoteza</th><th>Status po etapie III</th></tr></thead>
<tbody>
<tr><td><strong>H1. Dom rzemieślnika/rybaka z warsztatem</strong> (sieciarnia, wędzarnia, warsztat szkutniczy)</td><td><span class="tag t-wn">wzmocniona</span> Ogłoszenie z 2022 r. nazywa dokładnie te dwie funkcje: dom mieszkalny + warsztat. W kwartale w 1938 r. działały wędzarnia (Dammstr. 5) i dwie handlownie ryb (Fischergasse 1 i 3), a szkutnik Seide pracował przy Grabenstr. 28.</td></tr>
<tr><td><strong>H2. Zaplecze przystani / dom łodziowy</strong></td><td><span class="tag t-hip">osłabiona jako identyfikacja, wzmocniona jako kontekst</span> Infrastruktura łodziowa w kwartale jest bogato udokumentowana (Ruderclub 1885: dom łodziowy, rampa, pomost; klub „1913”), ale jej adresy są inne niż 61/6. Nie wykluczam prywatnego domu łodziowego lub wypożyczalni — dziś pod tym adresem działa wypożyczalnia łodzi wędkarskich.</td></tr>
<tr><td><strong>H3. Obiekt administracji wodnej</strong></td><td><span class="tag t-brak">niepotwierdzona</span> Halicka podaje, że miejsce po klubie 1885 stało się „późniejszą siedzibą Zarządu Dróg Wodnych” — ale przypisuje to okolicom kładki do Klette, nie naszej działce. Wymaga sprawdzenia w aktach 1945–1955.</td></tr>
</tbody></table>

<h2>6. Zaktualizowana lista kwerend — teraz krótsza i konkretniejsza</h2>
<ol>
<li><strong>Odpis księgi wieczystej dla dz. 61/6</strong> (Sąd Rejonowy w Krośnie Odrzańskim). Ogłoszenie z 2022 r. potwierdza, że KW istnieje. Dział II pokaże ciąg właścicieli — a przy nieruchomościach poniemieckich w aktach bardzo często leżą <strong>odpisy niemieckich Grundbuchblätter</strong> z nazwą ulicy i numerem posesji.</li>
<li><strong>Starostwo Powiatowe — wydruk z rejestru budynków</strong> dla dz. 61/6: rok budowy i funkcja każdego z trzech budynków. To jedyna droga, by stwierdzić, czy hala przy wale stoi od przed wojny.</li>
<li><strong>Urząd Miasta — akta sprzedaży/dzierżawy</strong> dz. 61/6 (grupa rejestrowa 5, grunt komunalny): kto był użytkownikiem wieczystym, kiedy powstało użytkowanie, czy i kiedy gmina zbywała grunt. Wniosek o informację publiczną + wgląd do akt przetargowych.</li>
<li><strong>Kontakt z autorem ogłoszenia z 2022 r.</strong> (oferta prywatna, imię „Szczepan” w formularzu kontaktowym) — osoba ta zna stan i historię obu budynków; to najtańsza i najszybsza weryfikacja hipotezy H1.</li>
<li><strong>Archiwum Państwowe w Zielonej Górze</strong> — akta miasta Crossen (<em>Bauakten</em> posesji) i Starostwo Krośnieńskie 1945–1950 (przejęcia mienia poniemieckiego).</li>
<li><strong>Geheimes Staatsarchiv PK, Rep. 97 Nr. 5540</strong> — <em>Grundstücksverzeichnis des Amtsgerichts Crossen a. O.</em>, 1921–1937.</li>
<li><strong>Przypis 174 monografii Halickiej</strong> — sprawdzić, na jakim źródle opiera opis Ruderclubu 1885 (możliwe, że citations prowadzą do archiwum klubu lub do <em>Crossener Kreiskalender</em>, który zawiera sprawozdania stowarzyszeń).</li>
<li><strong>Hansa Luftbild, RW 0229</strong> — negatywy 46002, 7482, 7485, 7486: data nalotu i odbitki wyższej jakości (bez daty nie da się porównać stanu zabudowy).</li>
</ol>

<h2>7. Przebieg kwerendy w tym etapie</h2>
<h3>Nowe źródła wykorzystane</h3>
<ul>
<li><strong>B. Halicka, <em>Krosno Odrzańskie</em>, rozdz. 5 i 6 (PDF, beatahalicka.pl)</strong> — pełny tekst, przeszukany; 34 + 13 stron; 45 ilustracji wypakowanych z PDF i przejrzanych. Stąd: Westpromenade = południowa Grobla, Rybaki = Fischerei, przesunięcie ujścia Bobru 1908–10, kładka do Klette, Ruderclub 1885 (1919/1924/1926) i klub „1913” (1922).</li>
<li><strong>nieruchomosci-online.pl</strong> — archiwalne ogłoszenie sprzedaży Grobla 64 (nr 23258112, 07.04.2022) wraz z makietą działki i opisem „dom do remontu + warsztat”.</li>
<li><strong>Brandenburg-Datenbank</strong> (te same transkrypcje, przeszukane pod kątem klubów): Ruder-Club 1885 — Boberstr. 39 (1926) i Klosterplatz 8 (1938); Ruder-Club 1913 — Uferstr. 2 (1938); ulica „Am Hafen” (1938).</li>
<li><strong>polska-org</strong> — karta miasta (4309874) i karta portu rzecznego (6804024, zdjęcie 2017 r.).</li>
</ul>
<h3>Ślepe uliczki i ograniczenia</h3>
<ul>
<li><strong>ULDK</strong> nie znajduje działki 61/6 (dane pobrano obejściem przez KIEG).</li>
<li><strong>szukajwarchiwach.gov.pl</strong> i <strong>opus4.kobv.de</strong> (Crossener Kreiskalender) — blokady antybotowe; roczniki 1913–1942 pozostają do przejrzenia ręcznie.</li>
<li>Brak zdjęcia samego obiektu przy Grobli 64 z lat 1945–2000 — jedyne współczesne materiały to ortofoto i makieta z ogłoszenia.</li>
<li>Nie ustaliłem, czy nieruchomość została sprzedana po 2022 r. (status ogłoszenia ≠ akt).</li>
</ul>

<footer>
<p><strong>Separacja twierdzeń:</strong> <span class="tag t-fakt">fakt</span> z podanym źródłem · <span class="tag t-wn">wniosek</span> interpretacja z porównania źródeł · <span class="tag t-hip">hipoteza</span> wymaga dowodu z akt · <span class="tag t-kor">korekta</span> zmiana wcześniejszego ustalenia.</p>
<p>Ilustracje H-01…H-03 to reprodukcje z PDF monografii udostępnionego przez autorkę; podano oryginalne podpisy niemieckie. Nie przypisuję im innej proweniencji, niż wskazana.</p>
<p>Etap III · 28 października 2026 · dokument roboczy kwerendy.</p>
</footer>
</div></body></html>"""

for i, r in enumerate(FIG, 1):
    HTML = HTML.replace('{{FIG%d}}' % i, r)
open(OUT, 'w', encoding='utf-8').write(HTML)
print(round(len(HTML) / 1e6, 2), 'MB', HTML.count('<figure'), 'figur')
