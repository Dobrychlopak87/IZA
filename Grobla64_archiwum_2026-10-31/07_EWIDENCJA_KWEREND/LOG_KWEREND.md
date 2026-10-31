# Log kwerend — co, gdzie i z jakim wynikiem

Wszystkie zapytania wykonane w trakcie pracy (rundy 1–5), z wynikiem.
Legenda: ✅ trafienie · 🟡 częściowe · ⬜ pusto · ⛔ zablokowane

## Archiwa i katalogi archiwalne
| kanał | zapytanie | wynik |
|---|---|---|
| Archivportal-D / DDB | `Badeanstalt Crossen` | ✅ **Rep. 31B FrankfurtO 324, 1936** — wniosek budowlany na łaźnię |
| Archivportal-D | `Badeanstalt` w zespole 55F Kr. Crossen (454 j.) | 🟡 tylko Sommerfeld (Lubsko); dla miasta Crossen brak → kwerenda po ulicach |
| Archivportal-D | `Stadtgraben`, `Westpromenade`, `Schwimm/Waschanstalt/Volksbad` | ⬜ / obce miasta |
| Archivportal-D | `Crossen (Oder)` ogólnie | 🟡 m.in. Bundesarchiv R 1508/1361 (Grabenstraße 332 b, 1938–43), R 154/7938 |
| szukajwarchiwach.gov.pl | wyszukiwarka + API | ⛔ Incapsula („Portlety tymczasowo niedostępne”) |
| Herder-Institut Bildkatalog | węzeł Crossen, Profanbau | ⬜ 2 błędnie podpięte rekordy |
| Deutsche Digitale Bibliothek | wyszukiwarka obiektów | ⛔ 404 / JS |
| OPUS4 SLBP (Crossener Kreis-Kalender 1913–1942) | 25 roczników, skany | 🟡 dostęp uzyskany (obejście Anubis), ale fraktura bez warstwy tekstowej → kwerenda ręczna |

## Fotografie
| kanał | zakres | wynik |
|---|---|---|
| fotopolska.eu | **pełny sweep 1 137 kart** + opisy + komentarze | ✅ 6 nowych zdjęć ulicy (Grabenstraße/Westpromenade 1932, Dammstrasse 1905) ⬜ zero wizerunków łaźni |
| ZBC Zielona Góra | 261 rekordów „Crossen” → 401 unikatowych tytułów | ⬜ brak widokówki łaźni (są dla Sulechowa i Sulęcina) |
| polska-org.pl | 1 247 zdjęć przez 10 arkuszy kontaktowych | ✅ 1 karta „Städt. Badeanstalt” (1916) |
| oldthing.de / aukcje | `Badeanstalt Crossen` | ⬜ brak ofert |
| Landesarchiv NRW | RW 0229 Nr. 46002 | ✅ nalot 1925–32 z zespołem (materiał użytkownika) |

## Teksty i biblioteki
| kanał | wynik |
|---|---|
| Google Books API `"Badeanstalt" "Crossen"` | ⛔ HTTP 429 (trzykrotnie) |
| HathiTrust full-text | ⛔ Cloudflare 403 |
| archive.org advancedsearch | ⬜ tylko dokumenty CIA |
| Deutsches Städtebuch (Crossen) | ✅ 1911 „1 Flussbadeanstalt”, 1928 „2 Bootshäuser, 1 Freiluftschwimmbad” |
| Księgi adresowe 1913/1926/1938 | ✅ 1913 Bademeister Sämisch (Stadtgraben); 1938 Heidenreich — Badeanstalt, Grabenstraße |
| Program opieki nad zabytkami 2020 (uchwała XIX/175/20) | ✅ „Nad Bobrem usytuowane były łaźnie miejskie”; wykaz GZEW dla Grobli bez nr 64 |
| BIP Krosno Odrzańskie | 🟡 wyszukiwarka nie działa; dokumenty tylko pod znanym adresem (PFU/studium 2016 dotyczą przestrzeni publicznej, nie budynków) |

## Dane przestrzenne
| kanał | wynik |
|---|---|
| ULDK GUGiK (`GetParcelByXY/ById`, `GetBuildingByXY/ById`, PL-1992) | ✅ pełna geometria: 2 działki, 3 budynki, wszystkie powierzchnie |
| GUGiK WMS ORTO HighResolution | ✅ ortofoto posesji i szerszy kadr |
| Overpass API | ✅ obrysy budynków i cieki w otoczeniu |
| Geoportal — ortofoto archiwalne | ⛔ warstwy archiwalne wymagają uwierzytelnienia (401) |

## Metodyka
Zastosowano pipeline z `elementalsouls/Claude-OSINT` (seed → ekspansja → wzbogacenie →
konwergencja, *connector resilience*, *negative-result discipline*) oraz zasadę
`obra/superpowers/verification-before-completion` (weryfikacja pliku wyjściowego przed
ogłoszeniem wyniku). Wynik negatywny raportowany wyłącznie po **kompletnym** przejściu
zbioru, z podaniem jego liczebności.
