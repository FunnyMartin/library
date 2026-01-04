# Public Library Management System

**Autor:** Martin Šilar  
**Škola:** SPŠE Ječná  
**Datum:** 4. 1. 2026  
**Typ práce:** Školní projekt – programování a databázové systémy  

---

## Popis projektu

Tento projekt představuje jednoduchý informační systém pro správu veřejné knihovny.
Aplikace umožňuje evidenci knihovních výpůjček, jejich vracení a práci s databází prostřednictvím textového uživatelského rozhraní (CLI).

Projekt slouží k demonstraci:

- práce s relační databází MySQL
- návrhu vícevrstvé architektury
- použití návrhového vzoru DAO
- implementace databázových transakcí
- testování aplikace pomocí testovacích scénářů

---

## Použité technologie

- Python 3
- MySQL
- mysql-connector-python
- Git

---

## Požadavky pro spuštění

- Nainstalovaný Python 3
- Běžící databázový server MySQL
- Přístupové údaje k databázi (nastavitelné v `src/db/config.py`)

---

## Vytvoření databáze

Skripty lze spustit buď pomocí příkazu `SOURCE`, nebo přes MySQL Workbench.

1. Přihlášení do MySQL:

```bash
mysql -u root -p
```

2. Vytvoření databáze a tabulek:

```sql
SOURCE db/schema.sql;
```

3. Vytvoření databázových pohledů:

```sql
SOURCE db/views.sql;
```

---

## Vložení testovacích dat

Testovací data jsou připravena ve formátech:

- CSV (`members.csv`)
- JSON (`books.json`)

Data slouží pro inicializační naplnění databáze a testování aplikace.
Import dat je prováděn jednorázově podle dokumentace a testovacích scénářů.

---

## Instalace závislostí

V kořenovém adresáři projektu spusťte:

```bash
pip install -r requirements.txt
```

---

## Spuštění aplikace

Aplikace se spouští z příkazové řádky bez použití IDE:

```bash
python -m src.cli.app
```

---

## Ovládání aplikace

Po spuštění se zobrazí textové menu s možnostmi:

- výpis registrovaných čtenářů
- výpis knih
- výpůjčka knihy
- vrácení knihy
- zobrazení aktivních výpůjček

Ovládání probíhá zadáváním číselných voleb a identifikátorů (ID).

---

## Poznámka pro testera

- Tester nemusí znát zdrojový kód aplikace
- Tester postupuje pouze podle tohoto README a testovacích scénářů
- Zobrazení ID v CLI je záměrné a slouží k jednoznačné identifikaci záznamů při testování

---

## Dokumentace projektu

Projektová dokumentace je rozdělena do samostatných souborů:

- `analysis.md` – analýza problému
- `design.md` – návrh řešení
- `test_scenarios.md` – testovací scénáře

Tato struktura zajišťuje přehlednost a snadnou orientaci v projektu.
