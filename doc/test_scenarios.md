# Public Library Management System

**Autor:** Martin Šilar
**Škola:** SPŠE Ječná
**Datum:** 4. 1. 2026
**Projekt:** Školní projekt – testovací scénáře

---

## Testovací scénář TS-01

### Spuštění aplikace a zobrazení dat

**Cíl:**
Ověřit, že aplikace je spustitelná, připojí se k databázi a zobrazí základní data.

**Předpoklady:**

- Databáze MySQL je vytvořena pomocí `schema.sql`
- Jsou vložena testovací data (members, books, copies)
- Jsou nainstalovány závislosti z `requirements.txt`

**Postup:**

1. Otevřít terminál v kořenovém adresáři projektu
2. Spustit aplikaci příkazem: ``python -m src.cli.app``
3. Zvolit možnost `1 – List members`
4. Zvolit možnost `2 – List books`

**Očekávaný výsledek:**

- Aplikace se spustí bez chyby
- Zobrazí se textové menu
- Vypíší se registrovaní čtenáři
- Vypíší se dostupné knihy

**Výsledek testu:**
☐ Úspěšný ☐ Neúspěšný

---

## Testovací scénář TS-02

### Vypůjčení knihy (transakční scénář)

**Cíl:**
Ověřit správnou funkci výpůjčky knihy jako transakce nad více tabulkami.

**Předpoklady:**

- Existuje čtenář (`members`)
- Existuje exemplář knihy se stavem `available`
- Aplikace je spuštěna

**Postup:**

1. Zvolit možnost `3 – Borrow book`
2. Zadat platné `Member ID`
3. Zadat platné `Copy ID` (stav `available`)
4. Zadat platné datum vrácení
5. Potvrdit akci

**Očekávaný výsledek:**

- Zobrazí se hláška „Book borrowed successfully“
- V tabulce `loans` vznikne nový záznam
- Stav exempláře v tabulce `copies` se změní na `borrowed`
- Transakce je provedena korektně

**Výsledek testu:**
☐ Úspěšný ☐ Neúspěšný

---

## Testovací scénář TS-03

### Chybový stav, pokus o vypůjčení nedostupného exempláře

**Cíl:**
Ověřit, že aplikace správně reaguje na chybový stav a provede rollback transakce.

**Předpoklady:**

- Existuje exemplář knihy se stavem `borrowed`
- Aplikace je spuštěna

**Postup:**

1. Zvolit možnost `3 – Borrow book`
2. Zadat platné `Member ID`
3. Zadat `Copy ID`, které není dostupné
4. Potvrdit akci

**Očekávaný výsledek:**

- Aplikace zobrazí chybovou hlášku
- Nevznikne nový záznam v tabulce `loans`
- Stav exempláře v tabulce `copies` zůstane beze změny
- Transakce je vrácena zpět (rollback)

**Výsledek testu:**
☐ Úspěšný ☐ Neúspěšný

---

## Shrnutí testování

Provedené testovací scénáře ověřují:

- spustitelnost aplikace
- správnou práci s databází
- funkčnost transakčních scénářů
- ošetření chybových stavů

Na základě provedených testů aplikace splňuje stanovené požadavky.
