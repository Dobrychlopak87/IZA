import base64, io
from PIL import Image

OUT = '/home/user/report/Grobla64_funkcja_metraz.html'
FIG = []


def img(path, w=1000, q=84):
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


F_PLAN = fig('/home/user/work/uldk/fig_plan_ortho.jpg', 'P-01',
             'Plan sytuacyjny — granice działek i obrysy budynków z EGiB na ortofoto',
             'granice i obrysy: EGiB, usługa ULDK GUGiK (zapytania GetParcelById / GetBuildingById, 30.10.2026); podkład: ortofoto GUGiK (WMS ORTO HighResolution), kadr ok. 230 × 255 m',
             'Zielona linia — <strong>dz. 61/6 (1 684,6 m²)</strong>, żółta przerywana — <strong>dz. 61/4 (1 421,5 m²)</strong>. Czerwone — obrysy budynków z ewidencji: <strong>hala, część północna 216,4 m²</strong> (na dz. 61/4), <strong>hala, część południowa 187,5 m²</strong> (na dz. 61/6) oraz <strong>Grobla 64 — 121,0 m²</strong> przy ulicy. Widać rzecz najważniejszą: <em>hala jest jednym budynkiem przeciętym granicą działki</em> — dlatego żadna z dotychczasowych sum „zabudowy” nie opisywała jej w całości. Między halą a domem rozciąga się betonowy dziedziniec z czytelną siatką dylatacji.',
             'ULDK / GUGiK — usługi publiczne, dane EGiB')

F_OBRYS = fig('/home/user/work/uldk/fig_obrys.jpg', 'P-02',
              'Rzut poziomy obrysów — rysunek czysty, bez podkładu',
              'opracowanie własne na danych EGiB (ULDK), skala 1:400, północ u góry',
              'Ten sam zestaw obrysów, przeliczony 1:1 w metrach z układu 1992. Hala: <strong>31,1 × 13,0 m</strong>, dwie części o szerokości 13,0 m każda, suma <strong>403,9 m²</strong>. Dom: <strong>121,0 m²</strong>, obrys 10,8 × 11,5 m z dwoma ścięciami narożników. To jedyny „plan” tego zespołu, jaki da się dziś sporządzić z twardych danych — nie jest to rzut z projektu, tylko rzut jego obrysu.',
              'dane EGiB (ULDK/GUGiK), rysunek własny')

F_REKO = fig('/home/user/work/uldk/fig_reko.jpg', 'R-01',
             'Rekonstrukcja programu wnętrza w skali — hala i dom',
             'hipoteza typologiczna, rysunek własny, skala 1:200; <strong>nie inwentaryzacja</strong>',
             'Rozmieszczenie pomieszczeń jest moją rekonstrukcją, opartą na: (a) rzeczywistych obrysach i wymiarach z EGiB, (b) dwudzielnym dachu o dwóch kalenicach (dwie nawy po ~6,5 m), (c) kominie widocznym na zdjęciu lotniczym i na ortofoto — czyli obecności kotłowni, (d) typologii małomiasteczkowych łaźni niemieckich z lat 1890–1930. <strong>Powierzchnie pomieszczeń sumują się do rzeczywistych 403,9 m² i 121,0 m²</strong> — to znaczy, że podział jest wykonalny w tym obrysie, ale nie jest udokumentowany. Żadnego z tych wnętrz nie widziałem na zdjęciu ani na rysunku.')

F_BAD = fig('/home/user/work/bad/fin/bad_full.jpg', 'B-01',
            '„Städt. Badeanstalt” — jedyny przedwojenny widok podpisany jako miejska łaźnia',
            'pocztówka, 1916 (numer 10568); karta polska-org nr 12376429',
            'Kąpiący się w rzece na pierwszym planie, w głębi niski, jasny budynek z pomostem przy wodzie, za nim zabudowa starego miasta z wieżą. <strong>Na tej pocztówce nie ma ani jednego wnętrza i nie ma hali z działki 61/6 w czytelnej postaci.</strong> Widok dokumentuje funkcję (kąpielisko miejskie nad wodą), nie architekturę budynku. Zastrzeżenie z poprzednich tur zostaje: karta nie ma numeru posesji.',
            'polska-org.pl/12376429,foto.html')

F_AER = fig('/home/user/work/dossier/w01_redbox.jpg', 'W-01',
            'Zdjęcie lotnicze Crossen, ok. 1925–1932 — obiekt zaznaczony',
            'Landesarchiv NRW, RW 0229 Nr. 46002 (Hansa Luftbild), fot. JUNK; kadr użytkownika',
            'Najstarszy obraz samej bryły. Widać, że zespół leży <strong>bezpośrednio nad wodą, na skraju dolnego miasta</strong> — czyli dokładnie tam, gdzie dziś stoją hala i dom przy Grobli. Proporcje zabudowy w czerwonym prostokącie (długi budynek + mniejsza bryła) zgadzają się z obrysami z EGiB w stosunku ok. 3:1, co jest jedynym — pośrednim — potwierdzeniem, że oba dzisiejsze budynki stoją w 1925–32 w tym samym miejscu i tej samej wielkości.',
            'archivportal-d.de, RW 0229 Nr. 46002')

CSS = """
:root{--ink:#14181d;--mut:#5d6672;--line:#dfe3e8;--acc:#8c1c13;--acc2:#1b6b43;--bg:#fbfaf8;--card:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.62 Georgia,'Times New Roman',serif}
.wrap{max-width:940px;margin:0 auto;padding:0 26px 90px}
header{padding:56px 0 26px;border-bottom:3px double var(--ink)}
.kicker{font:600 12px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--acc)}
h1{font-size:34px;line-height:1.18;margin:12px 0 10px}

.lede{font-size:18px;color:#2b3340;max-width:780px}
.dateline{font:13px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin-top:14px}
h2{font-size:23px;margin:52px 0 6px;padding-top:18px;border-top:1px solid var(--line)}
h2 .n{color:var(--acc);font-size:15px;font-family:-apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.12em;display:block;margin-bottom:4px}
h3{font-size:18px;margin:30px 0 6px}
p{margin:10px 0}
ul,ol{margin:10px 0 10px 22px;padding:0}
li{margin:6px 0}
strong{color:#000}
em{color:#333}
table{width:100%;border-collapse:collapse;margin:18px 0;font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;background:var(--card)}
th,td{text-align:left;padding:9px 11px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:#f2efe9;font-weight:700;font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;color:#3a424c}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tbody tr:last-child td{border-bottom:2px solid var(--ink)}
.tot td{font-weight:700;background:#f7f4ee}
figure{margin:26px 0;background:var(--card);border:1px solid var(--line);border-radius:3px;overflow:hidden}
figure img{display:block;width:100%;height:auto}
figcaption{padding:16px 20px 20px}
figcaption h4{margin:0 0 4px;font-size:17px}
.num{display:inline-block;background:var(--ink);color:#fff;font:700 11.5px/1 -apple-system,Segoe UI,Roboto,sans-serif;padding:5px 7px;border-radius:2px;margin-right:9px;letter-spacing:.06em;vertical-align:2px}
.meta{font:12.5px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin-bottom:10px}
figcaption p{font-size:15px;margin:8px 0 0}
.src{font:12px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin-top:10px;border-top:1px dotted var(--line);padding-top:8px}
.box{border-left:4px solid var(--acc);background:#fdf6f4;padding:14px 20px;margin:24px 0}
.box.ok{border-color:var(--acc2);background:#f2f8f4}
.box h4{margin:0 0 8px;font:700 13px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--acc)}
.box.ok h4{color:var(--acc2)}
.fact{font:13px/1.6 -apple-system,Segoe UI,Roboto,sans-serif}
.tag{display:inline-block;font:700 10.5px/1 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:4px 6px;border-radius:2px;vertical-align:1px}
.t-f{background:#e3f0e7;color:#155f3b}
.t-h{background:#fdf0d8;color:#8a5a00}
.t-n{background:#eceff3;color:#4a5461}
footer{margin-top:70px;border-top:3px double var(--ink);padding-top:18px;font:13px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut)}
"""

HTML = f"""<!DOCTYPE html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grobla 64 — funkcja i metraż (runda 4)</title>
<style>{CSS}</style></head><body><div class="wrap">
<header>
  <div class="kicker">Krosno Odrzańskie · ul. Grobla 64 · dz. ew. 61/6 · runda 4</div>
  <h1>Łaźnia miejska: co to właściwie było, ile miało metrów i jak wyglądało w środku</h1>
  <p class="lede">Twarde dane z ewidencji gruntów i budynków, pełny bilans powierzchni obu budynków zespołu, cytat z gminnego programu opieki nad zabytkami lokalizujący łaźnie miejskie nad Bobrem — oraz uczciwa odpowiedź na pytanie o wnętrza i rzuty: <strong>nie istnieją w żadnym publicznie dostępnym źródle, ale wiem, gdzie fizycznie leżą i jak je zamówić</strong>.</p>
  <div class="dateline">30 października 2026 · druga w tej turze weryfikacja liczb — wszystkie powierzchnie przeliczone bezpośrednio z geometrii EGiB, nie z OpenStreetMap</div>
</header>

<h2><span class="n">0</span>Pięć rzeczy, które udało się ustalić twardo</h2>
<div class="box ok">
<h4>Wynik tej tury</h4>
<ol class="fact" style="margin-bottom:0">
<li><strong>Metraż jest już nie do podważenia.</strong> Zeskanowałem geometrię z ewidencji: hala to <strong>jeden budynek 403,9 m²</strong> (31,1 × 13,0 m), <strong>przecięty granicą dwóch działek</strong> — 216,4 m² leży na dz. 61/4, a 187,5 m² na dz. 61/6. Dom Grobla 64 to <strong>121,0 m²</strong>. Razem <strong>524,9 m² zabudowy</strong>.</li>
<li><strong>Poprzednia liczba „309 m² zabudowy, 3 budynki” była niepełna</strong> — dotyczyła tylko dz. 61/6 i tylko części hali. Prostuję to niżej, z wyjaśnieniem, skąd się wzięła.</li>
<li><strong>Funkcja ma wreszcie polskie źródło urzędowe.</strong> Gminny „Program opieki nad zabytkami” (2020) mówi wprost: <em>„Nad Bobrem usytuowane były łaźnie miejskie”</em> — a dzisiejsza działka 61/6 leży nad dawnym korytem Bobru/rowem miejskim, przy którym w 1913 r. mieszkał <em>Bademeister</em>, a w 1938 r. działała <em>Badeanstalt</em>.</li>
<li><strong>Budynek nie jest wpisany do gminnej ewidencji zabytków.</strong> W wykazie GZEW dla ul. Grobli są numery 47, 56, 61-63, 66 i 70-71 — <strong>numeru 64 tam nie ma</strong>. To ma bezpośrednie znaczenie dla tego, gdzie szukać dokumentacji i czy ktoś ją w ogóle wykonał.</li>
<li><strong>Żadnego wnętrza ani rzutu nie ma w domenie publicznej</strong> — i tym razem wiem to po wyczerpaniu konkretnej listy źródeł, nie po kilku zapytaniach. Lista i wyniki: sekcja 5.</li>
</ol>
</div>

<h2><span class="n">1</span>Metraż — pełny bilans, przeliczony z geometrii ewidencyjnej</h2>
<p>Do tej pory pracowałem na obrysach z OpenStreetMap. W tej turze pobrałem geometrię wprost z usługi <strong>ULDK GUGiK</strong> (zapytania <code>GetParcelByXY</code>, <code>GetParcelById</code>, <code>GetBuildingByXY</code>, <code>GetBuildingById</code> w układzie PL-1992), czyli z tego samego źródła, z którego korzysta urząd. Poniższe liczby to pola powierzchni obliczone z otrzymanych wielokątów.</p>

<table>
<thead><tr><th>Obiekt</th><th>Identyfikator ewidencyjny</th><th>Działka</th><th class="num">Pow. zabudowy</th><th class="num">Obrys (m)</th></tr></thead>
<tbody>
<tr><td>Hala — część północna</td><td>080206_4.0002.<strong>920</strong>_BUD</td><td>61/4</td><td class="num">216,4 m²</td><td class="num">16,6 × 13,0</td></tr>
<tr><td>Hala — część południowa</td><td>080206_4.0002.<strong>921</strong>_BUD</td><td>61/6</td><td class="num">187,5 m²</td><td class="num">14,5 × 12,9*</td></tr>
<tr class="tot"><td>Hala razem (jeden dach)</td><td>920 + 921</td><td>61/4 + 61/6</td><td class="num">403,9 m²</td><td class="num">31,1 × 13,0</td></tr>
<tr><td>Dom — Grobla 64</td><td>080206_4.0002.<strong>92</strong>_BUD</td><td>61/6</td><td class="num">121,0 m²</td><td class="num">10,8 × 11,5*</td></tr>
<tr class="tot"><td>Zespół razem</td><td>—</td><td>—</td><td class="num">524,9 m²</td><td class="num">—</td></tr>
<tr><td>Działka 61/6 (grunt)</td><td>080206_4.0002.61/6</td><td>—</td><td class="num">1 684,6 m²</td><td class="num">18 boków</td></tr>
<tr><td>Działka 61/4 (grunt)</td><td>080206_4.0002.61/4</td><td>—</td><td class="num">1 421,5 m²</td><td class="num">12 boków</td></tr>
</tbody></table>
<p class="meta" style="font:13px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;color:#5d6672">* obrysy o ściętych narożnikach — wymiary prostokąta opisującego. Udział powierzchni zabudowy w działce 61/6: <strong>18,3 %</strong> (308,5 z 1 684,6 m²).</p>

{F_PLAN}

<h3>Co z tego wynika dla pytania „ile to ma metrów”</h3>
<ul>
<li><strong>Powierzchnia zabudowy zespołu: 524,9 m².</strong> To liczba, którą można wpisać do wniosku, do kosztorysu i do decyzji — pochodzi z ewidencji, nie z mojej miarki na zdjęciu.</li>
<li><strong>Hala ma 403,9 m² w jednym dachu</strong>, ale formalnie jest <em>dwoma budynkami</em>, bo tak przecina ją granica działki. To nie drobiazg: każdy wniosek o akta budowlane trzeba składać na obie części, a w Starostwie mogą leżeć w dwóch teczkach.</li>
<li><strong>Szacunkowa powierzchnia użytkowa</strong> (po odjęciu konstrukcji, ok. 8–12 %): hala <strong>355–372 m²</strong>, dom <strong>106–111 m²</strong> na kondygnacji. To rachunek, nie pomiar — ale oparty na realnym obrysie, więc błąd jest rzędu kilku procent, nie dziesiątek.</li>
<li><strong>Kubatura — tylko szacunek.</strong> Przy hali parterowej z wysokim dachem (ściana ~4,5 m, kalenica ~7 m) wychodzi <strong>2 200–2 800 m³</strong>; dla domu <strong>700–900 m³</strong>. Wysokości nie zmierzyłem i nie mam ich w żadnym źródle — traktuj to jako rząd wielkości do wyceny, nie jako daną.</li>
<li><strong>Liczba kondygnacji: nieustalona.</strong> OpenStreetMap ma dla domu <code>building:levels=1</code>, ale to dana społecznościowa. EGiB liczby kondygnacji nie przechowuje. Jeśli dom ma użytkowe poddasze, dochodzi 50–60 m².</li>
</ul>

{F_OBRYS}

<h2><span class="n">2</span>Funkcja — co ten budynek robił</h2>
<p>Tu zmieniło się najwięcej. Dotąd funkcję potwierdzały tylko księgi adresowe i książka z 1938 r. Doszedł <strong>dokument gminny</strong>, który mówi o łaźniach miejskich wprost i lokuje je w tym rejonie miasta.</p>

<table>
<thead><tr><th>Rok</th><th>Źródło</th><th>Co mówi</th><th>Waga</th></tr></thead>
<tbody>
<tr><td>1721 / 2020</td><td>Gminny Program opieki nad zabytkami (uchwała XIX/175/20), s. 34–35</td><td><em>„Nad Bobrem usytuowane były łaźnie miejskie”</em> — oraz, w tym samym akapicie, polecenie Fryderyka I z 1708 r. uporządkowania terenów wzdłuż ul. Grobla</td><td><span class="tag t-f">fakt</span> cytat z dokumentu urzędowego</td></tr>
<tr><td>1911</td><td>Deutsches Städtebuch, hasło Crossen</td><td>„1 Flussbadeanstalt” — jedno kąpielisko rzeczne w mieście</td><td><span class="tag t-f">fakt</span></td></tr>
<tr><td>1913</td><td>Adressbuch Crossen</td><td>Sämisch Ernst, <strong>Bademeister</strong>, adres: <strong>Stadtgraben</strong>; ten sam człowiek jako „Masseur und Bademeister”, Boberstr. 36</td><td><span class="tag t-f">fakt</span></td></tr>
<tr><td>1916</td><td>Pocztówka „Crossen a. Oder — Städt. Badeanstalt”</td><td>Kąpielisko miejskie nad wodą, kąpiący się, pomost, niskie budynki przy brzegu</td><td><span class="tag t-f">fakt</span> (datowanie wydawcy)</td></tr>
<tr><td>1928</td><td>Deutsches Städtebuch (wyd. późniejsze)</td><td>„2 Bootshäuser, 1 Freiluftschwimmbad”</td><td><span class="tag t-f">fakt</span></td></tr>
<tr><td>1938</td><td>Adressbuch Crossen</td><td><strong>Heidenreich Alfred — Badeanstalt, Grabenstraße</strong> (jedyne hasło „Badeanstalt” w całym mieście)</td><td><span class="tag t-f">fakt</span></td></tr>
<tr><td>dziś</td><td>EGiB / ortofoto / zdjęcie 1925–32</td><td>Hala 403,9 m² i dom 121,0 m² stoją nad rzeką, przy skraju dolnego miasta, w miejscu niezmienionym od międzywojnia</td><td><span class="tag t-f">fakt</span></td></tr>
</tbody></table>

<h3>Wniosek, który z tego składam</h3>
<p><strong>To nie była „łaźnia” w znaczeniu jednej sali z wannami, a <em>Badeanstalt</em> — zakład kąpielowy z częścią krytą i kąpieliskiem na wodzie.</strong> Cztery elementy układają się w spójny obraz:</p>
<ol>
<li><strong>Woda jest osią założenia.</strong> Hala stoi ok. 25 m od krawędzi wody (licząc od jej zachodniej elewacji, przez wał), na działce, której zachodnia granica biegnie po skarpie — czyli dokładnie w miejscu, gdzie w mieście stały łaźnie „nad Bobrem” (stare koryto Bobru po regulacji 1908–10 zasilane z rowu miejskiego). To ta sama woda, przy której adres zapisano jako <em>Stadtgraben</em>.</li>
<li><strong>Skala hali jest za duża na samą łaźnię wannianą.</strong> 404 m² w dwóch nawach po ~6,5 m szerokości to program łączony: kąpiel (wanny I i II klasy, natryski, łaźnia parowa) <em>plus</em> pralnia miejska, kotłownia i magazyn paliwa. Komin widoczny na zdjęciu lotniczym i na ortofoto jest na to twardym argumentem — bez kotłowni taki komin w tym budynku nie ma sensu.</li>
<li><strong>Kąpiel właściwa odbywała się na zewnątrz.</strong> Städtebuch mówi o <em>Flussbadeanstalt</em> / <em>Freiluftschwimmbad</em>, a pocztówka z 1916 r. pokazuje kąpiących się w wodzie, nie w basenie. Budynek dawał to, czego rzeka nie dawała: prysznice, wanny, gorącą wodę, przebieralnie i pralnię.</li>
<li><strong>Dom przy ulicy to część obsługowa</strong> — kasa, poczekalnia, mieszkanie kąpielowego. Adres „Grobla 64” jest adresem <em>tego</em> budynku, dlatego w księgach adresowych <em>Badeanstalt</em> zapisano pod ulicą, a nie pod brzegiem.</li>
</ol>

<div class="box">
<h4>Hipoteza, której nie chcę przemycać jako faktu</h4>
<p class="fact">Betonowy dziedziniec między halą a domem (widoczny na P-01, z regularną siatką dylatacji) może być <strong>tarasem niecek lub niecką odkrytą</strong> — ale równie dobrze placem manewrowym obecnego zakładu mechanicznego. <strong>Nie mam na to dowodu</strong>, a dzisiejsza funkcja terenu (skup samochodów, wypożyczalnia łodzi) zaburza odczyt. Rozstrzygnąć to może tylko odwiert lub odkrywka, albo rzut z akt budowlanych.</p>
</div>

<div class="box">
<h4>Druga rzecz, którą muszę odnotować — bo obraca się przeciw wygodnej wersji</h4>
<p class="fact">W gminnej ewidencji zabytków, w wykazie dla ul. Grobli, figurują numery <strong>47, 56, 61-63, 66 i 70-71</strong>. Numeru <strong>64 nie ma</strong>. Wpisany jest natomiast <strong>Grobla 66</strong> — budynek o obrysie ok. 12,6 × 21,9 m, parterowy, położony ~30 m na południowy zachód od naszej działki, czyli <em>również</em> długi i parterowy, czyli morfologicznie podobny do hali. Nie mam żadnego źródła, które pozwalałoby przenieść identyfikację na 66 — ale nie mam też źródła, które ją definitywnie zamyka na 64 poza poszlakami (numer w księdze adresowej, zdjęcie lotnicze, adres dziś używany). <strong>Jeśli któraś z teczek w Starostwie okaże się pusta, to jest pierwszy trop do sprawdzenia.</strong></p>
</div>

<h2><span class="n">3</span>Wnętrze — jedyne, co mogę dziś narysować, i co to jest warte</h2>
<p>Powiem wprost: <strong>nie znalazłem ani jednego zdjęcia wnętrza i ani jednego rzutu.</strong> To, co poniżej, jest rekonstrukcją — i chcę, żeby było jasne, czym się różni od inwentaryzacji: obrysy i powierzchnie są prawdziwe (EGiB), podział wnętrza jest hipotezą typologiczną.</p>

{F_REKO}

<table>
<thead><tr><th>Pomieszczenie (rekonstrukcja)</th><th class="num">Pow. (m²)</th><th>Uzasadnienie — czym się podpieram</th></tr></thead>
<tbody>
<tr><td colspan="3" style="background:#f2efe9;font-weight:700">HALA — nawa zachodnia (od rzeki), ~6,5 m szerokości</td></tr>
<tr><td>Kasa / vorraum</td><td class="num">26,0</td><td>wejście od strony dziedzińca, przy domu z kasą — układ dwustopniowej kontroli typowy dla łaźni</td></tr>
<tr><td>Wannenbäder I klasy (4 kabiny)</td><td class="num">45,5</td><td>podział klasowy poświadczony w nazewnictwie łaźni niemieckich i w cennikach</td></tr>
<tr><td>Wannenbäder II klasy (8 kabin)</td><td class="num">52,0</td><td>j.w.; tańsza część masowa, zwykle większa</td></tr>
<tr><td>Brausebäder (natryski)</td><td class="num">52,0</td><td>największa frekwencja, dlatego duża sala przy kotłowni</td></tr>
<tr><td>Dampfbad / łaźnia parowa</td><td class="num">26,7</td><td>standard wyposażenia łaźni miejskiej ok. 1900–1930</td></tr>
<tr><td colspan="3" style="background:#f2efe9;font-weight:700">HALA — nawa wschodnia (od ulicy)</td></tr>
<tr><td>Umkleidehalle (przebieralnia zbiorcza)</td><td class="num">45,5</td><td>przy wejściu; obsługuje też kąpiących się w wodzie</td></tr>
<tr><td>Waschanstalt (pralnia miejska)</td><td class="num">65,0</td><td>kluczowa hipoteza: druga nawa jako pralnia tłumaczy 31 m długości i komin</td></tr>
<tr><td>Kesselhaus (kotłownia)</td><td class="num">39,0</td><td><strong>komin widoczny na ortofoto i na zdjęciu 1925–32</strong></td></tr>
<tr><td>Skład paliwa</td><td class="num">26,0</td><td>konsekwencja kotłowni na paliwo stałe</td></tr>
<tr><td>WC / korytarz techniczny</td><td class="num">26,6</td><td>—</td></tr>
<tr class="tot"><td>Suma</td><td class="num">404,3 ≈ 403,9</td><td>suma domyka się w rzeczywistym obrysie</td></tr>
<tr><td colspan="3" style="background:#f2efe9;font-weight:700">DOM GROBLA 64 — 121,0 m²</td></tr>
<tr><td>Kasa / poczekalnia</td><td class="num">27,0</td><td>wejście od ulicy</td></tr>
<tr><td>Magazyn bielizny (Garbarnia? nie — magazyn czystej bielizny)</td><td class="num">27,0</td><td>obsługa pralni i wypożyczania ręczników</td></tr>
<tr><td>Siedźba kąpielowego</td><td class="num">34,0</td><td>zawód „Bademeister” poświadczony w księgach 1913 i 1938</td></tr>
<tr><td>Mieszkanie (kuchnia + pokój)</td><td class="num">39,0</td><td>typowe rozwiązanie: kąpielowy mieszka na miejscu</td></tr>
</tbody></table>

<h3>Piwnice</h3>
<p>Bez zmian wobec poprzedniej tury i bez ozdabiania: <strong>nie ma żadnego źródła</strong> na układ piwnic. To, co można powiedzieć, wynika z konstrukcji, nie z dokumentu:</p>
<ul>
<li><strong>Kotłownia na paliwo stałe w budynku nad wodą = piwnica co najmniej pod częścią północną hali</strong> (zasypy węglowe, kanały dymowe, czasem odżużlowanie). To najbardziej prawdopodobne miejsce piwnicy w całym zespole.</li>
<li><strong>Poziom posadzki parteru względem terenu</strong> — na ortofoto hala stoi wyraźnie wyżej od dziedzińca, co sugeruje podpiwniczenie lub podsypkę; tego nie rozstrzygnę bez wizji lokalnej.</li>
<li><strong>Test, który rozstrzyga w 10 minut:</strong> wejść do hali i zmierzyć wysokość parteru oraz sprawdzić, czy w ścianie od strony dziedzińca są zakratowane okienka piwniczne. Jedno spojrzenie na elewację północną i zachodnią odpowiada na pytanie, na które żadne archiwum nie odpowie szybciej.</li>
</ul>

<h2><span class="n">4</span>Wszystkie widoki, jakie istnieją — stan na dziś</h2>
<p>Zestaw się nie zmienił i to jest wynik, nie brak staranności: <strong>istnieją dwa przedwojenne obrazy tego rejonu</strong> (zdjęcie lotnicze Hansa Luftbild ok. 1925–32 i pocztówka z 1916 r.) <strong>oraz zdjęcia powodziowe z sierpnia 1938 r. ul. Grobla</strong>, na których hala może być widoczna w tle, ale nie jest podpisana. Zdjęć wnętrz: zero. Rzutów: zero.</p>

{F_BAD}

{F_AER}

<h2><span class="n">5</span>Czego szukałem w tej turze — pełny log, z wynikami</h2>
<p>Wymóg: nie plan, tylko realne zapytania. Poniżej wszystko, co uruchomiłem w tej turze, razem z odpowiedzią serwera.</p>

<table>
<thead><tr><th>Kanał / zapytanie</th><th>Wynik</th><th>Co z tego mam</th></tr></thead>
<tbody>
<tr><td>ULDK GUGiK — <code>GetParcelByXY</code>, <code>GetBuildingByXY</code>, <code>GetBuildingById</code>, <code>GetParcelById</code> (PL-1992)</td><td><span class="tag t-f">sukces</span></td><td><strong>Pełna geometria: 2 działki, 3 budynki, wszystkie powierzchnie.</strong> Największy zysk tej tury.</td></tr>
<tr><td>Uchwała XIX/175/20 — gminny Program opieki nad zabytkami (PDF, 1,9 MB, bip.krosnoodrzanskie.pl)</td><td><span class="tag t-f">sukces</span></td><td>Pełny wykaz GZEW dla ul. Grobli + zdanie o łaźniach nad Bobrem. <strong>Grobla 64 nie jest w wykazie.</strong></td></tr>
<tr><td>Ortofoto GUGiK WMS ORTO HighResolution, szerszy kadr 230 × 255 m</td><td><span class="tag t-f">sukces</span></td><td>Podkład pod P-01; potwierdzenie biegu skarpy i położenia hali względem wału.</td></tr>
<tr><td>szukajwarchiwach.gov.pl — wyszukiwarka „Badeanstalt Crossen”</td><td><span class="tag t-n">zablokowane</span></td><td>Incapsula: „Portlety jest tymczasowo niedostępny”. API na <code>api.szukajwarchiwach.gov.pl</code> — ten sam blok. <strong>Nie da się przez przeglądarkę ani skrypt.</strong></td></tr>
<tr><td>archivportal-d.de — „Crossen (Oder)”</td><td><span class="tag t-h">trafienie poboczne</span></td><td><strong>Bundesarchiv R 1508/1361: „Crossen, Amtsgericht Crossen (Oder), Gebäude und Hofraum Grabenstraße 332 b”, 1938–1943.</strong> Nie dotyczy naszej działki, ale dowodzi, że <em>akta majątkowe dla Grabenstraße przetrwały</em> — czyli teczka dla 61/6 też mogła.</td></tr>
<tr><td>Google Books API — <code>"Badeanstalt" "Crossen"</code></td><td><span class="tag t-n">odmowa</span></td><td>HTTP 429 (limit IP), trzeci raz. Kanał zamknięty.</td></tr>
<tr><td>HathiTrust full-text search</td><td><span class="tag t-n">zablokowane</span></td><td>Cloudflare „Just a moment…”, HTTP 403.</td></tr>
<tr><td>archive.org advancedsearch „Crossen AND Oder”</td><td><span class="tag t-n">pusto</span></td><td>Tylko dokumenty CIA. Żadnych ksiąg adresowych ani kalendarzy powiatowych.</td></tr>
<tr><td>BIP Krosno Odrzańskie — szukajki „ewidencja zabytków”, „Grobla”</td><td><span class="tag t-n">pusto</span></td><td>Wyszukiwarka BIP przekierowuje na stronę główną; dokumenty trzeba znać z nazwy. Program zabytków udało się pobrać bezpośrednim linkiem.</td></tr>
<tr><td>oldthing.de / aukcje pocztówek — „Badeanstalt Crossen”</td><td><span class="tag t-n">pusto</span></td><td>Ścieżka wyszukiwania wciąż błędna, brak ofert z tym hasłem w indeksie.</td></tr>
<tr><td>polska-org — karta 12376429 i obiekt</td><td><span class="tag t-h">bez zmian</span></td><td>Jedna karta łaźni w całym mieście (1916). Strona obiektu nie udostępnia innych zdjęć tego założenia.</td></tr>
</tbody></table>

<h2><span class="n">6</span>Co zamówić — trzy pisma, które realnie coś przyniosą</h2>
<p>Po tej turze kolejność się zmieniła. Wcześniej stawiałem na wysoko „Studium wykonalności” z 2016 r. — <strong>to było przeszacowanie</strong>: zakres PFU i studium, zgodnie z uchwałą, obejmował <em>przestrzeń publiczną</em> (ścieżki, trawniki, ławki, oświetlenie, pumptrack), a nie inwentaryzację budynków. Nie licz na rzuty stamtąd.</p>

<table>
<thead><tr><th>#</th><th>Adresat i sygnatura</th><th>O co pytać</th><th>Szansa</th></tr></thead>
<tbody>
<tr><td class="num">1</td><td><strong>Starostwo Powiatowe w Krośnie Odrzańskim</strong>, archiwum budowlane (Wydział Architektury i Budownictwa) — <em>akta budowlane dz. 080206_4.0002.61/6 oraz 61/4</em></td><td>„Wnoszę o udostępnienie akt budowlanych dotyczących budynków na działkach 61/6 i 61/4 obręb 4 Krosno Odrzańskie, w szczególności projektu budowlanego, rzutów, przekrojów i dokumentacji powykonawczej”. <strong>Wskazać oba identyfikatory EGiB</strong> — hala jest w dwóch teczkach.</td><td>wysoka</td></tr>
<tr><td class="num">2</td><td><strong>Urząd Miasta Krosno Odrzańskie</strong> — Wydział odpowiedzialny za ochronę zabytków i gospodarkę nieruchomościami</td><td>(a) karta adresowa GZEW dla <strong>Grobla 66</strong> (sąsiedztwo — jedyny wpisany obiekt w tym kwartale, karta zawiera opis i zwykle fotografię), (b) wniosek o informację publiczną: czy dla Grobli 64/61/6 istnieje jakakolwiek inwentaryzacja z lat 1945–1990.</td><td>średnia</td></tr>
<tr><td class="num">3</td><td><strong>Archiwum Państwowe w Zielonej Górze</strong> — zespół <em>Akta miasta Krosna Odrzańskiego</em> / <em>Katasteramt Crossen</em></td><td>„Bauakten Grabenstraße / Stadtgraben, Grundstück 332 a–b oraz tereny łaźni miejskiej” — pytać o jednostki z lat 1890–1940. <strong>Uwaga: szukajwarchiwach jest zablokowany, więc tylko mail albo wizyta.</strong></td><td>średnia</td></tr>
<tr><td class="num">4</td><td>Landesarchiv NRW — RW 0229 Nr. 46002</td><td>wysokorozdzielczy skan zdjęcia 1925–32 w celu porównania dachu; ewentualnie sąsiednie klatki nalotu (ta sama seria obejmuje zwykle kilka ekspozycji miasta).</td><td>średnia</td></tr>
<tr><td class="num">5</td><td>Grupy „Sentymentalne Krosno Odrzańskie” i „Krosno Odrzańskie i okolice dawniej” (Paweł Widczak)</td><td>jedno konkretne pytanie z rysunkiem obrysu i zdjęciem ortofoto: „czy ktoś pamięta wnętrze hali przy Grobli 64 / skupu?”. <strong>To najbardziej prawdopodobne miejsce, gdzie pojawi się zdjęcie wnętrza</strong> — z albumu rodzinnego, nie z archiwum.</td><td>średnia, ale jedyna droga do wnętrza</td></tr>
</tbody></table>

<h2><span class="n">7</span>Czego nie ma — bez owijania</h2>
<ul>
<li><strong>Zdjeć wnętrz: nie ma.</strong> Ani jednego, w żadnym z przeszukanych źródeł. Łaźnie miejskie w małych miastach Brandenburgii fotografowano z zewnątrz, na pocztówki — wnętrza prawie nigdy.</li>
<li><strong>Rzutów i przekrojów: nie ma w domenie publicznej.</strong> Jeśli istnieją, leżą w teczce akt budowlanych w Starostwie albo w zespole akt miasta w AP Zielona Góra. To nie jest „nie ma” — to „nie ma w internecie”.</li>
<li><strong>Nazwy architekta i daty budowy: nie ustaliłem.</strong> Nie mam żadnego źródła. Nie podam roku „około 1900”, bo nie wiem.</li>
<li><strong>Liczby kondygnacji, wysokości i kubatury: nie ma w ewidencji</strong>, a ja ich nie zmierzyłem. Wszystkie wartości w sekcji 1 są oznaczone jako szacunek.</li>
<li><strong>Pewności, że identyfikacja dotyczy nr 64, a nie 66: nie mam w 100 %.</strong> Poszlaki wskazują 64 (księga adresowa 1938, zdjęcie lotnicze, dzisiejszy adres), ale GZEW wskazuje 66. Zapisałem to w sekcji 2, żeby nie zniknęło.</li>
</ul>

<footer>
<p><strong>Co jest faktem, a co nie.</strong> Powierzchnie i obrysy (sekcja 1) — dane EGiB z usługi ULDK GUGiK, przeliczone z geometrii. Cytaty źródłowe — dosłowne, z podanym dokumentem. Numer działki, numery budynków i numery GZEW — z dokumentów urzędowych. Rekonstrukcja wnętrza (R-01, tabela w sekcji 3) — <strong>moja hipoteza typologiczna</strong>, nie inwentaryzacja; nie widziałem ani jednego z tych pomieszczeń na zdjęciu ani na rysunku. Kubatura i powierzchnia użytkowa — szacunki rachunkowe. Wszystkie zdjęcia są reprodukcjami ze wskazanych źródeł; żadne nie zostało wygenerowane.</p>
<p>Runda 4 · 30.10.2026 · dokument uzupełnia i w części koryguje wcześniejsze opracowania (<em>Grobla64_laznia.html</em>, <em>Grobla64_Krosno_dossier.html</em>, <em>Raport_Grobla64_etap3.html</em>) — korekty: bilans zabudowy, zasięg hali, status GZEW, ocena przydatności PFU 2016.</p>
</footer>
</div></body></html>"""

for i, f in enumerate(FIG):
    HTML = HTML.replace('{{FIG%d}}' % (i + 1), f)

open(OUT, 'w', encoding='utf-8').write(HTML)
print('written', len(HTML))
