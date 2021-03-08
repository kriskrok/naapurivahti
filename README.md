[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)

# Naapurivahti-sovellus avuksi taloon ja puutarhaan


#### [Tietokantakuvaus](./documentation/tietokanta.md)
#### [Sovellus Herokussa](https://naapurivahti.herokuapp.com/)
#### [Käyttöönotto](https://github.com/kriskrok/naapurivahti/blob/main/documentation/kayttoonotto.md)
#### [Käyttötapaukset](https://github.com/kriskrok/naapurivahti/blob/main/documentation/kayttotapaukset.md)

## Sovellus taloyhtiön sisäisten vahtivuorojen organisointiin ja kirjaamiseen

Sovelluksesta on toteutettuna tällä hetkellä etusivun navigointinäkymässä listatut näkymät pl. Omat tiedot -näkymä. Sovellukseen toteutettu toiminnallisuus on kuvattu tarkemmin käyttötapauksina [täällä](https://github.com/kriskrok/naapurivahti/blob/main/documentation/kayttotapaukset.md). 

Sovellukseen on toteutettu kirjautumismahdollisuus. Kirjautumattomalle käyttäjälle näytetään ainoastaan sovelluksen etusivu. Navigointi muualla sovelluksessa ohjaa kirjautumattoman käyttäjän kirjautumissivulle.

Sovelluksen kautta on mahdollista luoda käyttäjätunnus. Sovelluksen kaikkien käyttäjien salasanoista tallennetaan ainoastaan hash-arvo. Unohtunutta salasanaa ei siis voida mahdollisten unohdusten sattuessa palauttamaan vaan käyttäjän tulee tällöin luoda uusi tunnus.


Sovellukseen ei ole vielä toteutettu mahdollisuutta luoda uusia admin-käyttäjätunnuksia. Sovellusta voi tästä huolimatta ihastella seuraavilla admin-testitunnuksilla:

- Tunnus: ```Maija```
- Salasana: ```sateenkaarikala```


Kaikista tietokantakuvauksen mukaisista tauluista on tehty ORM-toteutukset. Näitä ei vielä kaikin osin tosin ole otettu sovelluksessa käyttöön. Sovelluksessa ei ole vielä toiminnallisuutta luodun Pictures-luokan käyttöönotolle. Luodut toteutukset löytyvät vastuualueittain jaoteltuna omissa kansioissaan. Esimerkiksi, käyttäjää kuvaavan Accounts-toteutuksen voi kaivella ihmeteltäväksi navigoimalla repositoriossa -> application/auth/models.py

## Aihekuvaus

Naapurivahti&#8480;-sovellus auttaa pitämään kirjaa taloyhtiössä tapahtuvista sattumuksista. Sovellus auttaa myös organisoimaan taloyhtiön sisäistä Naapuripartio&#8480;-toimintaa. Sovellukseen voi kirjata ja myöhemmin tarkastella havaittuja tapahtumia ja ilmiöitä.

Sovellus auttaa pitämään kirjaa sekä organisoimaan taloyhtiön naapuripartio-toimintaa. Sovellukseen voi kirjata havaintoja partioinnin aikana kohdatuista tapahtumista sekä ilmiöistä.

Taloyhtiön asukkaat jaetaan kahteen kastiin, taloyhtiön hallituksen jäseniin ja riviasukkaisiin. Hallituksen jäsenet voivat toimia sovelluksessa Suurmartan (ylläpitäjän) roolissa

## Käyttäjäroolit
### Kuvaus
- Sovelluksessa on tavallisia käyttäjiä
- Sovelluksessa on ylläpitäjän oikeudet omaavia suurmarttoja
- Suurmartta voi tulevaisuudessa luoda vahtivuoroja ja lisätä käyttäjiä vahtivuoroon

## Vahtivuorot&trade;
### Kuvaus
- Vahtivuoroon sisältyy aloitus- ja lopetuspvmäärät kellonaikoineen
- Vahtivuoroon voi tulevaisuudessa kuulua käyttäjiä
- Vahtivuoroon voi kuulua korkeintaan yksi(1) raportti
- Raporttiin voi kuulua havaintoja
- Havaintoon voi tulevaisuudessa kuulua yksi tai useampi kuva
- Vahtivuorosta on nähtävissä raportti (näkymä)
- Raportit ovat kaikkien käyttäjien tarkasteltavissa

---

### Sovelluksen jatkokehityskohteet
- CSRF-tokenit käyttöön ensitilassa
- Sovellukseen rekisteröityminen vaatii erillisen rekisteröitymisavaimen
- Rekisteröitymisavaimia voivat luoda suurmarttatilin haltijat
- Käyttäjä voi lisätä ja päivittää itsestään profiilitietoja
- Käyttäjä voi lähettää palveluun kuvia
- Kuva voi liittyä joko tehtyyn havaintoon tai käyttäjän omiin profiilitietoihin
- Vahtivuorolistan rajaaminen käyttäjittäin
- Suurmartta voi nimetä ja lisätä käyttäjiä vahtivuoroon
- Vahtivuoroon liittyvää raporttia voi muokata ainoastaan vuoroon liitetyt käyttäjät sekä suurmartat

---