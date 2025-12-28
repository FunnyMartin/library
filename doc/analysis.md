# Public Library Management System  

**Autor:** Martin Šilar  
**Škola:** SPŠE Ječná  
**Datum:** 28. 12. 2025  
**Typ práce:** Školní projekt – programování, databázové systémy  

---

## 1. Úvod

Tento projekt se zabývá návrhem a implementací informačního systému pro správu veřejné knihovny.  
Cílem projektu je vytvořit aplikaci, která umožní evidovat knihy, jejich fyzické exempláře, autory, registrované čtenáře a výpůjčky. Projekt vzniká v rámci výuky programování a databázových systémů a slouží k procvičení práce s relační databází a návrhu softwarového řešení.

---

## 2. Kontext a popis problému

Veřejné knihovny pracují s velkým množstvím knih, které mají často více fyzických exemplářů.  
Zároveň musí evidovat čtenáře, sledovat výpůjčky, termíny vrácení a případné pokuty za pozdní vrácení nebo poškození knih.

Bez informačního systému je správa těchto údajů časově náročná a náchylná k chybám.  
Problémy mohou vznikat například při:

- zjišťování dostupnosti konkrétní knihy,
- sledování, kdo má knihu aktuálně vypůjčenou,
- vyhodnocování statistik (nejčtenější knihy, aktivní čtenáři),
- evidenci pokut.

Cílem systému je tyto činnosti zjednodušit, zpřehlednit a zajistit konzistentní uložení dat v relační databázi.

---

## 3. Cíloví uživatelé

Systém je určen pro následující typy uživatelů:

- **Čtenář**  
  Registrovaná osoba, která si může půjčovat knihy a vracet je zpět do knihovny.

- **Knihovník / správce systému**  
  Osoba, která spravuje knihovní fond, eviduje výpůjčky, vrácení knih a řeší pokuty.

---

## 4. Funkční požadavky

- **FR-01** Systém musí umožňovat evidenci knih (název, ISBN, žánr, rok vydání).  
- **FR-02** Systém musí umožňovat evidenci autorů a jejich vazby na knihy.  
- **FR-03** Systém musí umožňovat evidenci fyzických exemplářů knih a jejich aktuální stav.  
- **FR-04** Systém musí umožňovat registraci čtenářů a správu jejich členství.  
- **FR-05** Systém musí umožňovat vytvoření výpůjčky konkrétního exempláře knihy.  
- **FR-06** Systém musí umožňovat vrácení vypůjčené knihy a aktualizaci jejího stavu.  
- **FR-07** Systém musí umožňovat evidenci pokut za pozdní vrácení nebo poškození knihy.  
- **FR-08** Systém musí umožňovat zobrazení přehledu aktuálně vypůjčených knih.  
- **FR-09** Systém musí umožňovat generování základních statistických přehledů (např. nejčtenější knihy).

---

## 5. Nefunkční požadavky

- **NFR-01** Aplikace musí být spustitelná na školním počítači bez použití IDE.  
- **NFR-02** Data musí být ukládána do skutečné relační databáze MySQL.  
- **NFR-03** Konfigurace databázového připojení musí být oddělena od zdrojového kódu.  
- **NFR-04** Systém musí ošetřovat chybové stavy (např. nedostupná databáze, neplatný vstup).  
- **NFR-05** Projekt musí být verzován pomocí systému Git.  
- **NFR-06** Zdrojový kód a dokumentace musí být přehledné a srozumitelné.  
- **NFR-07** Funkčnost systému musí být ověřitelná pomocí testovacích scénářů.

---

## 6. Omezení a předpoklady

- Systém není určen pro online provoz s velkým množstvím uživatelů.  
- Aplikace řeší základní funkce knihovny, nikoliv kompletní ekonomický nebo účetní systém.  
- Uživatelské rozhraní je navrženo tak, aby bylo použitelné i pro netechnického uživatele.

---

## 7. Shrnutí

Analýza definuje problém správy veřejné knihovny a stanovuje základní funkční a nefunkční požadavky systému.  
Na základě této analýzy bude v další fázi vytvořen návrh architektury aplikace a databázového schématu, který umožní následnou implementaci a testování systému.
