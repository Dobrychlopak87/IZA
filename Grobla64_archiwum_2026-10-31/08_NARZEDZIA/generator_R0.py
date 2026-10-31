import base64, os
DOS='/home/user/work/dossier'
def img(name):
    p=os.path.join(DOS,name+'.jpg')
    return "data:image/jpeg;base64,"+base64.b64encode(open(p,'rb').read()).decode()

def fig(name, num, title, meta, body, url):
    return f'''<figure>
<img src="{img(name)}" alt="">
<div class="fc">
<div class="fnum">{num}</div>
<h4>{title}</h4>
<div class="fmeta">{meta}</div>
<p>{body}</p>
<p class="flink"><a href="{url}">polska-org.pl — karta zdjęcia</a></p>
</div>
</figure>'''

def foto_id(i): return f"https://polska-org.pl/{i},foto.html"

A=[
('d10_6947940','F-01','Kanał rybacki — początek galerii: kanał i jego kładka','1890–1910 · skan: Petroniusz','Skan pocztówki pokazujący cały kanał wraz z nabrzeżami, łodziami i zabudową. Na polska-org ta karta jest kartą wprowadzającą do obiektu: opis obiektu podaje, że kanał łączył Bóbr z Odrą, biegł przez dzielnicę rybacką, służył do cumowania i naprawy łodzi, a nad nim przerzucona była kładka <em>Die Fischerbrücke</em>.', foto_id(6947940)),
('d11_7827719','F-02','Kanał — widok z mostku, w głębi miasto','1900–1902','Dwuczęściowa karta: po lewej panorama miasta z kościołem, po prawej kanał z łodziami i pomostami. Dobry materiał do rozpoznania sylwety miasta widzianej znad wody.', foto_id(7827719)),
('d12_7331531','F-03','„Fischerei" — przystań rybacka z pomostami','1900–1906 · Verlag Emil Koch','Podpis na karcie: <em>„Gruss aus Crossen a. Oder — Fischerei"</em>. Widok wzdłuż kanału: po obu stronach drewniane pomosty, łodzie, niewielkie budynki gospodarcze — to dokładnie ten typ zabudowy, który na badanym zdjęciu lotniczym tworzy ciemną połać dachową w czerwonym prostokącie.', foto_id(7331531)),
('d13_10683921','F-04','Przystań rybacka na kanale','1902','Kolejne ujęcie kanału w głąb, z wyraźnie widoczną drewnianą zabudową nabrzeża i łodziami.', foto_id(10683921)),
('d14_5204332','F-05','Przystań rybacka — kolorowana karta','1902–1905','Wersja kolorowana tego samego motywu; dobrze widać układ: woda, pomosty, domy z wysokimi dachami po prawej.', foto_id(5204332)),
('d15_4489950','F-06','Kanał o zachodzie słońca','1906','Nastrojowa karta z łodziami; w tle zabudowa dzielnicy rybackiej.', foto_id(4489950)),
('d16_10160851','F-07','Wejście do przystani rybackiej','1909 · skan: Alistair','Podpis karty: <em>„Wejście do dawnej przystani rybackiej na Odrze"</em>. Ważne, bo pokazuje <strong>wylot kanału</strong> — miejsce, w którym kanał łączył się z wodą otwartą; właśnie w takim punkcie stoi zaznaczony obiekt (blisko wody, na skraju zabudowy).', foto_id(10160851)),
('d17_6150525','F-08','Przystań na kanale — karta kolorowana','1910','Widok z mostku w głąb kanału; po lewej strony pomosty, po prawej wysoka zieleń.', foto_id(6150525)),
('d18_8262589','F-09','Przystań w ozdobnej ramie („Partie am Fischereigraben")','1910–1915','Karta w secesyjnej ramie z napisem <em>„Partie am Fischereigraben"</em>. Nazwa <strong>Fischereigraben</strong> jest tu kluczowa: to niemiecka nazwa kanału rybackiego, którą odnajdziemy potem na kartach z 1932 r.', foto_id(8262589)),
('d19_8319180','F-10','Przystań na kanale — ujęcie z góry','1910–1915','Karta kolorowana; widać układ pomostów i kilka łodzi.','https://polska-org.pl/8319180,foto.html'),
('d20_6590175','F-11','Kanał z łodziami, w głębi zabudowa','1910–1920','Pionowa karta; po lewej stronie wysoki, wąski budynek z drewnianą dobudówką — kandydat do porównania z bryłą z prostokąta.', foto_id(6590175)),
('d21_6154299','F-12','Kanał — ujęcie z mostku','1914','Klasyczne ujęcie wzdłuż osi kanału; łodzie przy obu brzegach.', foto_id(6154299)),
('d22_4494394','F-13','„Mała przystań rybacka"','1917','Podpis karty: <em>„Mała przystań rybacka na Odrze"</em>; łódź z wioślarzem, brzeg z drzewami.', foto_id(4494394)),
('d23_8604230','F-14','Wędkowanie na kanale','1920 · skan: foto-baron','Scena z wędkarzem; dobrze widoczna niska zabudowa i ogrody nad wodą.', foto_id(8604230)),
('d24_12282086','F-15','Przystań rybacka — fotografia (nie pocztówka)','1928 · skan: Zbigniew Franczukowski (bynio)','Najpóźniejsze ujęcie naziemne tej przystani przed wojną, bliskie czasowi powstania badanego zdjęcia lotniczego (ok. 1930–1931).', foto_id(12282086)),
('d25_5268195','F-16','„Crossen/Oder — Fischereigraben"','1932','Karta z 1932 r. z nadrukiem <em>„Crossen/Oder — Fischereigraben"</em>: kanał, łodzie, drewniane umocnienia brzegów, po lewej murowany budynek z wyciągiem, w głębi skarpa, biała willa i ogród. <strong>To najpóźniejsza karta z tej serii i najlepszy materiał porównawczy do zdjęcia lotniczego.</strong>', foto_id(5268195)),
]

B=[
('d30_4520844','B-01','„Bobermündung" — ujście Bobru','1901–1909 · Verlag Emil Koch','Szeroki widok na rozlewisko u ujścia Bobru; pierwszy plan zadrzewiony, w głębi miasto.', foto_id(4520844)),
('d31_4590604','B-02','„Bobermündung — Blick v. Wilhelmshöhe"','1901–1909','Ten sam motyw, co karta z Landesarchiv Baden-Württemberg (sygn. N 1/78 T 1 Nr. 193), ale w innym stanie i z innym podpisem. Warto mieć obie wersje: pokazują szerokość i kształt wody przed regulacją.', foto_id(4590604)),
('d32_5482205','B-03','Kładka nad starą Odrą (pierwotnym ujściem Bobru)','1906','Obiekt na polska-org nosi nazwę <strong>„Kładka (nie istnieje)"</strong>; w opisie: <em>„Kładka nad Starą Odrą (pierwotnym ujściem Bobru do Odry)… łączyła Stare Miasto z dawnym grodziskiem, na którym w XVIII wieku wzniesiono dwór Stary Raduszec (Vorwerk Klette), dzisiaj zrujnowany"</em>. Kładka widoczna jest też na planie z 1895 r. (podpis <em>Vorwerk Klette</em>) — to ona domyka topografię wody, nad którą stoi zaznaczony budynek.', foto_id(5482205)),
('d33_4542778','B-04','★ „Partie a. d. Bobermündung" — najważniejsza karta w tym dossier','1909–1910 · kolorowana','Na jednej karcie widać cały układ: <strong>Bóbr</strong> na pierwszym planie (nazwany odręcznie „Bóber"), <strong>długa drewniana kładka</strong>, piaszczysta łacha z białym budynkiem gospodarczym, a w głębi <strong>Odra</strong> (nazwana odręcznie „Oder!"). Po prawej stronie, na brzegu od strony miasta — <strong>zwarte skupisko zabudowy rybackiej: duży, jasny dom z wysokim dachem, czerwone dachówki, szalowane domki, ogrody</strong>. To niemal dokładnie ta konfiguracja, którą widzimy na badanym zdjęciu lotniczym: woda na pierwszym planie, skarpa z ogrodami, zabudowa na krawędzi.', foto_id(4542778)),
('d34_5019030','B-05','Ujście Bobru — drugie ujęcie tego samego skupiska','1909–1910','Wersja kolorowana z innego punktu: widok od strony miasta na wodę i łachę; zabudowa rybacka po prawej.', foto_id(5019030)),
('d35_5294124','B-06','Widok na Odrę i miasto znad ujścia Bobru','1913–1916','Panorama: rzeka, miasto, wieża kościoła mariackiego. Pokazuje, jak wyglądał brzeg od strony wody.', foto_id(5294124)),
('d36_6088893','B-07','„Gesamtansicht von Nordwesten"','1913–1916','Panorama ogólna od północnego zachodu — orientacja w układzie miasta wobec wody.', foto_id(6088893)),
('d37_10694063','B-08','Fragment miasta i ujście Bobru','1918','Ujęcie łączące zabudowę i ujście; przydatne do rozpoznania, które dachy należą do dzielnicy rybackiej.', foto_id(10694063)),
('d38_6847209','B-09','Widok na Odrę i fragment miasta','1935','Karta z 1935 r. — <strong>po</strong> wybudowaniu nowego ujścia Bobru (kanał do elektrowni Stary Raduszec, połowa lat 30.): pozwala rozdzielić to, co na zdjęciu z ok. 1930 r. jeszcze istniało, od tego, co zmieniono.', foto_id(6847209)),
('d39_8426432','B-10','Powódź 1938 — panorama','1938 · skan: maras','Powódź z sierpnia 1938 r. na tym samym odcinku wody; pozwala ocenić zasięg zalewania terasy nadrzecznej, na której stoją opisywane domy.', foto_id(8426432)),
]

C=[
('d40_6385294','S-01','Kanał Odry z mostem Elizy','1900','Stalowy most kratownicowy (Elisenbrücke) nad wodą; obok zabudowa i statek. Most był w ciągu dzisiejszej ul. Bohaterów Wojska Polskiego.', foto_id(6385294)),
('d41_6856488','S-02','Kanał Odry — widok z mostu w stronę miasta','1908','W opisie obiektu: rzeka Otok to <strong>stare koryto Odry, dawniej Stadt-Graben</strong>, otaczające miasto od wschodu, południa i zachodu; w końcowym odcinku znajdowało się pierwotne ujście Bobru.', foto_id(6856488)),
('d42_4543741','S-03','Most Elizy na kanale','1910–1920','W opisie: most nad rzeką Otok (dawniej Stadt-Graben), w ciągu ul. Bohaterów Wojska Polskiego.', foto_id(4543741)),
('d43_4330386','S-04','★ „Stadtgraben" — widok z małej przystani przy fosie miejskiej','1915–1918','Karta z obiegu 1918 r. Widok z przystani na wodę: łodzie na pierwszym planie, po lewej <strong>duży, jasny dom z wysokim dachem, częściowo przesłonięty drzewami</strong>, w głębi miasto z wieżą. Konfiguracja zbliżona do kadru z prostokąta: dom nad wodą, drzewa, ścieżka.', foto_id(4330386)),
('d44_6028922','S-05','„Partie a. d. Elisenbrücke"','1915–1925','Most kratownicowy z bliska; widoczna skarpa i zieleń.', foto_id(6028922)),
('d45_12376429','S-06','★ Miejskie kąpielisko („Städt. Badeanstalt")','1916','Podpis karty: <em>„Crossen a. Oder — Städt. Badeanstalt"</em>: kąpiący się w płytkiej wodzie, za nimi miasto z wieżą mariacką. Potwierdza, że ta woda była użytkowana rekreacyjnie i że jej brzegi były zagospodarowane (pomosty, przebieralnie).', foto_id(12376429)),
('d46_4330405','S-07','„Partie am Jordan mit Mädchen-Volksschule"','1918–1924','Szkoła żeńska nad wodą (dziś Szkoła Podstawowa przy ul. Bohaterów Wojska Polskiego) — <strong>duży, dwukondygnacyjny gmach z ryzalitem i wieżyczkami</strong>. To dobry materiał do rozpoznania wielkiego, jasnego budynku widocznego na zdjęciu lotniczym tuż za obiektem z prostokąta.', foto_id(4330405)),
('d47_11098058','S-08','Fragment miasta od strony wody','1935–1940','Najpóźniejsze ujęcie z tej grupy; pokazuje stan zabudowy w ostatnich latach przed zniszczeniem.', foto_id(11098058)),
]

D=[
('d50_5120441','L-01','★ „Crossen / O. — Orig.-Fliegeraufnahme 76423"','1930–1940 (karta: 1930/33)','Najostrzejsze zdjęcie lotnicze tego rejonu, jakie znalazłem — z tej samej epoki i prawdopodobnie z tej samej serii nalotów, co fotografia z Landesarchiv NRW. Widać skarpę, ogrody, nabrzeże i <strong>dach po dachu</strong> całą krawędź zabudowy od strony wody, z mostkiem kratownicowym w kadrze. To na tym zdjęciu najłatwiej odnaleźć bryłę z czerwonego prostokąta.', foto_id(5120441)),
('d51_5041421','L-02','Zdjęcie lotnicze — ujęcie z przeciwnej strony wody','1930–1942','Szerszy plan: cała dzielnica nadwodna, bieg rzeki, łachy.','https://polska-org.pl/5041421,foto.html'),
('d52_6589210','L-03','„Crossen a. Oder. Fliegeraufnahme"','1935','Panorama od strony wody z 1935 r.: pozwala sprawdzić, czy obiekt z prostokąta jeszcze stoi (a jeśli tak — gdzie dokładnie).', foto_id(6589210)),
('d53_5793399','L-04','„Crossen a. Oder. Fliegeraufnahme"','1932','Bardzo szeroki plan z dużym fragmentem doliny — do orientacji w hydrografii (Otok, stare ujście Bobru, łachy).', foto_id(5793399)),
('d54_5129282','L-05','Zdjęcie lotnicze z mostem','1935–1940','W kadrze most na Odrze i zabudowa nadbrzeżna — pomocne przy dopasowaniu osi kadru naszego zdjęcia.', foto_id(5129282)),
('d55_7433072','L-06','„Crossen a. Oder — vom Flugzeug gesehen" (Rynek)','1933','Rynek z kościołem mariackim z lotu ptaka — skala porównawcza dla czytania dachów na naszym zdjęciu.', foto_id(7433072)),
]

E=[
('d61_10860234','E-01','★ „Crossen a. O. — Am Fischerhäuschen"','1930','Karta pocztowa: <strong>kryta strzechą chata rybacka</strong> z białym kozłem, gęsiami i stosem drewna, wśród drzew. Podpis <em>„Am Fischerhäuschen"</em> („przy chatce rybaka") oznacza konkretne miejsce w dzielnicy rybackiej. Karta krążyła w obiegu w tym samym roku, w którym powstało badane zdjęcie lotnicze. <em>Źródło karty według polska-org: Deutsche Digitale Bibliothek.</em>', foto_id(10860234)),
('d62_4695401','E-02','Fischerstrasse podczas powodzi, 1903','1903','Zalana <strong>Fischerstraße (dziś ul. Bobrowa)</strong> — ulica dzielnicy rybackiej. Pokazuje, jak nisko położona była ta część miasta i dlaczego zabudowa nad wodą miała charakter ogrodowo-rybacki, a nie pierzejowy.', foto_id(4695401)),
('d60_6957922','E-03','Dolne miasto dzisiaj: ul. Bobrowa i pl. Bolesława Prusa','sierpień 2017 · fot. Petroniusz','Współczesne zdjęcie tej samej dzielnicy: <em>„Na pierwszym planie widać ulicę Bobrową, w prawo dochodzi do niej ul. Stefana Żeromskiego, teren zielony za krzakami po prawej to plac Bolesława Prusa"</em>. Kanału już nie ma; z przedwojennej zabudowy nadwodnej pozostały pojedyncze domy i zieleń.', foto_id(6957922)),
]

def gallery(items):
    out=[]
    for name,num,title,meta,body,url in items:
        out.append(fig(name,num,title,meta,body,url))
    return "\n".join(out)

HTML=f"""<!DOCTYPE html>
<html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dossier: zaznaczony budynek — dzielnica rybacka Crossen (Krosno Odrzańskie)</title>
<style>
:root{{--ink:#1a1b1d;--mut:#5b636f;--line:#d7dbe1;--acc:#8c1d18;--bg:#fbfaf7}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:Georgia,"Times New Roman",serif;line-height:1.6;font-size:16.5px}}
.wrap{{max-width:1040px;margin:0 auto;padding:32px 20px 90px}}
header.top{{border-bottom:3px double var(--acc);padding-bottom:16px;margin-bottom:22px}}
h1{{font-size:29px;line-height:1.22;margin:0 0 10px}}
.sub{{color:var(--mut);font-style:italic;margin:0}}
.meta{{font-family:system-ui,Segoe UI,Arial,sans-serif;font-size:13px;color:var(--mut);margin-top:10px}}
h2{{font-size:22px;margin:44px 0 8px;padding-bottom:6px;border-bottom:1px solid var(--line)}}
h3{{font-size:18px;margin:26px 0 6px}}
p{{margin:.6em 0}}
a{{color:#12457a;text-decoration:none;border-bottom:1px solid #b9cbe0}}
a:hover{{background:#eef4fa}}
code{{font-family:ui-monospace,Consolas,monospace;font-size:.88em;background:#f0efe9;padding:1px 4px;border-radius:3px}}
.box{{background:#fff;border:1px solid var(--line);border-radius:6px;padding:15px 18px;margin:16px 0}}
.box.acc{{border-left:5px solid var(--acc);background:#fdf6f5}}
.box.warn{{border-left:5px solid #b8860b;background:#fffdf5}}
.tag{{display:inline-block;font-family:system-ui,Arial,sans-serif;font-size:10.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 7px;border-radius:10px;margin-right:5px}}
.t-fact{{background:#e6f0e8;color:#255b30;border:1px solid #bfd6c5}}
.t-conc{{background:#e8eef7;color:#1d4a7a;border:1px solid #c2d2e8}}
.t-hyp{{background:#fdf0e2;color:#8a5010;border:1px solid #eed3b3}}
.t-no{{background:#f6e6e6;color:#7d2020;border:1px solid #e2c2c2}}
figure{{margin:0 0 22px;background:#fff;border:1px solid var(--line);border-radius:6px;padding:12px;display:grid;grid-template-columns:340px 1fr;gap:16px}}
figure img{{width:100%;height:auto;display:block;border-radius:3px;align-self:start}}
@media(max-width:800px){{figure{{grid-template-columns:1fr}}}}
.fc h4{{margin:2px 0 4px;font-family:system-ui,Segoe UI,Arial,sans-serif;font-size:16px;line-height:1.3}}
.fnum{{font-family:system-ui,Arial,sans-serif;font-size:11.5px;letter-spacing:.08em;color:var(--acc);font-weight:700}}
.fmeta{{font-family:system-ui,Arial,sans-serif;font-size:12.5px;color:var(--mut);margin-bottom:6px}}
.fc p{{font-size:15px;margin:.45em 0}}
.flink{{font-family:system-ui,Arial,sans-serif;font-size:12.5px}}
table{{width:100%;border-collapse:collapse;margin:14px 0;font-family:system-ui,Segoe UI,Arial,sans-serif;font-size:13.5px}}
th,td{{border:1px solid var(--line);padding:7px 9px;vertical-align:top;text-align:left}}
th{{background:#f1f0ea}}
tbody tr:nth-child(even){{background:#fcfcfa}}
.small{{font-size:13.5px;color:var(--mut)}}
ul,ol{{margin:.5em 0 .9em 1.2em;padding-left:.2em}}
li{{margin:.28em 0}}
</style></head><body><div class="wrap">

<header class="top">
<h1>Zaznaczony budynek — dossier źródeł do jednego obiektu<br><span style="font-size:20px;font-weight:normal">Crossen an der Oder / Krosno Odrzańskie: nadwodna dzielnica rybacka (Fischerei, Stadtgraben, stare ujście Bobru)</span></h1>
<p class="sub">40 materiałów źródłowych dotyczących wyłącznie tego kwartału i stojącej w nim zabudowy — z datowaniem, podpisami, linkami i oceną przydatności</p>
<p class="meta">Uzupełnienie do raportu z 28.10.2026 · kwerenda: polska-org (karty obiektów i zdjęć), Landesarchiv NRW, DDB, aukcje i zbiory prywatne</p>
</header>

<div class="box acc">
<h3 style="margin-top:0">Co zmieniło się w stosunku do pierwszego raportu</h3>
<p><span class="tag t-fact">fakt</span> Obiekt z czerwonego prostokąta stoi w <strong>nadwodnej dzielnicy rybackiej</strong> Crossen, nad <strong>Starą Odrą / Otokiem (niem. <em>Stadt-Graben</em>)</strong> przy starym ujściu Bobru — a dokładniej w pasie, w którym biegł <strong>kanał rybacki (niem. <em>Fischerei</em>, <em>Fischereigraben</em>)</strong>, w kwartale ulic <strong>Uferstraße / Fischerstraße / Fischergraben / Dammstraße</strong> (dziś: <strong>ul. Nadodrzańska — ul. Bobrowa — ul. Grobla</strong>, rejon pl. Bolesława Prusa i ul. Żeromskiego).</p>
<p><span class="tag t-fact">fakt</span> Ta dzielnica <strong>nie istnieje w dawnym kształcie</strong>: kanał zasypano, nowe ujście Bobru powstało w połowie lat 30. przy elektrowni Stary Raduszec (ok. 1,3 km w dół Odry od starego), a przedwojenna zabudowa nadwodna została zniszczona w 1945 r.</p>
<p><span class="tag t-fact">fakt</span> Odnalazłem <strong>komplet znanych mi zdjęć naziemnych tej dzielnicy</strong>: 16 kart kanału rybackiego (1890–1932), 18 kart starego ujścia Bobru (1901–1938), 9 kart Stadtgrabenu/Otoku z mostem Elizy i kąpieliskiem miejskim (1900–1940), plus <strong>ostre zdjęcia lotnicze z lat 30.</strong> — i to one są w tym dossier.</p>
<p><span class="tag t-conc">wniosek</span> Obiekt jest domem mieszkalno-gospodarczym (względnie domem rybaka/ogrodnika) z ogrodem schodzącym do wody, w tym właśnie kwartale. <span class="tag t-no">nadal nieustalone</span> numer posesji i nazwa — do domknięcia potrzebny kataster (rozdz. 7).</p>
</div>

<h2>1. Skąd wiemy, że to ten kwartał — trzy wycinki z badanego zdjęcia</h2>
<p>Poniższe wycinki pochodzą z digitalizatu RW 0229 Nr. 46002 (Landesarchiv NRW, CC BY-SA 4.0). Zestawione z kartami z galerii pozwalają rozpoznać układ: <em>woda na pierwszym planie → zadrzewiona skarpa z ogrodami → jasna ścieżka nadbrzeżna → zabudowa, w której dominują wysokie, ciemne dachy</em>.</p>
{fig('d01_detail','W-01','Obiekt z prostokąta (powiększenie ×6)','skan archiwalny, kontrast wzmocniony','Dwie bryły: duża, ciemna połać dachowa (budynek gospodarczy lub dom z szerokim dachem) oraz — przed nią — jasny, bielony szczyt mniejszego domu z kominem. Wszystko przysłonięte koronami drzew, w ogrodzie, nad skarpą.','https://www.archivportal-d.de/item/RA6A7DCXRLNNV6DKDG4RVNXAOKEHSSXT')}
{fig('d02_sw','W-02','Południowo-zachodni skraj miasta nad wodą','RW 0229 Nr. 46002, wycinek','Widać całą krawędź: domy z ogrodami, jasny wydeptany pas nadbrzeża, drzewa, przy lewym brzegu pomost z łodzią. Woda jest szeroka i spokojna — to nie kanał, lecz rozlewisko starego ujścia Bobru / Otok.','https://www.archivportal-d.de/item/RA6A7DCXRLNNV6DKDG4RVNXAOKEHSSXT')}
{fig('d03_left','W-03','Zabudowa i kościół na skraju kwartału','RW 0229 Nr. 46002, wycinek','Powyżej nadbrzeża: zwarta zabudowa z wysokimi dachami, otwarty plac i <strong>kościół o neogotyckiej, ceglanej elewacji ze szczycikami</strong>. Ten kościół to punkt odniesienia przy dopasowywaniu kadru do planów i do ostrych zdjęć lotniczych z lat 30.','https://www.archivportal-d.de/item/RA6A7DCXRLNNV6DKDG4RVNXAOKEHSSXT')}

<div class="box warn">
<h3 style="margin-top:0">Kandydat do sprawdzenia: duży jasny dom nad Bobermündung (karta B-04)</h3>
<p>Na karcie <em>„Partie a. d. Bobermündung"</em> (B-04, 1909–1910) po stronie miasta stoi <strong>duży, jasny dom z wysokim, ciemnym dachem i białym szczytem z małym okienkiem strychowym</strong>, a za nim rozległa, ciemna połać dachowa i szalowane domki. To zestawienie brył najbardziej przypomina to, co widać w czerwonym prostokącie (W-01). Zestawiam oba wycinki poniżej.</p>
{fig('d05_boberm_zoom','W-04','Ten sam typ zabudowy na karcie z 1909–1910 (powiększenie)','fragment karty B-04; skan: t.ziemlicki / polska-org','Jasny dom z wysokim dachem i białym szczytem, obok ciemne dachy gospodarcze, szalowane domki, ogrody i jasna droga. <strong>To kandydat, nie identyfikacja</strong> — karta jest kartą widokową bez adresu, a kąt widzenia jest inny niż na zdjęciu lotniczym.','https://polska-org.pl/4542778,foto.html')}
<p><strong>Co trzeba, aby to potwierdzić:</strong> (1) na ostrym kadrze L-01 odszukać ten dom i porównać układ dachów; (2) sprawdzić w <em>Grundstücksverzeichnis</em> (GStA PK Rep. 97 Nr. 5540) i w <em>Einwohnerbuchu</em> 1926, kto był właścicielem posesji w tym miejscu; (3) zapytać autora kart na polska-org (Petroniusz) — dysponuje on zdjęciami dolnеgo miasta z 2017 r. i kompletem skanów, więc rozpoznanie zajmie mu prawdopodobnie chwilę.</p>
</div>

<h2>2. Galeria A — kanał rybacki i przystań (16 kart, 1890–1932)</h2>
<p class="small">Obiekt na polska-org: <a href="https://polska-org.pl/6947893,Krosno_Odrzanskie,Kanal_przystan_rybacka.html">„Kanał (przystań rybacka)", dawna nazwa <strong>Fischerei</strong>, status: nie istnieje</a>. Opis obiektu: „Kanał przecinał część Starego Miasta w Krośnie Odrzańskim łącząc Bóbr z Odrą. Kanał znajdował się w dzielnicy rybackiej, pełnił funkcję przystani rybackiej (cumowanie, naprawa łodzi). Nad kanałem przerzucona była kładka (<em>Die Fischerbrücke</em>) komunikująca z pozostałą częścią Starego Miasta. Obecnie kanał nie istnieje." Datowania i podpisy kart podaję za tą stroną (autorami skanów są m.in. Petroniusz, t.ziemlicki, Alistair, bynio, foto-baron).</p>
{gallery(A)}

<h2>3. Galeria B — stare ujście Bobru i „Bobermündung" (10 kart, 1901–1938)</h2>
<p class="small">Obiekt: <a href="https://polska-org.pl/6947808,Krosno_Odrzanskie,Ujscie_Bobru_stare.html">„Ujście Bobru (stare)"</a>. Opis: stare ujście Bobru do Odry to dziś ujście rzeki <strong>Otok</strong> (czasami zwanej Starą Odrą); nowe ujście leży ok. <strong>1,3 km w dół Odry</strong>, a kanał odprowadzający wody Bobru powstał przy budowie elektrowni <strong>Stary Raduszec w połowie lat 30. XX w.</strong></p>
{gallery(B)}

<h2>4. Galeria C — Stadtgraben / Otok: most Elizy, kąpielisko, szkoła, przystań (8 kart, 1900–1940)</h2>
<p class="small">Obiekt: <a href="https://polska-org.pl/8543925,Krosno_Odrzanskie,Rzeka_Otok.html">„Rzeka Otok", dawne nazwy <em>Stadt-Graben</em>, <em>Stare koryto Odry</em></a>. Opis: krótki ciek otaczający niegdyś miasto od wschodu, południa i zachodu; w końcowym odcinku znajdowało się pierwotne ujście Bobru; nad Otokiem, w ciągu ul. Bohaterów Wojska Polskiego, przerzucony jest <strong>most Elizy (Elisenbrücke)</strong>.</p>
{gallery(C)}

<h2>5. Galeria D — zdjęcia lotnicze tej samej okolicy (6 kadrów, 1930–1940)</h2>
<p class="small">To najważniejsza grupa do <strong>odnalezienia samego budynku</strong>: kadry są ostrzejsze i często obejmują fragment, którego na zdjęciu z Landesarchiv NRW nie widać. Karta L-01 („Orig.-Fliegeraufnahme 76423") pochodzi z tej samej epoki i prawdopodobnie z tej samej serii nalotów.</p>
{gallery(D)}

<h2>6. Galeria E — trzy materiały domykające kontekst obiektu</h2>
{gallery(E)}

<h2>7. Jak domknąć identyfikację — konkretnie</h2>
<div class="box">
<h3 style="margin-top:0">Cechy, po których rozpoznać obiekt na materiałach z galerii</h3>
<ul>
<li><strong>Dwie bryły:</strong> duża, ciemna połać dachowa + niższy, jasny (bielony) szczyt z kominem, ustawiony frontem do ścieżki.</li>
<li><strong>Ogród:</strong> regularne nasadzenia drzew owocowych między domem a skarpą; brak ogrodzenia murowanego od strony wody.</li>
<li><strong>Położenie:</strong> bezpośrednio nad wodą, przy jasnym, wydeptanym pasie nadbrzeżnym, na skraju zwartej zabudowy — z tyłu, po drugiej stronie ulicy, duży dwukondygnacyjny gmach z rzędami okien (por. S-07, szkoła żeńska).</li>
<li><strong>Sąsiedztwo wodne:</strong> szerokie, spokojne rozlewisko (Otok / stare ujście Bobru), pomosty i łodzie, w głębi — piaszczysta łacha i kładka (por. B-03, B-04).</li>
</ul>
<h3>Dokumenty, które dają numer posesji i nazwisko właściciela</h3>
<ol>
<li><strong>GStA Preußischer Kulturbesitz, I. HA Rep. 97, Nr. 5540</strong> — <em>Grundstücksverzeichnis des Amtsgerichts Crossen an der Oder/Kreis Crossen</em>, 1921–1937 (<a href="https://www.archivportal-d.de/item/2JRQC4NXSE2JK55OZ24STXZRZKHEUCJJ">rekord</a>). Wykaz nieruchomości sądu obwodowego — numery parcel i właściciele.</li>
<li><strong>Einwohnerbuch von Stadt und Kreis Crossen 1926</strong> — spis ulic z numerami domów (<a href="https://stiftung-brandenburg.de/?page_id=1239">Stiftung Brandenburg</a>, <a href="https://www.bggroteradler.de/?page_id=8696&amp;dbid=10">indeks BGG</a>). Szukać haseł: <em>Fischerstraße</em>, <em>Uferstraße</em>, <em>Fischergraben</em>, <em>Dammstraße</em>.</li>
<li><strong>Kontakt do autora kart na polska-org</strong>: użytkownik <strong>Petroniusz</strong> prowadzi karty tego miasta i sfotografował dolne miasto w 2017 r.; użytkownik <strong>t.ziemlicki</strong> wgrał większość skanów. Karta „Kanał (przystań rybacka)" ma <strong>komentarze</strong> — to najszybsza droga do ustalenia, który dom stał w miejscu z prostokąta.</li>
<li><strong>Zamówienie reprograficzne w LAV NRW</strong> (rheinland@lav.nrw.de): nowy, lepszy skan RW 0229 Nr. 46002 — przy tej rozdzielczości różnica jest duża.</li>
</ol>
</div>

<h2>8. Nazwy ulic i wód — klucz do czytania źródeł</h2>
<table>
<thead><tr><th>Nazwa historyczna</th><th>Znaczenie / funkcja</th><th>Współcześnie</th></tr></thead>
<tbody>
<tr><td><em>Fischerei</em>, <em>Fischereigraben</em></td><td>kanał rybacki z przystanią, kładką (<em>Fischerbrücke</em>) i pomostami; dziś nie istnieje</td><td>zasypany; rejon ul. Bobrowej</td></tr>
<tr><td><em>Fischerstraße</em></td><td>ulica dzielnicy rybackiej</td><td><strong>ul. Bobrowa</strong></td></tr>
<tr><td><em>Dammstraße / Grabenstraße / Westpromenade</em></td><td>północny odcinek – Dammstraße, środkowy – Grabenstraße, południowy – Westpromenade</td><td><strong>ul. Grobla</strong></td></tr>
<tr><td><em>Stadt-Graben</em> / <em>Otok</em> / „Stara Odra"</td><td>stare koryto Odry otaczające miasto; tu pierwotne ujście Bobru</td><td><strong>rzeka Otok</strong></td></tr>
<tr><td><em>Bobermündung</em> (stare)</td><td>ujście Bobru do Odry przy mieście</td><td>przesunięte ok. 1,3 km w dół Odry (lata 30., elektrownia Stary Raduszec)</td></tr>
<tr><td><em>Elisenbrücke</em></td><td>most nad Otokiem w ciągu ul. Bohaterów Wojska Polskiego</td><td><strong>Most Elizy</strong></td></tr>
<tr><td><em>Vorwerk Klette</em></td><td>dwór na dawnym grodzisku, do którego prowadziła kładka; dziś ruina, własność prywatna</td><td>Stary Raduszec</td></tr>
</tbody></table>

<h2>9. Czego w tym dossier nie ma (świadomie)</h2>
<div class="box warn">
<ul>
<li><strong>Nie twierdzę, że któryś z domów na tych kartach to obiekt z prostokąta.</strong> Karty pokazują kwartał, wodę, pomosty i zabudowę — wskazanie właściwego domu wymaga zestawienia z lotniczym kadrem L-01 oraz z katastrem.</li>
<li>Nie widziałem <strong>żadnej fotografii wnętrza ani aktu własności</strong> tego domu; nie mam też potwierdzonej nazwy własnej budynku (typu „Haus X", „Gasthaus Y").</li>
<li>Datowania kart (np. „1909–1910") pochodzą od użytkowników polska-org i są przybliżone; podaję je jako ich datowanie, nie jako ustaloną datę.</li>
<li>Karty są skanami pocztówek i zdjęć z <strong>aukcji internetowych i zbiorów prywatnych</strong> — ich oryginały są rozproszone; podane linki prowadzą do kart, nie do instytucji przechowujących oryginał.</li>
</ul>
</div>

<h2>10. Kwerenda — co sprawdzono w tej turze</h2>
<table>
<thead><tr><th style="width:26%">Źródło</th><th>Metoda / zapytanie</th><th>Wynik</th></tr></thead>
<tbody>
<tr><td>polska-org.pl — karty obiektów</td><td>karta miasta (4309874) → obiekty wodne i ulice; <code>entityListForCity</code>, karty ulic: Bobrowa, Grobla, Nadodrzańska</td><td><span class="tag t-fact">trafienie</span> opisy: Kanał (Fischerei), Ujście Bobru stare/nowe, Rzeka Otok, Kładka, Most Elizy, Most Odrzański; nazwy historyczne ulic</td></tr>
<tr><td>polska-org.pl — karty zdjęć</td><td>pobranie 45 obrazów w pełnej rozdzielczości (1500 px) + podpisy i datowania</td><td><span class="tag t-fact">trafienie</span> komplet 16 + 18 + 9 kart z tego kwartału, 8 zdjęć lotniczych</td></tr>
<tr><td>heimatkreis-crossen-oder.de</td><td>przejrzenie wszystkich 10 podstron serwisu</td><td><span class="tag t-no">brak</span> serwis nie ma galerii zdjęć miasta (tylko plan Altstadt i literatura)</td></tr>
<tr><td>ZBC (Zielonogórska Biblioteka Cyfrowa)</td><td>kolekcja „Przedwojenne pocztówki lubuskie – Krosno Odrzańskie"</td><td><span class="tag t-no">bariera</span> treść wyłącznie w DjVu, bez serwera obrazów — nie da się pobrać skanu bez konwersji</td></tr>
<tr><td>Landesarchiv NRW / Archivportal-D</td><td>rekordy RW 0229 (46002, 7482, 7485, 7486) i rekord Bestandu</td><td><span class="tag t-fact">trafienie</span> pełne metadane, ostrzeżenie archiwum o błędnych przypisaniach i o wymianie skanów na nowe</td></tr>
</tbody></table>

<p class="small" style="margin-top:26px">Wszystkie karty z polska-org podaję z linkiem do konkretnego zdjęcia; skany pochodzą od użytkowników serwisu (Petroniusz, t.ziemlicki, Alistair, bynio, foto-baron, maras) i są tam publikowane jako materiał historyczny. W raporcie nie zmieniono żadnego podpisu — datowania i opisy cytuję w brzmieniu ze źródła, a własne obserwacje oznaczam.</p>

</div></body></html>"""
open('/home/user/report/Dossier_budynek_Crossen.html','w',encoding='utf-8').write(HTML)
print(round(len(HTML)/1e6,2),'MB')
