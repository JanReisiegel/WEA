# Odpovědi na okruhy ke zkoušce

## Co je HTTP? Jaké má vlastnosti

- Hyper Text Transfer Protocol
- Komunikační protocol pro přenos hypertextových dokumentů mezi klientem a serverem
- Princip požadavků a odpovědí
- Vlastnosti:
  - Bezstavový - Nepamatuje si předchozí požadavky -> každý požadavek je nezávislý
    - Řešení: Cookies mebo sessions
  - Textový - jednoduchá čitelnost požadavků a odpovědí
  - Klient-server - klient požadavky, serever zpracování požadavků + odpovědi
  - Rozšiřitelnost/flexibilita - Podpora různých metod (GET, POST, PUT, ...)
  - Podpora HTTPS - bezpečný přenos dat

## Jak vypadá HTTP požadavek?

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozila/5.0
Accept: text/html
```

- Typ požadavku (GET)
- URI (Iniform resource identifier): Cílová URL (index.html)
- Verze protokolu HTTP (HTTP/1.1 nebo HTTP/2)
- Halvičky - typ požadovaného obsahu (Accept) nebo identifikace prohlížeče (User-Agent)
- Tělo požadavku:
  - pouze u některých metod (př.: POST)
  - pro zasílání dat (formuláře)

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

- GET
  - získání dat ze serveru (pouze získává)
  - Data se posílají v URL - parametry: `?query=value`
- PUT
  - Nahrazení nebo aktualizování dat na serveru
  - Pokud zdroj neexistuje, může ho vytvořit
  - Často jako aktualizace dat v REST API
- CONNECT
  - Vytvoření tunelového spojení, například pro šifrované připojení (HTTPS)

## K čemu se používají metody POST, DELETE, OPTIONS?

- POST
  - Odeslání dat na server (formuláře)
  - Data odesílána v těle požadavku
  - Vytváří nové zdroje nebo spouští serverové operace
- DELETE
  - smazání dat na serveru
- OPTIONS
  - Zjištění podporovaných metod serveru a umožňuje zjistit, co je povoleno (užitečné pro CORS)

## Jaké je rozdělení HTTP stavů?

- imformativní
- úspěšné
- přesměrování
- chyby klienta
- chyby serveru

## K čemu se používají stavy HTTP 2xx, 3xx?

- 2xx: Úspěšné zpracování požadavku
  - 200 OK: Požadavek úspěšně zpracován
  - 201 Created: Zdroj byl vytvořen
- 3xx: Přesměrování klienta někam
  - 301 Moved: Zdroj byl trvale přesunut
  - 302 Found: Dočasné přesměrování

## K čemu se používají stavy HTTP 1xx, 5xx, 4xx?

- 1xx: imformace o pažadvku (přijal požadavek a čeká na další informace)
  - 100 Continue
- 4xx: Chyba na straně klienta (404 page not found - špatná url)
  - 404 Not Found: Požadovaný zdroj neexistuje
  - 401 Unauthorized: Nutná autentizace
  - 418 I'm teapot: Vtip k 1. dubnu
- 5xx: Chyba na straně serveru (500 internal server error)
  - 500 Internal Server Error: Neočekávaná chyba na serveru
  - 503 Service Unavailable: Server je dočasně nedostupný

## Co je session a k čemu se využívá?

- ukládá stav mezi více požadavky uživatele
- Server uchovává data (přihlašovací údaje) po dobu trvání relace
- obvykle pomocí identifikátoru uloženého v Cookies
- užívá se k:
  - autentizaci
  - správu nákupního košíku
  - atd.

## Co jsou cookies a k čemu se využívají?

- malé textové soubory uložené v prohlížeči
- slouží k uchovávání informací
- Příklady:
  - Přihlášení uživatele
  - Uživatelská preference
  - Sledování aktivit (pro marketing)
  - Nastavení vzhledu stránky (světlý a tmavý režim)

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
  - Interoperabilita mezi různými systémy (podpora různých platforem)
  - Široká podpora standardů
- Nevýhody:
  - Nároky na zabezpečení (bezpečností rizika)
  - Potřeba internetového připojení

## Co je SPA? Výhody a nevýhody

- Single Page Aplication: Aplikace načte jednu stránku a dynamicky mění obsah.
- Výhody:
  - Plynulá uživatelská zkušenost
  - Rychlá interaktivita
  - Méně zatížení serveru
- Nevýhody:
  - Horší SEO
  - Dlouhá doba při prvním načtení

## Co je MVC? Výhody a nevýhody

- Model-View-Controller: Architektonický návrh pro strukturování softwarových aplikací
  - Model - logika dat
    - Obsahuje logiku pro manipulaci s daty aplikace
    - Komunikuje s databází a zpracovává obchodní logiku
  - View - uživatelské rozhraní
    - Prezentuje data uživateli
    - Zajišťuje vykreslení UI na základě dat z modelu
  - Controller - Zprostředkovává interakci mezi Modelem a View
    - Řídí tok mezi Modelem a View
    - Zpracovává vstupy uživatele a rozhoduje, jaká data se mají zobrazit
- Výhody:
  - Lepší organizace kódu
  - Odělení rezentace a logiky usnadňuje týmový vývoj
  - Zlepšuje možnost opakovatelného použití komponent
- Nevýhoda
  - Komplexita u malých projektů
  - Může být složitějšá na pochopení a implementaci

## Co je FCP? Výhody a nevýhody

- First Contentful Paint
- Metrika měřící čas od načtení stránky do okamžiku, kdy prohlížeč zobrazí první obsah (text, obrázek,...)
- Výhody:
  - Umožňuje měřit rychlost vykreslováníobsahu
  - Důležitý pro hodnocení uživatelské zkušenosti
- Nevýhody:
  - Nezohledňuje Interaktivitu stránky
  - Může být ovlivněno sítí nebo výkonem zařízení

## Jaké vlastnosti má Javascript?

- Dynamický - měnění obsahu v reálném čase
- interpretovaný - spouští se v prohlížeči bez nutnsti kompilace
- Slabě typovaný - proměnné mohou měnit svůj datový typ (z čísla se stane text)
- podporuje asynchronní operace (načítání dat z API)
- Událostně řízený - reaguje na akce uživatele (kliknutí, pohyb myši, ...)
- Pracuje s DOM (manipulace s prvky HTML a styly CSS)
- Běží na straně serveru (Node.js) i klienta

## Co jsou události a k čemu se využívají? Příklad události

- akce k interaktivnímu chování webových stránek
- mohou nastat také při provádění kódu
- příklady:
  - kliknutí, stisk klávesy, pohyb myši, načtení stránky atd.

```
document.querySelector("button").addEventListener("click", () => {
    alert("Button Click")
});
```

## K čemu slouží DOM? Jak se s tím pracuje v JS

- Document Object Manager
- představuje strukturu HTML (nebo XML) stránky jako strom objeků
  - každý prvek ve stránce je uzel v tomto stromě
- Pomocí DOM lze manipulovat s prvky
- Změna textu:
  ```
  document.getElementById("element").innerText = "Nový text";
  ```
- Změna stylu:
  ```
  document.getElementById("headline").style.color = "#906090";
  ```
- Přidání nových prvků
  ```
  let newElement = document.createElement("p");
  newElement.innerText = "Nový odstavec";
  document.body.appendChild(newElement);
  ```

## Jakým způsobem se ukládají hesla?

- Nikdy neukládat hesla jako prostý text
- přímé uložení hesla do databáze (bez hashování) je bezpečnostní riziko
- ukládat pomocí

  - Hashování - hesla se převedou na hash (bcrypt nebo Argon2)
  - Salting (Solení) - Přidává se náhodný řetězec (salt) k heslu před hashováním, aby se zabránilo útoku hrubou silou

- hesla se ukládají pomocí hashovacích funkcí (bcrypt)
- hash hesla se uloží do databáze
- Příklad:
  - heslo `password123` může po hashování a solení být převedeno na `$2a$10$W3BjUe4p...` (výstup z bcrypt)

## Co je CSRF attack?

- Cross-Site Request Forgery
- útočník přiměje uživatele odelat nechtěný požadavek na server, kde je uživatel přihlášen
- Jak útok funguje:
  1. Uživatel se přihlási na legitimní web (např.: banka)
  2. Útočník naláká uživatele na podvodný web
  3. Podvodný web pošle skrytý požadavek na server banky jménem uživatele (např.: převod peněz)
- Ochrana proti CSRF:
  - Tokeny CSRF
    - Náhodné hodnoty generované serverem a přidávané k formulářům
  - Kontrola refereru
    - Server ověřuje, zda požadavek přichází z důvěryhodného zdroje

## K čemu se využívá JWT token?

- JSON Web Token
- k bezpečnému přenosu informací mez klientem a serverem v JSON formátu
- autentizace uživatelů
- Jak JWT funguje?
  1. Klient pošle přihlašovací údaje serveru
  2. Server ověří údaje a vytvoří JWT obsahující informace o uživateli
  3. Klient ukládá token (Cookies/localStorage) a přikládá jej k dalším požadavkům na server
- Struktura JWT
  - skládá se z 3 částí oddělených tečkami: `header`.`payload`.`signature`
  - Header - imformace o algoritmu a typu tokenu
  - Payload - Data (např.: uživatelské ID, role,...)
  - Signature - Kryptografický podpis ověřující integritu dat
- Výhody
  - Bezpečný přenos informací
  - Nezávislý na stavu serveru (bez potřeby sessions)
- Nevýhody
  - Pokud je token odcizen, útočník získá přístup do systému po celou dobu platnosti tokenu
