# Public Library Management System

**Autor:** Martin Šilar
**Škola:** SPŠE Ječná
**Datum:** 29. 12. 2025
**Typ práce:** Školní projekt – návrh řešení

---

## 1. Účel návrhu

Tento dokument popisuje návrh řešení informačního systému pro správu veřejné knihovny na základě provedené analýzy.
Cílem návrhu je definovat architekturu aplikace, databázový model, hlavní datové toky a chování systému bez řešení konkrétní implementace zdrojového kódu.

Návrh slouží jako podklad pro následnou implementaci, testování a obhajobu projektu.

---

## 2. Architektura aplikace

Aplikace je navržena jako **three-tier architektura**, která zajišťuje jasné oddělení odpovědností mezi jednotlivými částmi systému a umožňuje snadnou údržbu a rozšiřitelnost.

### 2.1 Přehled vrstev (Three-tier)

#### 1. Prezentační vrstva (Presentation Layer)

- zajišťuje komunikaci s uživatelem
- poskytuje ovládání aplikace netechnickému uživateli
- neobsahuje aplikační ani databázovou logiku
- předává uživatelské požadavky aplikační logice

---

#### 2. Aplikační vrstva (Service Layer)

- obsahuje aplikační a řídicí logiku systému
- zpracovává uživatelské požadavky
- provádí validaci vstupních dat
- řídí transakční scénáře
- komunikuje výhradně s datovou vrstvou

---

#### 3. Datová vrstva (Data Access Layer)

- zapouzdřuje přístup k databázi
- obsahuje implementaci DAO / Repository tříd
- obsahuje SQL dotazy
- komunikuje s databází MySQL
- zajišťuje izolaci databázové logiky od aplikační vrstvy

Databázový server MySQL je považován za součást datové vrstvy.

---

## 3. Použité návrhové vzory

### 3.1 DAO / Repository pattern (D1)

Pro přístup k databázi je použit návrhový vzor **DAO (Data Access Object)**, případně Repository.

- každá hlavní entita databáze má vlastní DAO třídu
- aplikační logika nikdy nepřistupuje k databázi přímo
- změna databázového schématu nevyžaduje změnu aplikační logiky

Použití tohoto návrhového vzoru splňuje hlavní úkol **D1** dle zadání projektu.

---

## 4. Databázový návrh

### 4.1 Přehled tabulek

Databázový model je navržen s cílem minimalizovat počet tabulek, zachovat normalizaci dat a splnit všechny povinné požadavky zadání.

#### 1. `members`

- eviduje registrované čtenáře knihovny
- obsahuje informace o typu členství a aktivitě čtenáře

---

#### 2. `books`

- reprezentuje logickou knihu (titul)
- neobsahuje informace o fyzických exemplářích

---

#### 3. `authors`

- eviduje autory knih

---

#### 4. `book_author`

- vazební tabulka mezi knihami a autory
- realizuje vztah M:N

---

#### 5. `copies`

- reprezentuje fyzické exempláře knih
- obsahuje informace o stavu exempláře a jeho pořizovací ceně

---

#### 6. `loans`

- eviduje výpůjčky konkrétních exemplářů knih
- obsahuje informace o datu výpůjčky, datu vrácení a případné pokutě

---

### 4.2 Vztahy mezi entitami

- `books` ↔ `authors`

  - vztah M:N realizovaný pomocí tabulky `book_author`
- `books` → `copies`

  - vztah 1:N (jedna kniha může mít více exemplářů)
- `members` → `loans`

  - vztah 1:N (čtenář může mít více výpůjček)
- `copies` → `loans`

  - vztah 1:N (exemplář může být v průběhu času vypůjčen opakovaně)

---

## 5. Transakční scénáře

### 5.1 Vypůjčení knihy

Proces vypůjčení knihy je realizován jako databázová transakce:

1. ověření dostupnosti fyzického exempláře
2. vytvoření záznamu v tabulce `loans`
3. aktualizace stavu exempláře v tabulce `copies`
4. potvrzení transakce

V případě chyby v kterémkoliv kroku je provedeno vrácení transakce (rollback).

---

### 5.2 Vrácení knihy

1. aktualizace záznamu výpůjčky (datum vrácení)
2. výpočet případné pokuty
3. změna stavu exempláře na dostupný
4. potvrzení transakce

---

## 6. Databázové pohledy (Views)

Pro zjednodušení práce s daty a tvorbu přehledů budou vytvořeny minimálně dva databázové pohledy:

### 6.1 Přehled aktuálních výpůjček

- spojení tabulek `members`, `books`, `copies` a `loans`
- zobrazuje pouze nevrácené výpůjčky

---

### 6.2 Statistiky knihovny

- agregovaná data o výpůjčkách
- přehled počtu výpůjček podle knih nebo žánrů

---

## 7. Import dat

Systém podporuje import dat z externích souborů:

- **CSV** – import čtenářů
- **JSON** – import knih a autorů

Importní proces zahrnuje:

- kontrolu struktury souboru
- validaci povinných údajů
- ošetření chyb vzniklých při importu

---

## 8. Konfigurace systému

Konfigurace aplikace je oddělena od zdrojového kódu a uložena v samostatném konfiguračním souboru.

Konfigurovatelné položky zahrnují:

- připojení k databázi
- přihlašovací údaje
- port a host databázového serveru

---

## 9. Chybové stavy a jejich řešení

Systém musí ošetřovat následující chybové stavy:

- nedostupná databáze
- neplatná nebo chybějící konfigurace
- pokus o výpůjčku nedostupného exempláře
- neplatná vstupní data

Všechny chybové stavy musí být uživateli oznámeny srozumitelným způsobem.

---

## 10. Shrnutí

Tento návrh definuje architekturu aplikace, databázový model a základní chování systému pro správu veřejné knihovny.
Na jeho základě bude provedena implementace aplikace, vytvoření databázového schématu, testovacích scénářů a finální dokumentace projektu.
