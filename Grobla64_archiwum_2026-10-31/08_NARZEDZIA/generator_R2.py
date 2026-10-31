import base64, io
from PIL import Image

OUT = '/home/user/report/Grobla64_laznia.html'
FIG = []


def img(path, w=820, q=82):
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


F_RED = fig('/home/user/work/dossier/w01_redbox.jpg', 'W-01', 'Zdjęcie wyjściowe — obiekt zaznaczony na zdjęciu lotniczym',
            'Landesarchiv NRW, RW 0229 Nr. 46002 (Hansa Luftbild), bez daty, ok. 1925–1932',
            'Dwie bryły w sadzie nad wodą: dom z kominem i duża hala o szerokim dachu. Po informacji, że obiekt był <strong>łaźnią</strong>, ten układ czyta się inaczej: dom obsługi/kąpielowego + hala niecki. Hala stoi dalej od wody, dom — przy ścieżce dojazdowej.',
            'archivportal-d.de, RW 0229 Nr. 46002')

F_ZOOM = fig('/home/user/work/dossier/d01_detail.jpg', 'W-02', 'Powiększenie obiektu z prostokąta (ok. ×6)',
             'wycinek z RW 0229 Nr. 46002',
             'Widoczne: komin przy domu (co sugeruje piec/kotłownię), jasny szczyt z okienkiem, przy hali — ciemna, jednolita połać bez świetlików. Brak czytelnych okien w części dachowej hali — typowe dla krytych niecek i hal basenowych, gdzie światło idzie przez górne okna ścian szczytowych.')

F_ORTHO = fig('/home/user/work/bad/fin/ortho_hi.jpg', 'D-01', 'Stan dzisiejszy — ortofoto całej posesji',
              'GUGiK ORTO HighResolution (WMS), 28.10.2026; kadr ok. 200 × 200 m',
              'Działka 61/6 to południowo-wschodni fragment kadru (za ulicą widoczne 55, 49/51). Hala stoi przy wale, plac na południe od niej jest wybetonowany — widoczne regularne pasy nawierzchni.')

F_HALL = fig('/home/user/work/bad/fin/hall_today.jpg', 'D-02', 'Hala dziś — powiększenie',
              'wycinek ortofoto GUGiK, ok. 45 × 55 m',
              'Dach dwuspadowy, dwie kalenice (dwie przyległe części), bez okien dachowych; elewacje kryte blachą/tynkiem. Na południe od hali — betonowy plac z pasami dylatacji. <strong>Ten plac to potencjalnie dawny taras niecek lub basen odkryty — do sprawdzenia w aktach, nie twierdzę tego jako faktu.</strong>')

F_SITE = fig('/home/user/work/bad/fin/site_plan.png', 'D-03', 'Plan sytuacyjny — obrysy budynków wokół posesji',
              'schemat własny z danych OpenStreetMap (footprints, 28.10.2026), skala 6 px = 1 m; północ u góry',
              'Grobla 64 (czerwony) = jeden budynek mieszkalny o obrysie 13,2 × 11,7 m i powierzchni zabudowy ok. 120 m² (dane OSM). Hala przy wale oznaczona jako osobny obrys bez numeru adresowego. Widoczne też sąsiednie posesje 55, 66, 70, 61, 63 — układ pozwala zorientować się w rozmieszczeniu hali względem domu.')

F_BAD = fig('/home/user/work/bad/fin/bad_full.jpg', 'B-01', '„Städt. Badeanstalt” — miejska łaźnia/kąpielisko, 1916',
             'pocztówka, 1916; karta polska-org nr 12376429 (skan 1640 × 1033 px)',
             'Jedyny znany mi widok podpisany wprost jako miejska łaźnia Crossen. Na pierwszym planie kąpiący się w rzece, w głębi lewy brzeg z zabudową mieszkalną, drzewami i <strong>mostkiem/pomostem</strong> oraz jasnymi, niskimi budynkami przy wodzie. Tło: wieża kościelna i kamienice starego miasta. Zastrzeżenie: pocztówka nie ma numeru posesji, a scena kąpieli jest plenerowa — nie jest to z pewnością zdjęcie wnętrza łaźni ani widok samej hali przy dzisiejszej Grobli 64.',
             'polska-org.pl/12376429,foto.html')

F_BADL = fig('/home/user/work/bad/fin/bad_left.jpg', 'B-02', 'Ten sam kadr — lewy brzeg, powiększenie',
              'wycinek B-01, ok. ×2,5',
              'Powiększenie pokazuje zabudowania przy wodzie: parterowe, jasne budynki z dachami dwuspadowymi, drewniany pomost oraz wyższy, ceglany budynek w głębi. To najbardziej „budynkowy” fragment tej pocztówki; wciąż nie ma podstaw, by wskazać w nim halę z działki 61/6.')

F_BADR = fig('/home/user/work/bad/fin/bad_right.jpg', 'B-03', 'Ten sam kadr — prawy brzeg i zabudowa w głębi',
              'wycinek B-01, ok. ×2,5',
              'Parterowa zabudowa z dachami dwuspadowymi i wysokie topole — typowy obraz nadwodnego przedmieścia. Materiał porównawczy dla bryły domu z W-02, nie identyfikacja.')

F_A33 = fig('/home/user/work/bad/aerial1933.jpg', 'A-01', '„Crossen a. d. Oder vom Flugzeug gesehen” — zdjęcie lotnicze, 1933',
             'pocztówka lotnicza, 1933; karta polska-org nr 7433072 (1300 × 911 px)',
             'Widok z samolotu od strony Odry na starówkę; u dołu kadru wschodni brzeg rzeki i zabudowa nadwodna. To zdjęcie obejmuje północny skraj opisywanego kwartału (okolice mostu i starego ujścia Bobru); <strong>działka 61/6 leży poza kadrem, na południe</strong>. Przydatne jako kontekst topograficzny, nie jako zdjęcie samej łaźni.')

F_CANAL = fig('/home/user/work/bad/fin/canal_amtsfischerei.jpg', 'H-01', '„Amtsfischerei mit Silberberg” — kanał rybacki z łodziami',
              'pocztówka kolorowana, reprodukcja w: B. Halicka, <em>Krosno Odrzańskie</em>, rozdz. 5',
              'Łodzie rybackie przy brzegu kanału, na prawym brzegu stelaż do suszenia sieci. To pass wodny bezpośrednio na północ od naszej działki. Pokazuje charakter wody, przy której stała łaźnia: spokojny kanał, nie Odra.')

CSS = """
:root{--ink:#15171c;--mut:#5b6270;--line:#dde1e8;--acc:#8c1c13;--bg:#f7f5f0}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.62 Georgia,'Times New Roman',serif}
.wrap{max-width:1040px;margin:0 auto;padding:0 22px 90px}
header{background:linear-gradient(160deg,#0f1216,#242c36);color:#fff;padding:50px 22px 38px;margin-bottom:30px;border-bottom:5px solid var(--acc)}
header .in{max-width:1040px;margin:0 auto}
.kicker{font:600 12px/1.4 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#e3bcb6}
h1{font:700 34px/1.15 Georgia,serif;margin:.35em 0 .2em}
header p{color:#c9cfd9;max-width:74ch}
h2{font:700 25px/1.2 Georgia,serif;margin:50px 0 6px;padding-bottom:8px;border-bottom:2px solid var(--ink)}
h3{font:700 19px/1.3 Georgia,serif;margin:28px 0 6px}
h4{font:700 16.5px/1.35 Georgia,serif;margin:0 0 4px}
p{margin:.55em 0}a{color:#7a1710}
.lead{font-size:17.5px;color:#2a2f38}
figure{margin:26px 0;background:#fff;border:1px solid var(--line);border-radius:6px;overflow:hidden}
figure img{display:block;width:100%;height:auto;background:#000}
figcaption{padding:14px 18px 16px}
.num{display:inline-block;font:700 11.5px/1 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.1em;color:#fff;background:var(--acc);padding:5px 8px;border-radius:3px;margin-right:9px;vertical-align:2px}
.meta{font:13px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut);margin:5px 0 8px}
.src{font:12.5px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;word-break:break-word}
table{width:100%;border-collapse:collapse;margin:16px 0;background:#fff;font:14.5px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;border:1px solid var(--line)}
th{background:#eceff4;text-align:left;padding:9px 11px;border-bottom:1px solid #cfd6e0}
td{padding:8px 11px;border-bottom:1px solid #eef1f5;vertical-align:top}
tr:last-child td{border-bottom:0}
.box{background:#fff;border:1px solid var(--line);border-left:5px solid var(--acc);border-radius:5px;padding:16px 20px;margin:22px 0}
.box.ok{border-left-color:#1d6b3f}.box.warn{border-left-color:#b06a00}
ul,ol{margin:.5em 0 .9em;padding-left:1.35em}li{margin:.32em 0}
.tag{display:inline-block;font:600 11px/1 -apple-system,Segoe UI,Roboto,sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border-radius:3px;margin-right:6px}
.t-fakt{background:#1d6b3f;color:#fff}.t-wn{background:#1f4e79;color:#fff}.t-hip{background:#8a5b00;color:#fff}.t-brak{background:#6b7280;color:#fff}.t-sprz{background:#8c1c13;color:#fff}
footer{margin-top:56px;padding-top:18px;border-top:1px solid var(--line);font:13px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;color:var(--mut)}
.sheet{background:#fff;border:1px solid var(--line);border-radius:6px;padding:10px;margin:22px 0}
@media(max-width:760px){h1{font-size:26px}}
"""

SVG = """
<div class="sheet">
<svg viewBox="0 0 900 620" width="100%" role="img" aria-label="Schemat funkcjonalny">
 <rect x="0" y="0" width="900" height="620" fill="#fff"/>
 <!-- plot -->
 <polygon points="60,70 780,50 800,540 70,560" fill="#f2efe7" stroke="#b9b2a2" stroke-width="2"/>
 <text x="80" y="95" font-family="Georgia" font-size="15" fill="#6b6558">działka 61/6 · 1 684 m² (Bi) · 309 m² zabudowy · 3 budynki</text>
 <!-- street -->
 <rect x="60" y="560" width="740" height="34" fill="#dcd6c8" stroke="#b9b2a2"/>
 <text x="70" y="583" font-family="Georgia" font-size="14" fill="#6b6558">ul. Grobla (dawna Westpromenade / Grabenstraße)</text>
 <!-- wal / water -->
 <polygon points="20,60 60,70 70,560 30,570" fill="#cfe0e6" stroke="#9fbcc6"/>
 <text x="12" y="300" font-family="Georgia" font-size="13" fill="#3d6673" transform="rotate(-88 30,300)">wał · kanał / starorzecze Odry</text>
 <!-- hall -->
 <rect x="180" y="150" width="150" height="230" fill="#e7cfc9" stroke="#8c1c13" stroke-width="2"/>
 <text x="196" y="180" font-family="Georgia" font-size="15" font-weight="bold" fill="#8c1c13">HALA</text>
 <text x="196" y="202" font-family="Georgia" font-size="12.5" fill="#5b5348">ok. 230 m² · dach dwuspadowy</text>
 <text x="196" y="220" font-family="Georgia" font-size="12.5" fill="#5b5348">2 przęsła · komin</text>
 <text x="196" y="250" font-family="Georgia" font-size="12" fill="#8c1c13">hipoteza: niecka + kotłownia</text>
 <text x="196" y="268" font-family="Georgia" font-size="12" fill="#8c1c13">w piwnicy / na parterze</text>
 <!-- house -->
 <rect x="360" y="230" width="130" height="120" fill="#d8e3d2" stroke="#1d6b3f" stroke-width="2"/>
 <text x="374" y="258" font-family="Georgia" font-size="15" font-weight="bold" fill="#1d6b3f">DOM</text>
 <text x="374" y="280" font-family="Georgia" font-size="12.5" fill="#4a5a45">13,2 × 11,7 m · ok. 120 m²</text>
 <text x="374" y="298" font-family="Georgia" font-size="12.5" fill="#4a5a45">adres: Grobla 64</text>
 <text x="374" y="322" font-family="Georgia" font-size="12" fill="#1d6b3f">hipoteza: kasa, mieszkanie</text>
 <text x="374" y="340" font-family="Georgia" font-size="12" fill="#1d6b3f">kąpielowego, magazyn</text>
 <!-- yard / basins -->
 <rect x="180" y="400" width="330" height="140" fill="#e6e6e2" stroke="#8b8b83" stroke-dasharray="6 5"/>
 <text x="196" y="428" font-family="Georgia" font-size="13.5" fill="#5b5348">plac betonowy z pasami dylatacji</text>
 <text x="196" y="450" font-family="Georgia" font-size="12.5" fill="#8b8b83">d. taras niecek / basen odkryty? — do sprawdzenia w aktach</text>
 <text x="196" y="472" font-family="Georgia" font-size="12.5" fill="#8b8b83">ew. ślady fundamentów po pomostach</text>
 <!-- third building -->
 <rect x="560" y="380" width="120" height="90" fill="#dcdcd6" stroke="#8b8b83"/>
 <text x="574" y="408" font-family="Georgia" font-size="13" fill="#5b5348">3. budynek</text>
 <text x="574" y="428" font-family="Georgia" font-size="12" fill="#8b8b83">zaplecze / szatnia?</text>
 <!-- entrance arrow -->
 <line x1="420" y1="560" x2="420" y2="360" stroke="#8c1c13" stroke-width="3" marker-end="url(#ar)"/>
 <defs><marker id="ar" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#8c1c13"/></marker></defs>
 <text x="430" y="540" font-family="Georgia" font-size="13" fill="#8c1c13">wejście od ulicy (hipoteza)</text>
 <!-- north -->
 <g transform="translate(840,80)"><path d="M0,-26 L9,10 L0,3 L-9,10 z" fill="#15171c"/><text x="-5" y="26" font-family="Georgia" font-size="14">N</text></g>
 <text x="60" y="612" font-family="-apple-system,Segoe UI" font-size="11.5" fill="#8b8b83">Schemat roboczy. Proporcje i rozmieszczenie brył wg ortofoto i OSM; podział funkcji wewnątrz — hipoteza typologiczna, nie inwentaryzacja.</text>
</svg>
</div>
"""

HTML = f"""<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grobla 64 (dz. 61/6) — łaźnia: materiał wizualny i rekonstrukcja</title>
<style>{CSS}</style></head><body>
<header><div class="in">
<div class="kicker">Kwerenda · etap IV · obiekt = łaźnia</div>
<h1>Grobla 64, dz. 61/6 — łaźnia miejska<br><span style="font-size:.6em;color:#c9cfd9">zdjęcia, widoki, schemat wnętrza i rozkład piwnic</span></h1>
<p>Nowa informacja — że częściowo stojący budynek był łaźnią — zmienia ciężar dowodów. Poniżej: co z tego wynika dla identyfikacji, komplet widoków przedwojennych, jakie udało się znaleźć, oraz uczciwa odpowiedź na pytanie o wnętrze i piwnice: co jest faktem, co rekonstrukcją typologiczną, a czego w sieci po prostu nie ma.</p>
</div></header>
<div class="wrap">

<div class="box ok">
<h3 style="margin-top:0"><span class="tag t-fakt">fakt</span>Trzy twarde punkty, które tę funkcję potwierdzają</h3>
<ol>
<li><strong>Księga branżowa 1938 r.</strong> notuje w Crossen pozycję: <em>„Heidenreich, Alfred — <strong>Badeanstalt</strong> — <strong>Grabenstraße</strong>”</em>. To <strong>jedyny</strong> wpis z hasłem „Badeanstalt” w całym mieście w tej księdze — i jedyny w ciągu ulicy, która dziś nazywa się Grobla (północ = Dammstraße, środek = Grabenstraße, południe = Westpromenade).</li>
<li><strong>Księga z 1913 r.</strong> notuje w tym samym kwartale zawód <em>„Bademeister”</em>: Sämisch Ernst, <em>Stadtgraben</em> oraz <em>Boberstr. 36</em> — czyli osoba obsługująca kąpielisko mieszkała nad wodą, przy której leży nasza działka.</li>
<li><strong>Słownik miast historycznych</strong> (Deutsches Städtebuch, hasło Crossen): <em>„1911: 1 Flussbadeanstalt”</em>, <em>„1928: 2 Bootshäuser, 1 Freiluftschwimmbad”</em> — a więc w mieście działała łaźnia rzeczna i kąpielisko na wolnym powietrzu, plus dwa domy łodziowe.</li>
</ol>
<p style="margin-bottom:0"><span class="tag t-brak">granica</span>Żaden z tych zapisów nie podaje numeru posesji. Powiązanie „Badeanstalt, Grabenstraße” z działką 61/6 opiera się na: (a) położeniu jedynego istniejącego do dziś obiektu kąpielowego w tym ciągu, (b) Państwa informacji, że budynek był łaźnią, (c) skali obiektu (hala + dom + plac). To mocna zbieżność, ale nadal zbieżność — dopóki nie ma aktu budowlanego albo zdjęcia z podpisem „Badeanstalt, Westpromenade”.</p>
</div>

<h2>1. Co dokładnie stoi na działce — i co z tego jest łaźnią</h2>
<table>
<thead><tr><th>Element</th><th>Dane</th><th>Interpretacja</th></tr></thead>
<tbody>
<tr><td>Działka 61/6</td><td>1 684 m², klasoużytek Bi, 309 m² powierzchni zabudowy, 3 budynki, własność gminna (grupa 5)</td><td>układ „obiekt użyteczności + zaplecze + plac”</td></tr>
<tr><td>Budynek adresowy (Grobla 64)</td><td>obrys 13,2 × 11,7 m, ok. 120 m², 1 kondygnacja w OSM</td><td>dom obsługi / kąpielowego, kasa, ewentualnie mieszkanie</td></tr>
<tr><td>Hala przy wale</td><td>dach dwuspadowy, dwie kalenice (dwa przęsła), ok. 230 m² zabudowy, bez okien dachowych</td><td><span class="tag t-hip">hipoteza</span>hala niecki — część, która „wciąż stoi”</td></tr>
<tr><td>Betonowy plac na południe od hali</td><td>regularne pasy nawierzchni widoczne na ortofoto</td><td><span class="tag t-hip">hipoteza</span>dawny taras niecek / basen odkryty; wymaga sprawdzenia w aktach</td></tr>
<tr><td>Trzeci budynek</td><td>obrys ok. 120 m² w głębi działki</td><td>szatnie, przebieralnie, magazyn opału</td></tr>
<tr><td>Funkcja dziś</td><td>zakład mechaniki/złomowania (Euro-Auto Rogowski) i wypożyczalnia łodzi wędkarskich</td><td>ciągłość funkcji „wodnej”: łodzie, woda, obsługa</td></tr>
</tbody></table>
{F_ORTHO}
{F_HALL}
{F_SITE}

<h2>2. Wnętrze i pomieszczenia — rekonstrukcja typologiczna</h2>
<div class="box warn">
<p style="margin:0"><span class="tag t-hip">hipoteza</span><strong>Nie mam zdjęcia ani rzutu wnętrza tej łaźni.</strong> Poniższy opis to model standardu miejskiej łaźni niemieckiej z lat 1900–1935, dopasowany do bryły i wielkości obiektu (hala ok. 230 m² + dom 120 m² + plac). Każdy punkt trzeba potwierdzić w aktach budowlanych — traktowanie tego jako inwentaryzacji byłoby nadużyciem.</p>
</div>
<table>
<thead><tr><th>Pomieszczenie (niemiecki odpowiednik)</th><th>Funkcja</th><th>Gdzie w bryle</th><th>Na co patrzeć w aktach</th></tr></thead>
<tbody>
<tr><td><strong>Badehalle / Schwimmhalle</strong></td><td>duża niecka, wannа dla pływających, górne okna w ścianach szczytowych</td><td>hala przy wale</td><td>rozpiętość dachu, ślady posadowienia niecki, dylatacje</td></tr>
<tr><td><strong>Wannenbäder I/II Klasse</strong></td><td>kabiny z wannami, często 6–12 sztuk, „klasa I” droższa</td><td>parter hali, wzdłuż ściany</td><td>podział na kabiny, wentylacja, kanalizacja</td></tr>
<tr><td><strong>Brausebäder</strong></td><td>prysznice zbiorowe (najtańsze, dla robotników)</td><td>parter / piwnica</td><td>liczba stanowisk, odpływy</td></tr>
<tr><td><strong>Dampfbad / russisches Bad</strong></td><td>łaźnia parowa</td><td>hala, przy kotłowni</td><td>komin, kanały dymowe</td></tr>
<tr><td><strong>Umkleidekabinen, Gemeinschaftsumkleide</strong></td><td>przebieralnie indywidualne i zbiorcza</td><td>dom lub dobudówka</td><td>szafki, wieszaki, liczby miejsc</td></tr>
<tr><td><strong>Kesselhaus + Brennstofflager</strong></td><td>kotłownia, skład węgla/drewna</td><td><strong>piwnica hali</strong>, przy kominie</td><td>typ kotła, pojemność, wysokość piwnicy</td></tr>
<tr><td><strong>Waschanstalt / Waschküche</strong></td><td>pralnia — w małych miastach często łączona z łaźnią</td><td>parter / piwnica</td><td>kotły do prania, balie, suszarnia</td></tr>
<tr><td><strong>Kasse + Wohnung des Bademeisters</strong></td><td>kasa przy wejściu, mieszkanie obsługi</td><td>dom przy ulicy</td><td>rozkład mieszkania, liczba izb</td></tr>
<tr><td><strong>Liegewiese, Steg, Umkleidekabinen (außen)</strong></td><td>część kąpielowa na wodzie: pomost, przebieralnie, ogrodzenie</td><td>od strony kanału</td><td>ślady pali/pomostu w dnie, fundamenty</td></tr>
<tr><td><strong>Desinfektionsrinne / Fußbad</strong></td><td>korytko dezynfekcyjne przy wejściu</td><td>wejście</td><td>posadzka, spadki</td></tr>
</tbody></table>
{SVG}

<h2>3. Piwnice — co da się powiedzieć, a czego nie ma</h2>
<div class="box">
<p><strong>Publicznie dostępne źródła nie zawierają rzutu piwnic tej łaźni.</strong> Mapa zasadnicza i EGiB pokazują wyłącznie obrys budynku; rzuty kondygnacji i piwnic są w:</p>
<ul>
<li><strong>aktach budowlanych</strong> (Bauakten) — oryginalne projekty z przekrojami i rzutem piwnic,</li>
<li><strong>inwentaryzacjach powykonawczych</strong> i dokumentacji technicznej budynku (Starostwo / zarządca),</li>
<li><strong>dokumentacji rewitalizacyjnej gminy</strong> z lat 2016–2019 (PFU i studium wykonalności dla ulic Grobla, Bobrowa, Pl. Prusa, Żeromskiego, Wodna, Rybaki — zamówione przez gminę).</li>
</ul>
<p style="margin-bottom:0"><strong>Typowy rozkład piwnic w łaźni tej skali (hipoteza):</strong> pod halą — kotłownia z kotłem i zasobnikiem wody, skład opału, kanał dymowy do komina, pomieszczenie filtrów/pomp, magazyn sprzętu; pod domem — piwnica gospodarcza, ziemniaczarka, czasem pralnia. Jeśli niecka była zagłębiona, jej dno z odpływem leży poniżej poziomu terenu i piwnica hali jest głębsza niż w typowym budynku gospodarczym — to najprostszy sposób sprawdzenia tezy „łaźnia” bez wchodzenia do środka: <strong>wysokość i układ piwnic pod halą</strong>.</p>
</div>

<h2>4. Wszystkie widoki przedwojenne, jakie udało się znaleźć</h2>
<p>Kwerenda objęła 1 247 zdjęć miasta na polska-org (pełny listing, wszystkie strony), 45 ilustracji z monografii Halickiej, 6 biuletynów Heimatkreis Crossen/Oder (PDF, 228 ilustracji z OCR), kartę miasta na Fotopolsce oraz wyszukiwania po hasłach „Badeanstalt”, „Flussbadeanstalt”, „Schwimmbad”, „łaźnia” w katalogach aukcyjnych. Wynik jest poniżej — z pełną informacją, czego w nim nie ma.</p>
{F_BAD}
{F_BADL}
{F_BADR}
{F_A33}
{F_CANAL}
{F_RED}
{F_ZOOM}
<table>
<thead><tr><th>Kategoria</th><th>Co jest</th><th>Czego nie ma</th></tr></thead>
<tbody>
<tr><td>Widok podpisany „Badeanstalt”</td><td>1 karta: B-01 (1916), z wody, scena kąpieli + zabudowania w tle</td><td>podpisu z numerem posesji; ujęcia samej hali</td></tr>
<tr><td>Lotnicze</td><td>A-01 (1933) — starówka, kwartał poza kadrem; RW 0229 Nr. 46002 (W-01) — nasz obiekt</td><td>nalotu obejmującego działkę 61/6 z ostrą rozdzielczością</td></tr>
<tr><td>Kanał / Rybaki</td><td>H-01 „Amtsfischerei mit Silberberg”, karty z etapu I–III</td><td>zdjęcia budynku łaźni od strony kanału</td></tr>
<tr><td><strong>Wnętrza</strong></td><td><strong>brak</strong></td><td>zdjęcia niecki, przebieralni, kotłowni — nie znalazłem ani jednego</td></tr>
<tr><td><strong>Rzuty / plany</strong></td><td>plany miasta 1893 i 1945 (układ ulic)</td><td>rzut przyziemia i piwnic budynku</td></tr>
<tr><td>Po 1945</td><td>zdjęcia „dolnego miasta”, powódź 2010, ortofoto</td><td>zdjęcia łaźni w okresie powojennym</td></tr>
</tbody></table>

<h2>5. Gdzie realnie są wnętrza i rzuty — kolejność działań</h2>
<ol>
<li><strong>Starostwo Powiatowe w Krośnie Odrzańskim — archiwum budowlane.</strong> Wniosek o udostępnienie <em>akt budowlanych budynku na dz. 61/6</em> (obręb 2): projekt pierwotny, rozbudowy, przekroje, rzut piwnic. To jedyne miejsce, gdzie takie rysunki mogą być w komplecie.</li>
<li><strong>Urząd Miasta Krosno Odrzańskie — Wydział Gospodarki Nieruchomościami.</strong> Wniosek o informację publiczną: PFU i studium wykonalności rewitalizacji dolnego miasta (2016) oraz akta dzierżawy/użytkowania wieczystego dz. 61/6. Dokumentacja rewitalizacyjna zwykle zawiera inwentaryzację z rzutami.</li>
<li><strong>Archiwum Państwowe w Zielonej Górze.</strong> Akta miasta Crossen (Bauakten, akta policji budowlanej) — pytać o zespół „Akta miasta Krosna Odrzańskiego” i o spuściznę po przedwojennych urzędach; oraz Starostwo Krośnieńskie 1945–1950 (przejęcia mienia, spisy budynków).</li>
<li><strong>Sąd Rejonowy — akta księgi wieczystej dz. 61/6.</strong> Ciąg właścicieli od 1945 r.; przy nieruchomościach poniemieckich w aktach leżą odpisy niemieckich Grundbuchblätter z nazwą ulicy i numerem posesji — to domknęłoby identyfikację.</li>
<li><strong>Zdjęcia wnętrz: kanał społecznościowy.</strong> Grupy <em>„Sentymentalne Krosno Odrzańskie”</em> i <em>„Krosno Odrzańskie oraz okolice dawniej”</em> (Paweł Widczak) oraz <em>Fotoarchiv des Stadtamtes Krosno Odrzańskie</em>. Prośba o zdjęcia łaźni/„basenu” przy Grobli, także z lat 1945–1990 — w albumach rodzinnych takie zdjęcia istnieją, ale nie są w żadnym katalogu.</li>
<li><strong>Landesarchiv NRW — RW 0229 Nr. 46002 i sąsiednie negatywy.</strong> Zamówienie odbitki w pełnej rozdzielczości i metadanych nalotu: bez tego nie da się porównać dachu hali sprzed wojny z dzisiejszym.</li>
<li><strong>Heimatkreis Crossen/Oder.</strong> Redakcja „Heimatgrüße” (roczniki 1950 i 1955 są w sieci jako skany) — warto napisać list do redakcji z prośbą o wspomnienia o łaźni; to środowisko pamięta miasto sprzed 1945 r.</li>
</ol>

<h2>6. Czego w tej turze nie znalazłem — bez owijania</h2>
<ul>
<li><strong>Żadnego zdjęcia wnętrza</strong> łaźni (niecka, przebieralnie, kotłownia) w dostępnych katalogach, bibliotekach cyfrowych, na aukcjach i w prasie cyfrowej.</li>
<li><strong>Żadnego rzutu</strong> budynku — ani przyziemia, ani piwnic; mapy i EGiB pokazują tylko obrys.</li>
<li><strong>Żadnego niemieckiego źródła, które łączy „Badeanstalt” z numerem posesji</strong> przy Westpromenade. Najbliżej jest wpis „Heidenreich, Badeanstalt, Grabenstraße” (1938) — bez numeru.</li>
<li>Kwerendy, które nie dały wyniku: szukajwarchiwach.gov.pl (blokada Incapsula), opus4.kobv.de (Crossener Kreiskalender — zapora antybotowa), zbc.uz.zgora.pl (wyszukiwarka zwraca tylko szkielet strony), deutsche-digitale-bibliothek.de (wyniki tylko przez JS), katalogi aukcyjne (brak ofert z hasłem „Badeanstalt Crossen”).</li>
</ul>

<footer>
<p><span class="tag t-fakt">fakt</span> ze wskazanym źródłem · <span class="tag t-wn">wniosek</span> interpretacja · <span class="tag t-hip">hipoteza</span> wymaga potwierdzenia w aktach · <span class="tag t-brak">brak</span> czego nie znalazłem.</p>
<p>Wszystkie ilustracje to reprodukcje z podanych kart i publikacji, w rozdzielczości ekranowej. Rysunek wnętrza (SVG) jest schematem autorskim, nie inwentaryzacją. Etap IV · 28 października 2026.</p>
</footer>
</div></body></html>"""

for i, r in enumerate(FIG, 1):
    HTML = HTML.replace('{{FIG%d}}' % i, r)
open(OUT, 'w', encoding='utf-8').write(HTML)
print(round(len(HTML) / 1e6, 2), 'MB', HTML.count('<figure'), 'figur')
