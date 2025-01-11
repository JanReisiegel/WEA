# Odpovědi na okruhy ke zkoušce

## Co je HTTP? Jaké má vlastnosti

- Hyper Text Transfer Protocol
- Protocol pro přenos hypertextových dokumentů mezi klientem a serverem
- Vlastnosti:
  - Bezstavový - Nepamatuje si předchozí požadavky
  - Textový - jednoduchá čitelnost požadavků a odpovědí
  - Klient-server - klient požadavky, serever Odpovědi
  - Rozšiřitelnost - Podpora různých metody
  - Podpora HTTPS - bezpečný přenos dat

## Jak vypadá HTTP požadavek?

```
GET /index.html HTTP/1.1
Host: wwwexample.com
User-Agent: Mozila/5.0
Accept: text/html
```

- Typ požadavku (GET)
- Cílová URL
- Verze protokolu
- Halvičky (Host, User-Agent,...)
- Tělo (data u POST)

## Jak vypadá HTTP odpověď

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

- Stavový řádek: Verze protokolu, stavový kód, popis
- Hlavičky (Content-Type, Content-Length, ...)
- Tělo - obsah odpovědi (např. html stránka)

## K čemu se použivají metody GET, PUT, CONNECT?

- GET - získání dat ze serveru (pouze získává)
- PUT - Nahrazení nebo vytvoření dat na serveru
- CONNECT - Nastavení tunelu pro šifrované spojení (HTTPS)

## K čemu se používají metody POST, DELETE, OPTIONS?

- POST - Odeslání dat na server
- DELETE - smazání dat na serveru
- OPTIONS - Zjištění podporovaných metod serveru

## Jaké je rozdělení HTTP stavů?

- imformativní
- úspěšné
- přesměrování
- chyby klienta
- chyby serveru

## K čemu se používají stavy HTTP 2xx, 3xx?

- 2xx: Úspěšné zpracování požadavku
- 3xx: Přesměrování klienta někam

## K čemu se používají stavy HTTP 1xx, 5xx, 4xx?

- 1xx: imformace o pažadvku (byl přijat ke zpracování)
- 4xx: Chyba na straně klienta (404 page not found - špatná url)
- 5xx: Chyba na straně serveru (500 internal server error)

## Co je session a k čemu se využívá?

- ukládá stav komunikace mezi klientem a serverem
- užívá se k:
  - autentizaci
  - správu nákupního košíku
  - atd.

## Co jsou cookies a k čemu se využívají?

- malé textové soubory uložené v prohlížeči
- k uchování informací mezi požadavky (přihlašovací údaje, nebo uživatelské preference)

## Co je SSR? Výhody a nevýhody

- Server-Side rendering - vykreslování stránky na serveru před odesláním
- Výhody:
  - Lepší SEO
  - Rychlejší načítání první stránky
- Nevýhody
  - Vyšší zátěž serveru
  - Pomalejší klientská interakce

## Co je Webová služba? Výhody a nevýhody

- umožňuje výměnu dat mezi aplikacemi přes síť pomocí standardních protokolů (HTTP)
- Výhody:
  - Interoperabilita mezi různými systémy
  - Široká podpora standardů
- Nevýhody:
  - Nároky na zabezpečení
  - Potřeba internetového připojení

## Co je SPA? Výhody a nevýhody

- Single Page Aplication: Aplikace načte jednu stránku a dynamicky mění obsah.
- Výhody:
  - Plynulá uživatelská zkušenost
  - Rychlá interaktivita
- Nevýhody:
  - Horší SEO
  - Dlouhá doba při prvním načtení

## Co je MVC? Výhody a nevýhody

- Model-View-Controller: Architektonický návrh pro organizaci kódu
  - Model - logika dat
  - View - uživatelské rozhraní
  - Controller - Zprostředkovává interakci mezi Modelem a View
- Výhody:
  - Lepší organizace kódu
  - Snadná údržba
- Nevýhoda
  - Komplexita u malých projektů

## Co je FCP? Výhody a nevýhody

- First Contentful Paint: Doba, kdy je první obsah stránky viditelný
- Výhody:
  - Dobrý indikátor uživatelské zkušenosti
- Nevýhody:
  - Nezohledňuje Interaktivitu stránky

## Jaké vlastnosti má Javascript?

- Dynamický, interpretovaný jazyk
- Slabě typovaný
- podporuje asynchronní operace
- Pracuje s DOM
- Běží na straně serveru (Node.js) i klienta

## Co jsou události a k čemu se využívají? Příklad události

- akce k interaktivnímu chování webových stránek
- příklady:
  - kliknutí, stisk klávesy, pohyb myši, atd.

```
document.querySelector("button").addEventListener("click", () => {
    alert("Button Click")
});
```

## K čemu slouží DOM? Jak se s tím pracuje v JS

- Document Object Manager
- představuje strukturu HTML stránky jako strom objeků
- Pomocí DOM lze manipulovat s prvky

```
document.getElementById("element").innerText = "Nový text";
```

## Jakým způsobem se ukládají hesla?

- hesla se ukládají pomocí hashovacích funkcí (bcrypt)
- hash hesla se uloží do databáze
- přímé uložení hesla do databáze (bez hashování) je bezpečnostní riziko

## Co je CSRF attack?

- Cross-Site Request Forgery: útočník přiměje uživatele odelat nechtěný požadavek na server, kde je uživatel přihlášen

## K čemu se využívá JWT token?
- JSON Web Token: k bezpečnému přenosu informací mez klientem a serverem
- autentizace uživatelů
