# Grobla 64 (Krosno Odrzańskie) — archiwum materiałów

**Stan na 31 października 2026 · 75 plików · 17.6 MB**

Budynek: dawna miejska łaźnia (Badeanstalt) przy ul. Grobla 64, Krosno Odrzańskie.
Działki ewidencyjne **080206_4.0002.61/6** (1 684,6 m²) i **61/4** (1 421,5 m²), obręb 4.

---

## 1. Najważniejsze ustalenia (w pięciu punktach)

1. **Metraż, twardo z ewidencji.** Hala to **jeden budynek 403,9 m²** (31,1 × 13,0 m),
   **przecięty granicą dwóch działek** (216,4 m² na 61/4 + 187,5 m² na 61/6).
   Dom Grobla 64 — **121,0 m²**. Razem **524,9 m² zabudowy**.
   → `04_GEOMETRIA_EGIB_I_RYSUNKI/TABELA_POWIERZCHNI.md`
2. **Funkcja.** Zakład kąpielowy (Badeanstalt), nie sama łaźnia wanniana: część kryta
   (wanny I/II klasy, natryski, łaźnia parowa, pralnia, kotłownia z kominem) + kąpielisko
   na wodzie. Gminny program zabytków: *„Nad Bobrem usytuowane były łaźnie miejskie”*.
   → `01_RAPORTY/R1_metraz_i_funkcja_2026-10-30.html`
3. **Sygnatura, która domyka sprawę.** Brandenburgisches Landeshauptarchiv, Potsdam:
   **Rep. 31B Frankfurt/O 324 (1936)** — „Antrag des Bürgermeisters in Crossen auf
   hochwasserpolizeiliche Genehmigung für den Bau einer Badeanstalt mit Umzäunung am
   rechten Ufer der Oder bei km 512,6”. Tam — jeżeli gdziekolwiek — są **rzuty**.
   → `02_SYGNATURY_I_PISMA/`
4. **Czego nie ma.** Żadnego zdjęcia wnętrza i żadnego rzutu w zasobach publicznych.
   Sprawdzone i udokumentowane: 1 137 kart fotopolski, 401 tytułów ZBC, zespół 454 akt
   ogniowych, Herder-Institut, Archivportal-D, szukajwarchiwach (zablokowane).
   → `07_EWIDENCJA_KWEREND/LOG_KWEREND.md`
5. **Otwarte ryzyko.** Grobla 64 **nie jest** w gminnej ewidencji zabytków (jest tam
   nr 66). Poszlaki wskazują 64, ale definitywnie rozstrzygnie to Lageplan z teczki 1936.

---

## 2. Jak to jest ułożone

```
01_RAPORTY/                  pięć raportów HTML (R1 najnowszy merytorycznie, R3 najnowszy w czasie)
                             + pełny wypis ksiąg adresowych (607 wierszy)
02_SYGNATURY_I_PISMA/        wykaz sygnatur + 5 gotowych pism do wysłania (PL i DE)
03_ZDJECIA_PRZEDWOJENNE/     wszystko, co istnieje: łaźnia 1916, naloty 1925–33, ulica 1905–38, ujście Bobru
04_GEOMETRIA_EGIB_I_RYSUNKI/ bilans powierzchni, plany P-01/P-02, rekonstrukcja R-01, surowe dane EGiB (WKT/JSON), skrypty
05_ZRODLA_TEKSTOWE/          Städtebuch, program zabytków 2020 (PDF + tekst), wypisy (GZEW, łaźnie nad Bobrem,
                             księgi adresowe) oraz kartografia/ — plany 1893 i 1945 z opisem zakresu użyteczności
06_ZDJECIA_WSPOLCZESNE/      stan dziś: ortofoto hali i posesji, ortofoto z numerami działek, schemat OSM + opis
07_EWIDENCJA_KWEREND/        log wszystkich zapytań + indeksy 1 137 zdjęć i 401 tytułów (dowody kompletności)
08_NARZEDZIA/                skrypty generujące raporty i rysunki (odtwarzalność)
SPIS_PLIKOW.csv              spis każdego pliku: opis, źródło, uwagi, rozmiar, suma kontrolna sha256
```

## 3. Od czego zacząć czytanie

- **Chcesz wyników:** `01_RAPORTY/R1_metraz_i_funkcja_2026-10-30.html`
  (metraż i funkcja) → `01_RAPORTY/R3_teczka_1936_runda5_2026-10-31.html` (sygnatura i zdjęcia).
- **Chcesz działać:** `02_SYGNATURY_I_PISMA/PISMO_01_BLHA_Potsdam_de.txt`
  i `02_SYGNATURY_I_PISMA/JAK_ZAMAWIAC.md`.
- **Chcesz zweryfikować:** `07_EWIDENCJA_KWEREND/LOG_KWEREND.md` + `SPIS_PLIKOW.csv`
  (każdy plik ma podane źródło).

## 4. Status dowodowy — czytaj przed cytowaniem

| kategoria | status |
|---|---|
| Powierzchnie i obrysy (R1, tabele) | **fakt** — geometria EGiB, przeliczona |
| Cytaty źródłowe (Städtebuch, GZEW, księgi adresowe) | **fakt** — dosłowne, z podaniem dokumentu |
| Sygnatura BLHA 31B FrankfurtO 324 / 1936 | **fakt** — odczytana z rekordu Archivportal-D; **teczki nie widziałem, nie jest zdigitalizowana** |
| Dopasowanie „km 512,6” i „rechtes Ufer” do dz. 61/6 | **wnioskowanie z dokumentu**, nie pomiar |
| Rysunek R-01 (program wnętrza) | **hipoteza typologiczna** — nie inwentaryzacja |
| Kubatura, powierzchnia użytkowa | **szacunek rachunkowy** |

Zdjęcia są reprodukcjami ze wskazanych źródeł; **żadne nie zostało wygenerowane**.
