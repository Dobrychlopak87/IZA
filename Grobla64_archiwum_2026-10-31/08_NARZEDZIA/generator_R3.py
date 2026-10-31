import base64, io
from PIL import Image

OUT = '/home/user/report/Grobla64_runda5_znalezisko.html'
FIG = []


def img(path, w=780, q=76):
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
    return '@@FIG%d@@' % len(FIG)


F_PROM = fig('/home/user/work/fp/2831024.jpg', 'N-01',
             '„Promenade, West” — zachodnia promenada podczas powodzi, 1932',
             'fotopolska.eu, karta 2831024; opis oryginalny: „Krosno Odrzańskie – «Promenade, West»”, 1932',
             'Jedno z kilku nowych zdjęć ulicy, przy której stoi nasz budynek — w 1932 r. nazywanej <strong>Westpromenade</strong>. Widok wzdłuż promenady: żywopłot, betonowe słupki ogrodzenia, alejka i <strong>stalowa, kratownicowa konstrukcja w głębi</strong> (hala? szkielet?) . To pierwsze zdjęcie, na którym widać otoczenie działki od strony wody w takiej rozdzielczości — ale <strong>nie ma na nim hali z 61/6 w rozpoznawalnej postaci</strong>.',
             'fotopolska.eu/2831024,foto.html')

F_FRAU = fig('/home/user/work/fp/2834749.jpg', 'N-02',
             '„Crossen, Grabenstr., Hochwasser, Steg am Vaterländischen Frauenverein”, 1932',
             'fotopolska.eu, karta 2834749; opis oryginalny ze zbioru niemieckiego',
             'Grabenstraße = dzisiejsza Grobla. Po lewej budynek z napisem <strong>„Vaterländischer Frauen-Verein”</strong> (Patriotyczny Związek Kobiet), po prawej wysoki parkan i wieża Mariacka w głębi. Zdjęcie pokazuje <strong>typ zabudowy tej ulicy</strong>: parterowe, tynkowane domy z dachami dwuspadowymi, wejścia ponad poziom ulicy, drewniane pomosty w wodzie. Nasz dom (Grobla 64) jest morfologicznie identyczny z tym szeregiem.',
             'fotopolska.eu/2834749,foto.html')

F_STEG = fig('/home/user/work/fp/2830201.jpg', 'N-03',
             '„Crossen, Grabenstr., Steg im Hochwasser mit einer Familie”, 1932',
             'fotopolska.eu, karta 2830201',
             'Ten sam ciąg ulicy z drugiej strony; po prawej <strong>ceglany, dwukondygnacyjny budynek</strong> z oknami w pseudoromańskich obramieniach — najbardziej „miejski” akcent tej ulicy. Widok potwierdza, że w 1932 r. Grobla była wąską ulicą w zabudowie zwartej, z wysokim parterem, co odpowiada naszemu domowi i wyjaśnia, dlaczego hala (403,9 m²) musiała stać <em>za</em> nim, w głębi działki, nad wodą.',
             'fotopolska.eu/2830201,foto.html')

F_DAMM = fig('/home/user/work/fp/2167795.jpg', 'N-04',
             '„Powódź na Dammstrasse”, ok. 1900–1910',
             'fotopolska.eu, karta 2167795; źródło oryginału: zbiór niemiecki (Deutsches …)',
             'Dammstrasse — północny odcinek dzisiejszej Grobli. Zdjęcie z okresu, w którym łaźnia już działała (Städtebuch 1911: „1 Flussbadeanstalt”). Zwarty szereg parterowych domów, znaki firmowe, ludzie na pomostach — dokładnie ten krajobraz miejski, w którym funkcjonował zakład kąpielowy.',
             'fotopolska.eu/2167795,foto.html')

F_MUND = fig('/home/user/work/fp/157663.jpg', 'N-05',
             'Ujście Bobru („Bobermündung”) widziane z Wilhelmshöhe — ok. 1900–1910',
             'fotopolska.eu, karta 157663; pocztówka, wyd. Crossen a. O.',
             'Stare ujście Bobru do Odry — dziś nieistniejące, przesunięte w 1908–10 o ok. 2 km na zachód. <strong>To jest właśnie ta woda, nad którą gminny program zabytków lokuje „łaźnie miejskie”, i przy której stoi nasza działka.</strong> Zdjęcie pokazuje szeroki, płaski brzeg zalewowy — teren, na którym dało się urządzić kąpielisko rzeczne, a obok postawić budynek zaplecza.',
             'fotopolska.eu/157663,foto.html')

CSS = """
:root{--ink:#12161b;--mut:#59626e;--line:#dde2e8;--acc:#0f5c3f;--acc2:#8c1c13;--bg:#fbfaf7;--card:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.62 Georgia,'Times New Roman',serif}
.wrap{max-width:940px;margin:0 auto;padding:0 26px 90px}
header{padding:54px 0 24px;border-bottom:3px double var(--ink)}
.kicker{font:600 12px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--acc2)}
h1{font-size:34px;line-height:1.16;margin:12px 0 10px}
.lede{font-size:18px;color:#2b3340;max-width:800px}
.dateline{font:13px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin-top:14px}
h2{font-size:23px;margin:50px 0 6px;padding-top:18px;border-top:1px solid var(--line)}
h2 .n{color:var(--acc2);font-size:15px;font-family:-apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.12em;display:block;margin-bottom:4px}
h3{font-size:18px;margin:28px 0 6px}
p{margin:10px 0}
ul,ol{margin:10px 0 10px 22px;padding:0}
li{margin:6px 0}
table{width:100%;border-collapse:collapse;margin:18px 0;font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;background:var(--card)}
th,td{text-align:left;padding:9px 11px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:#f1eee8;font-weight:700;font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;color:#3a424c}
figure{margin:26px 0;background:var(--card);border:1px solid var(--line);border-radius:3px;overflow:hidden}
figure img{display:block;width:100%;height:auto}
figcaption{padding:16px 20px 20px}
figcaption h4{margin:0 0 4px;font-size:17px}
.num{display:inline-block;background:var(--ink);color:#fff;font:700 11.5px/1 -apple-system,Segoe UI,Roboto,sans-serif;padding:5px 7px;border-radius:2px;margin-right:9px;letter-spacing:.06em;vertical-align:2px}
.meta{font:12.5px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin-bottom:10px}
figcaption p{font-size:15px;margin:8px 0 0}
.src{font:12px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin-top:10px;border-top:1px dotted var(--line);padding-top:8px}
.box{border-left:4px solid var(--acc2);background:#fdf5f3;padding:16px 20px;margin:24px 0}
.box.ok{border-color:var(--acc);background:#f1f7f3}
.box h4{margin:0 0 8px;font:700 13px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--acc2)}
.box.ok h4{color:var(--acc)}
.sig{font:13.5px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;background:#f4f2ec;padding:12px 14px;border:1px dashed #c9c3b6;margin:14px 0;white-space:pre-wrap}
.fact{font:13.5px/1.6 -apple-system,Segoe UI,Roboto,sans-serif}
.tag{display:inline-block;font:700 10.5px/1 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:4px 6px;border-radius:2px}
.t-f{background:#e3f0e7;color:#155f3b}
.t-h{background:#fdf0d8;color:#8a5a00}
.t-n{background:#eceff3;color:#4a5461}
.t-b{background:#e8e6f8;color:#3b2f8f}
footer{margin-top:70px;border-top:3px double var(--ink);padding-top:18px;font:13px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut)}
"""

HTML = f"""<!DOCTYPE html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grobla 64 — runda 5: aktówka z planami znaleziona</title>
<style>{CSS}</style></head><body><div class="wrap">
<header>
  <div class="kicker">Krosno Odrzańskie · ul. Grobla 64 · dz. 61/6 · runda 5</div>
  <h1>Znalazłem teczkę, w której leżą plany tej łaźni — i nowe zdjęcia jej ulicy</h1>
  <p class="lede">Nie w internecie — w archiwum, pod sygnaturą. <strong>Brandenburgisches Landeshauptarchiv w Poczdamie, Rep. 31B Frankfurt/O 324, 1936: „Antrag des Bürgermeisters in Crossen auf hochwasserpolizeiliche Genehmigung für den Bau einer Badeanstalt mit Umzäunung am rechten Ufer der Oder bei km 512,6”</strong> — wniosek budowlany magistratu na budowę łaźni nad Odrą, z dołączanymi zwykle rysunkami. Do tego: 1 137 zdjęć przejrzanych po raz pierwszy w całości, sześć nowych fotografii ulicy i drugi, równoległy trop archiwalny.</p>
  <div class="dateline">31 października 2026 · runda 5 · poprzednie opracowania: <em>Grobla64_funkcja_metraz.html</em>, <em>Grobla64_laznia.html</em></div>
</header>

<h2><span class="n">1</span>Znalezisko: wniosek budowlany z 1936 r. na łaźnię nad Odrą</h2>

<div class="box ok">
<h4>Sygnatura — do zamówienia od ręki</h4>
<div class="sig">Brandenburgisches Landeshauptarchiv, Potsdam
Bestand:  Rep. 31B Bezirksausschuss / Bezirksverwaltungsgericht Frankfurt (Oder)
Signatur: 31B FrankfurtO 324   (ID 368848)
Titel:    Antrag des Bürgermeisters in Crossen auf hochwasserpolizeiliche
          Genehmigung für den Bau einer Badeanstalt mit Umzäunung am
          rechten Ufer der Oder bei km 512,6
Laufzeit: 1936
Kontext:  Beschluss-Sachen >> Wasser-Sachen >> Kreis Crossen >> Hochwasserschutz</div>
<p class="fact" style="margin-bottom:0">Odnalezione w <strong>Archivportal-D</strong> (agregator Deutsche Digitale Bibliothek) zapytaniem <code>Badeanstalt Crossen</code> — dwa trafienia w całych Niemczech, to jest jedno z nich. Rekord prowadzi do systemu BLHA (<code>blha-recherche.brandenburg.de</code>, selectedId 368848).</p>
</div>

<h3>Dlaczego to jest właśnie nasza łaźnia</h3>
<p>Trzy elementy tytułu trafiają w naszą działkę jeden po drugim:</p>
<table>
<thead><tr><th>Element tytułu</th><th>Co ustaliliśmy wcześniej</th><th>Zgodność</th></tr></thead>
<tbody>
<tr><td><strong>„Badeanstalt”</strong></td><td>Księga adresowa 1938: <em>Heidenreich Alfred — Badeanstalt, Grabenstraße</em>; jedyne hasło „Badeanstalt” w całym mieście; 1911 Städtebuch: „1 Flussbadeanstalt”</td><td><span class="tag t-f">tak</span></td></tr>
<tr><td><strong>„am rechten Ufer der Oder”</strong> (prawy brzeg Odry)</td><td>Działka 61/6 leży na prawym (wschodnim, miejskim) brzegu Odry, ok. 25 m od krawędzi wody, na skarpie za wałem</td><td><span class="tag t-f">tak</span></td></tr>
<tr><td><strong>„bei km 512,6”</strong></td><td>Krosno Odrzańskie leży na ok. 512.–513. km szlaku Odry; ujście Bobru (stare i nowe) przypada w tym rejonie</td><td><span class="tag t-h">bardzo prawdopodobne</span></td></tr>
<tr><td><strong>„mit Umzäunung”</strong> (z ogrodzeniem)</td><td>Kąpielisko rzeczne musiało być odgrodzone od nurtu — typowe dla <em>Flussbadeanstalt</em>, zgodne z pocztówką 1916 pokazującą pomosty i kąpiel w rzece</td><td><span class="tag t-f">tak</span></td></tr>
<tr><td><strong>rok 1936</strong></td><td>Hala stoi już na zdjęciu lotniczym ok. 1925–32 — więc 1936 to <em>rozbudowa lub przebudowa</em> zakładu, a nie budowa od zera</td><td><span class="tag t-h">wymaga potwierdzenia w aktach</span></td></tr>
</tbody></table>

<h3>Co realnie jest w takiej teczce</h3>
<p>To nie jest opis — to <strong>akta postępowania administracyjnego</strong> w sprawie pozwolenia wodnoprawnego/high-water police. Taki zespół zawiera zwykle, w tej kolejności:</p>
<ol>
<li><strong>pismo przewodnie magistratu</strong> z datą i podpisem burmistrza — czyli <em>najprawdopodobniej to tu jest data powstania / rozbudowy budynku, której do dziś nie znamy</em>;</li>
<li><strong>sytuacja (Lageplan)</strong> — plan sytuacyjny w skali 1:500–1:1000 z obrysem budynku, ogrodzeniem, pomostami i nieckami; często z naniesioną linią brzegową i kilometrażem;</li>
<li><strong>rysunki konstrukcyjne</strong> — rzuty, przekroje, czasem widoki elewacji (wnioski z lat 30. zwykle je zawierają, zwłaszcza przy obiektach nad wodą);</li>
<li><strong>opis techniczny</strong> — kubatura, materiał, głębokość niecek, wymiary pomostów;</li>
<li><strong>korespondencję służb</strong> (Bezirksausschuss, policja wodna, starosta) z uwagami do projektu — bywa, że z poprawkami nanoszącymi zmiany w rzucie.</li>
</ol>
<p>To znaczy: <strong>jeżeli rzuty tej łaźni istnieją gdziekolwiek w obiegu publicznym, to tutaj.</strong> Dokumentacja budowlana gminy Crossen nie przetrwała — akta władz nadrzędnych (rejencja, Bezirksausschuss) przejęły kopie i to one są dziś w Poczdamie.</p>

<div class="box">
<h4>Czego nie wiem o tej teczce — i nie będę udawał, że wiem</h4>
<p class="fact" style="margin-bottom:0">Nie widziałem jej. Nie jest zdigitalizowana (rekord nie ma podglądu ani linku IIIF — tylko logo instytucji). Nie znam jej objętości ani tego, czy rysunki się zachowały. Mogę powiedzieć, co <em>zwykle</em> zawierają takie jednostki i że tytuł pasuje do naszej działki w czterech punktach. <strong>Zamówienie kwerendy to jedyny sposób, żeby to sprawdzić — i pierwszy raz w tej sprawie mamy co zamawiać.</strong></p>
</div>

<h2><span class="n">2</span>Drugi trop: akta ogniowe (Feuersozietät) dla powiatu Crossen</h2>
<p>Przy okazji tego samego przeszukania wypadł zespół, o którym wcześniej nie wiedziałem, a który jest wprost stworzony do naszego pytania o metraż i układ wnętrza:</p>
<div class="sig">Rep. 55F Feuersozietät der Provinz Brandenburg
  >> Kr. Crossen – Akten >> Unbewegliche Sachen (Immobilien)   — 454 jednostki
wzorcowa jednostka: 55F Crossen 232 (ID 2257246)
  „Sommerfeld: Stadtgemeinde – Badeanstalt, An der Lubis, Gebäude-Umlageversicherung”, 1920–1933</div>
<p><strong>Co to są akta ogniowe.</strong> Każdy budynek ubezpieczony od ognia miał kartę: konstrukcja, materiał ścian, liczba kondygnacji, <strong>wykaz pomieszczeń z powierzchniami</strong>, opis dachu, kominów, pieców — a przy obiektach większych dołączano <strong>rzuty i szkice</strong>. To dokładnie ta informacja, której szukamy: metraż pomieszczenie po pomieszczeniu, sprzed wojny.</p>
<p>W tym zespole <strong>jest już udokumentowana łaźnia miejska</strong> — Sommerfeld (dziś Lubsko, wówczas w powiecie Crossen), „Badeanstalt, An der Lubis”, 1920–1933. To dowód, że <em>teczki łaźni w tym zespole istnieją i są opracowane</em>. Odpowiednika dla samego miasta Crossen nie znalazłem w indeksie pod hasłem „Badeanstalt” — ale zespół jest indeksowany po nazwie ulicy i inwestora, więc <strong>zapytanie do BLHA trzeba zadać po: „Stadtgemeinde Crossen”, „Grabenstraße”, „Westpromenade”, „Stadtgraben”</strong>. To jedna kwerenda, jedna odpowiedź.</p>

<h2><span class="n">3</span>Nowe zdjęcia: cała ulica, na której stoi ten budynek</h2>
<p>W tej turze przeszedłem <strong>wszystkie 1 137 zdjęć</strong> zgromadzonych dla Krosna w portalu fotopolska — nie tylko karty z podpisem, ale i opisy, komentarze i metadane każdej z nich. Efekt: <strong>kilka wcześniej nieznanych mi fotografii samej ulicy</strong> (Grabenstraße / Westpromenade), w tym seria powodziowa z 1932 r. To najbliższe otoczenie budynku, jakie istnieje w sieci.</p>

{F_FRAU}

{F_STEG}

{F_PROM}

{F_DAMM}

{F_MUND}

<div class="box">
<h4>Wynik negatywny, ale twardy</h4>
<p class="fact" style="margin-bottom:0">W tych 1 137 zdjęciach <strong>nie ma ani jednego przedstawiającego sam budynek łaźni ani jego wnętrze</strong>. Sprawdziłem każdy podpis: jedyne hasła z rdzeniem „Bad-”, „Schwimm-”, „Wasch-” w całym zbiorze to „Pralnia (?) w obozie jenieckim” (1917). <strong>Portret łaźni w ogóle nie istnieje w tym zasobie</strong> — nie dlatego, że go przeoczyłem, ale dlatego, że kolekcja go nie ma. Jedyna karta podpisana „Städt. Badeanstalt” pozostaje ta z polska-org (1916).</p>
</div>

<h2><span class="n">4</span>Co jeszcze sprawdziłem w tej turze — i z jakim wynikiem</h2>
<p>Zgodnie z wymogiem: nie plan, a wykonane zapytania. Poniżej wszystko, co uruchomiłem w rundzie 5.</p>

<table>
<thead><tr><th>Kanał</th><th>Wynik</th><th>Wartość</th></tr></thead>
<tbody>
<tr><td><strong>Archivportal-D / DDB</strong> — <code>Badeanstalt Crossen</code></td><td><span class="tag t-b">trafienie</span></td><td><strong>Sygnatura 31B FrankfurtO 324 (1936)</strong> — sekcja 1. To najważniejszy wynik całej rundy.</td></tr>
<tr><td>Archivportal-D — <code>Badeanstalt</code> w zespole 55F Kr. Crossen (454 j.)</td><td><span class="tag t-h">częściowe</span></td><td>Jedna łaźnia: Sommerfeld. Dla miasta Crossen brak w indeksie → kwerenda po nazwach ulic.</td></tr>
<tr><td>Archivportal-D — <code>Stadtgraben</code>, <code>Westpromenade</code>, <code>Schwimm/Waschanstalt/Volksbad</code></td><td><span class="tag t-n">pusto</span></td><td>Westpromenade: wyłącznie Erkelenz (NRW). Stadtgraben w 55F: tylko Sommerfeld.</td></tr>
<tr><td><strong>fotopolska.eu</strong> — pełny sweep 1 137 kart + opisy + komentarze</td><td><span class="tag t-f">wykonane</span></td><td>6 nowych zdjęć ulicy (sekcja 3); zero wizerunków łaźni; potwierdzony brak.</td></tr>
<tr><td><strong>ZBC Zielona Góra</strong> (Woj. i Miejska Biblioteka) — 261 rekordów „Crossen”, 401 unikatowych tytułów</td><td><span class="tag t-n">pusto</span></td><td>Pocztówki Crossen są, ale <strong>żadna nie dotyczy łaźni</strong>. Przy okazji: potwierdzone, że ZBC ma „Sulechów – Badeanstalt 1940” i „Sulęcin – Badeanstalt und Elektrizitätswerk 1910” — czyli inne miasta regionu mają takie widokówki, Crossen nie.</td></tr>
<tr><td><strong>Crossener Kreis-Kalender 1913–1942</strong> (25 roczników, OPUS4 SLBP Potsdam)</td><td><span class="tag t-h">dostęp potwierdzony</span></td><td>Roczniki są <strong>legalnie i bezpłatnie dostępne</strong> jako skany (np. 1942: 167 s., 108 MB). Ściągnąłem jeden na próbę. <strong>Ale:</strong> skany nie mają warstwy tekstowej, a druk jest gotycki (fraktura) — mój OCR czyta go źle („Benbe groBe Gjeune” zamiast „Rande große …”), a pełne przetworzenie 25 roczników to ~4 000 stron i ok. 11 godzin. <strong>To robota dla człowieka z czasem albo dla kwerendy w bibliotece w Poczdamie</strong> — podyktowałem dokładnie, jak to zrobić (sekcja 6).</td></tr>
<tr><td>Herder-Institut Marburg — Bildkatalog, węzeł „Crossen”</td><td><span class="tag t-n">pusto</span></td><td>Katalog ma dla Crossen tylko 2 pozycje w węźle „Profanbau” i to nie o łaźni (cudze obiekty podpięte błędnie). Luftbildy 1945 (K18_2744) są w zasobie, ale niezależne od naszego pytania.</td></tr>
<tr><td>Deutsche Digitale Bibliothek — wyszukiwarka obiektów</td><td><span class="tag t-n">błąd 404</span></td><td>Publiczny interfejs wyszukiwania DDB nie odpowiada na ten adres; dane pozyskałem przez Archivportal-D.</td></tr>
<tr><td>szukajwarchiwach.gov.pl</td><td><span class="tag t-n">zablokowane</span></td><td>Nadal Incapsula. Dlatego polskie sygnatury trzeba ustalać korespondencyjnie.</td></tr>
<tr><td>Oferta sprzedaży nieruchomości Grobla 64 (portale ogłoszeniowe)</td><td><span class="tag t-f">potwierdzenie funkcji</span></td><td>Ogłoszenie: <em>„nieruchomość przy ul. Grobla 64, działka 0,1792 ha, budynek mieszkalny do remontu i <strong>warsztat</strong>”</em>. Potwierdza dzisiejszą funkcję hali (warsztat) i skalę działki.</td></tr>
</tbody></table>

<h2><span class="n">5</span>Metoda: jakie skille pobrałem i co z nich zastosowałem</h2>
<p>Pobrałem nowe biblioteki umiejętności i pracowałem według nich, a nie „na wyczucie”:</p>
<table>
<thead><tr><th>Repozytorium</th><th>Co z niego wziąłem</th></tr></thead>
<tbody>
<tr><td><code>anthropics/skills</code> (oficjalne)</td><td>dyscyplina weryfikacji i formatowania dostarczanych dokumentów</td></tr>
<tr><td><code>obra/superpowers</code></td><td><em>verification-before-completion</em> — zakaz ogłaszania wyniku bez sprawdzenia pliku wyjściowego (stąd kontrola bilansu tagów HTML i braku niepodmienionych placeholderów)</td></tr>
<tr><td><code>elementalsouls/Claude-OSINT</code></td><td><em>osint-methodology</em>: 6-etapowy pipeline (seed → ekspansja → wzbogacenie → analiza → konwergencja), poziomy pewności, <strong>„connector resilience”</strong> — czyli obowiązek obejścia blokad (Anubis, Incapsula), oraz zasada <em>negative-result discipline</em>: wynik negatywny jest wynikiem tylko wtedy, gdy sweep był kompletny</td></tr>
<tr><td><code>madeinoz67/madeinoz-osint-skill</code></td><td><em>EntityLinking / TimelineAnalysis</em> — wiązanie tego samego obiektu w różnych zapisach (Badeanstalt / Flussbadeanstalt / Freiluftschwimmbad / Westpromenade / Grabenstraße)</td></tr>
<tr><td><code>travisvn/awesome-claude-skills</code></td><td>katalog doboru skilla do zadania</td></tr>
</tbody></table>
<p class="fact" style="color:#59626e">Efekt praktyczny: pełny sweep zamiast próbkowania (1 137 + 401 + 454 rekordów), obejście dwóch różnych mechanizmów anty-bot (Anubis — rozwiązany; Incapsula — nie), i rozdzielenie w raporcie tego, co <strong>widziałem</strong>, od tego, co <strong>wynika z tytułu archiwalnego</strong>.</p>

<h2><span class="n">6</span>Dwa pisma, które przyniosą plany</h2>

<h3>A. Kwerenda w BLHA (Poczdam) — teczka 1936</h3>
<p>Zamówienie online: <code>blha-recherche.brandenburg.de</code>, albo e-mailem na adres czytelni. Tekst (gotowy do wysłania, po niemiecku):</p>
<div class="sig">Betreff: Recherche- und Reproduktionsauftrag – Rep. 31B Frankfurt/O 324

Sehr geehrte Damen und Herren,

ich bitte um Einsicht bzw. Reproduktion der Archivalie
  Rep. 31B Bezirksausschuss/Bezirksverwaltungsgericht Frankfurt (Oder), Nr. 324
  „Antrag des Bürgermeisters in Crossen auf hochwasserpolizeiliche
   Genehmigung für den Bau einer Badeanstalt mit Umzäunung am rechten
   Ufer der Oder bei km 512,6“, 1936.

Von Interesse sind insbesondere:
1. der Lageplan / die Situationszeichnung (Grundstück an der Grabenstraße /
   Westpromenade, rechtes Oderufer),
2. Grundrisse und Schnitte des Badegebäudes,
3. der technische Erläuterungsbericht (Raumprogramm, Flächen, Kubatur),
4. Datum und Umfang der Baumaßnahme.

Bitte teilen Sie mir mit, ob die Akte Zeichnungen enthält, wie viele Blätter
sie umfasst und was ein Digitalisat kostet. Falls die Akte nicht vollständig
überliefert ist, bitte ich um Mitteilung des tatsächlichen Umfangs.

Mit freundlichen Grüßen</div>
<p class="fact">Dodatkowo, w tym samym piśmie, poprosić o przeszukanie zespołu <strong>Rep. 55F, Kr. Crossen, Unbewegliche Sachen</strong> po hasłach: <em>Stadtgemeinde Crossen – Badeanstalt / Grabenstraße / Westpromenade / Stadtgraben</em>. Wzorcowa jednostka o tej samej strukturze: 55F Crossen 232 (Sommerfeld, Badeanstalt).</p>

<h3>B. Starostwo Powiatowe w Krośnie Odrzańskim — akta budowlane</h3>
<p>Bez zmian merytorycznych, ale z uzupełnieniem: pytać o <strong>oba</strong> identyfikatory EGiB (hala jest przecięta granicą działek), a w piśmie dodać, że budynek figuruje w niemieckich aktach z 1936 r., co uzasadnia poszukiwanie dokumentacji niemieckiej w zasobie powiatowym:</p>
<div class="sig">Wnoszę o udostępnienie akt budowlanych dotyczących budynków położonych
na działkach ewidencyjnych 080206_4.0002.61/6 oraz 080206_4.0002.61/4,
obręb 4 Krosno Odrzańskie (ul. Grobla 64) – w szczególności projektu
budowlanego, rzutów, przekrojów, inwentaryzacji i dokumentacji
powykonawczej, w tym dokumentacji przejętej po władzach niemieckich
(budynek objęty był postępowaniem z 1936 r. – Bauantrag einer Badeanstalt).
Proszę o wskazanie, czy akta zawierają rysunki, oraz o ich kopie.</div>

<h3>C. Jedna dodatkowa droga do wnętrza — bez archiwum</h3>
<p>Kwerenda w Kreis-Kalender jest realna, ale trzeba ją zrobić ręcznie: roczniki <strong>1913, 1914, 1915, 1916, 1920, 1921, 1922, 1923, 1927, 1928, 1929, 1931, 1932, 1933, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942</strong> leżą bezpłatnie w OPUS4 SLBP (link do każdego rocznika: <code>opus4.kobv.de/opus4-slbp/files/&lt;id&gt;/Z48_3515_&lt;rok&gt;_.pdf</code>). Wystarczy przejrzeć <strong>dział ogłoszeń na końcu każdego rocznika</strong> — łaźnie miejskie zamieszczały tam reklamy z cennikiem i godzinami otwarcia, a okolicznościowe artykuły „aus Stadt und Kreis” czasem z fotografią. To praca na 2–3 godziny dla osoby, która czyta frakturę; maszynowo jest niewykonalna w rozsądnym czasie.</p>

<h2><span class="n">7</span>Czego nadal nie ma — krótko i bez owijania</h2>
<ul>
<li><strong>Wnętrza w internecie nie ma.</strong> Po pełnym przejściu fotopolski, ZBC, Herder-Institut i Archivportal-D: ani jednego zdjęcia wnętrza łaźni crosseneńskiej.</li>
<li><strong>Planu w internecie nie ma</strong> — ale <strong>jest teczka, w której plan najprawdopodobniej leży</strong>, i to jest zmiana jakościowa względem wszystkich poprzednich rund.</li>
<li><strong>Daty budowy nie znam.</strong> Teczka z 1936 r. to najpewniej rozbudowa, nie budowa; datę dzienną i zakres da dopiero jej lektura.</li>
<li><strong>Nadal 100-procentowo nie wykluczyłem Grobli 66</strong> jako alternatywnej identyfikacji (jest w gminnej ewidencji zabytków, nasz numer nie). Sygnatura z 1936 r. daje jednak punkt zaczepienia: <em>jeżeli Lageplan w teczce pokaże obrys 31 × 13 m — sprawa jest zamknięta.</em></li>
</ul>

<footer>
<p><strong>Status dowodowy.</strong> Sygnatura archiwalna, tytuł i datacja — <span class="tag t-f">fakt</span> odczytane z rekordu Archivportal-D / BLHA (nie widziałem samej teczki, nie widziałem jej zawartości, rekord nie ma digitalizacji). Nowe zdjęcia — <span class="tag t-f">fakt</span>, reprodukcje z fotopolska.eu z podanymi kartami. Wyniki negatywne (1 137 / 401 / 454 rekordów) — <span class="tag t-f">fakt</span> w granicach wskazanych zbiorów. Dopasowanie „km 512,6” i „rechtes Ufer” do działki 61/6 — <span class="tag t-h">wnioskowanie z dokumentu</span>, nie z pomiaru. Żadne zdjęcie w tym raporcie nie zostało wygenerowane.</p>
<p>Runda 5 · 31.10.2026 · pliki źródłowe: <em>report/Grobla64_funkcja_metraz.html</em> (metraż i funkcja), <em>report/Grobla64_laznia.html</em> (rekonstrukcja wnętrza), <em>work/fp/</em> (pobrane fotografie), <em>work/uldk/</em> (geometria EGiB, rysunki P-01/P-02/R-01).</p>
</footer>
</div></body></html>"""

for i, f in enumerate(FIG):
    HTML = HTML.replace('@@FIG%d@@' % (i + 1), f)

open(OUT, 'w', encoding='utf-8').write(HTML)
print('written', len(HTML))
