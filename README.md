
# Public Library Management System

Autor: Martin Šilar  
Škola: SPŠE Ječná  
Datum: 8. 1. 2026  
Typ práce: Školní projekt – programování a databázové systémy  

---

## 1. Popis projektu

CLI aplikace pro správu veřejné knihovny.
Aplikace pracuje s relační databází MySQL a umožňuje správu knih, čtenářů, exemplářů a výpůjček.

---

## 2. Použité technologie

- Python 3
- MySQL
- mysql-connector-python
- Git

---

## 3. Požadavky na prostředí

- Python 3.x
- MySQL Server
- Přístup do MySQL
- Terminál / příkazová řádka

IDE není potřeba

---

## 4. Konfigurace databáze

Konfigurace databázového připojení je uložena v souboru:

`src/db/config.py`

Obsah souboru:

```[config.py]
{
  "host": "localhost",
  "port": 3306,
  "database": "library",
  "user": "root",
  "password": "student"
}
```

Před spuštěním aplikace upravte hodnoty dle školního PC.

---

## 5. Inicializace databáze

1. Přihlášení do MySQL:

`mysql -u root -p`

2. Vytvoření struktury databáze:

`SOURCE db/schema.sql;`

3. Vytvoření databázových pohledů:

`SOURCE db/views.sql;`

---

## 6. Instalace závislostí

`pip install -r requirements.txt`

---

## 7. Import testovacích dat

Adresář data/ obsahuje:

- members.csv
- books.json
- copies.csv

Import se provádí z aplikace přes volbu „Import data“.

---

## 8. Spuštění aplikace

`python -m src.cli.app`

---

## 9. Ovládání aplikace

Menu obsahuje:

1. List members

2. List books

3. Borrow book

4. Return book

5. Show active loans

6. Import data

7. Cancel loan

8. Show book statistics report

0. Exit

---

## 10. Poznámky pro testera

- Tester nepotřebuje znát zdrojový kód
- Tester postupuje pouze podle README a testovacích scénářů TS-01, TS-02, TS-03
- Aplikace ošetřuje chybné vstupy a transakce
