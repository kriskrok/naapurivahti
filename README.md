[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)

# Naapurivahti-sovellus avuksi taloon ja puutarhaan


#### [Tietokantakuvaus](./documentation/tietokanta.md)
#### [Sovellus Herokussa](https://naapurivahti.herokuapp.com/)

## Tilannetietoa

Sovelluksesta on toteutettuna tällä hetkellä etusivun navigointinäkymässä listatut näkymät pl. Omat tiedot näkymä. Sovelluksessa on mahdollista luoda uusia vahtivuoroja jotka tallentuvat tietokantaan. Kaikki tietokantaan tallennetut vahtivuorot näkyvät käyttäjälle vuorolistaus näkymässä (etusivu -> vuorot -> vuorolistaus).

Sovellukseen on toteutettu kirjautumismahdollisuus. Kirjautumattomalle käyttäjälle näytetään ainoastaan sovelluksen etusivu. Navigointi muualla sovelluksessa ohjaa kirjautumattoman käyttäjän kirjautumissivulle.

Sovellukseen ei ole vielä toteutettu mahdollisuutta luoda käyttäjätunnuksia. Sovellusta voi tästä huolimatta koestaa testitunnuksilla:

- Tunnus: ```Maija```
- Salasana: ```sateenkaarikala```

Sovellukseen on toteutettu yksi laajempi yhteenvetokysely jota hyödynnetään raporttilistausnäkymässä
(etusivu -> raportit -> listaa raportit). Raportteja ei ole mahdollista vielä luoda sovelluksen käyttöliittymän kautta. Raportteja voi kuitenkin luoda sovelluksessa luomalla uusia vuoroja, sillä kaikille sovellukseen lisätyille vuorolle luodaan automaagisesti vuoroon liittyvä raportti. Näiden raporttien ilmiintymistä pääsee niin halutessaanihastelemaan edellä mainitussa raporttilistausnäkymässä.

Tietokantakuvauksen mukaisista tauluista on tehty ORM-toteutukset. Näitä ei vielä kaikin osin tosin ole otettu sovelluksessa käyttöön. Luodut toteutukset löytyvät vastuualueittain jaoteltuna omissa kansioissaan. Esimerkiksi, käyttäjää kuvaavan Accounts-toteutuksen voi kaivella ihmeteltäväksi navigoimalla repositoriossa -> application/auth/models.py

## Aihekuvaus

Naapurivahti&#8480;-sovellus auttaa pitämään kirjaa taloyhtiössä tapahtuvista sattumuksista. Sovellus auttaa myös organisoimaan taloyhtiön sisäistä Naapuripartio&#8480;-toimintaa. Sovellukseen voi kirjata ja myöhemmin tarkastella havaittuja tapahtumia ja ilmiöitä.

Sovellus auttaa pitämään kirjaa sekä organisoimaan taloyhtiön naapuripartio-toimintaa. Sovellukseen voi kirjata havaintoja partioinnin aikana kohdatuista tapahtumista sekä ilmiöistä.

Taloyhtiön asukkaat jaetaan kahteen kastiin, taloyhtiön hallituksen jäseniin ja riviasukkaisiin. Hallituksen jäsenet voivat toimia sovelluksessa Suurmartan (ylläpitäjän) roolissa

## Toiminnallisuudet

- Käyttäjä voi luoda palveluun tunnuksen syöttämällä sähköpostiosoitteen ja salasanan sekä rekisteröitymisavaimen
- Uuden käyttäjätunnuksen luominen vaatii olemassa olevalta suurmarttatilillä luodun rekisteröitymisavaimen syöttämistä
- Käyttäjä voi kirjautua palveluun syöttämällä sähköpostiosoitteen ja salasanan
- Käyttäjä voi lisätä itsestään profiilitietoja
- Käyttäjä voi lähettää palveluun kuvan jota voi käyttää profiilikuvana
- Vahtivuorolistan teko
- Henkilökohtaisen vahtivuorolistan listaus
- Vahtivuorolistan listaus

## Käyttäjäroolit

- Sovelluksessa on tavallisia käyttäjiä
- Sovelluksessa on ylläpitäjän oikeudet omaavia suurmarttoja
- Suurmartta voi luoda vahtivuoroja ja lisätä käyttäjiä vahtivuoroon

## Vahtivuorot&trade;

- Vahtivuoroon sisältyy aloitus- ja lopetuspvmäärät kellonaikoineen
- Vahtivuoroon voi kuulua käyttäjiä
- Vahtivuoroon voi kuulua korkeintaan yksi(1) raportti
- Raporttiin voi kuulua havaintoja
- Havaintoon voi kuulua yksi tai useampi kuva

- Vahtivuorosta on nähtävissä raportti (näkymä)
- Raportit ovat kaikkien käyttäjien tarkasteltavissa
- Vahtivuoroon liittyvää raporttia voivat muokata ainoastaan vuoroon liitetyt asukkaat sekä suurmartat

---