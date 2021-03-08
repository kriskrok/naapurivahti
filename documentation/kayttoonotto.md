## Käyttö- ja asennusohjeet
### Asennus
---
### Paikallinen asennus

1. Sovelluksen lähdekoodi on vapaasti saatavilla osoitteesta [https://github.com/kriskok/naapurivahti](https://github.com/kriskrok/naapurivahti).
2. Sovellus tarvitsee toimiakseen Python3 asennuksen. Yhteensopivuutta 3.9 vanhempien versioiden kanssa ei ole koestettu.
3. Sovelluksen tarvitsemat riippuvuudet löytyvät listattuna '[requirements.txt](https://github.com/kriskrok/naapurivahti/blob/main/requirements.txt)' tiedostosta. Asennus hoitunee kivoiten pip-paketinhallintatyökalulla ja ottamalla käyttöön Python virtuaaliympäristön.
4. Sovellus käynnistyy käskyttämällä projektin juuressa `python3 run.py` jonka jälkeen käyttöliittymää pääsee ihastelemaan navigoimalla selaimella osoitteeseen `localhost:5000`

---

### Sovellus Herokussa
Herokun käyttämää Gunicorn-palvelinta ei käytetä paikallisessa asennuksessa ja tämän johdosta sitä ei ole listattuna requirements.txt tiedostossa. Herokun käynnistystä pääsee tarvittaessa sörkkimään muokkaamalla projektin juuresta löytyvää '[Procfile](https://github.com/kriskrok/naapurivahti/blob/main/Procfile)'-tiedostoa. 

Herokun [komentorivityökalu](https://devcenter.heroku.com/articles/heroku-cli#getting-started) mahdollistaa sovelluksen tuoreimpien muutosten päivittämisen Herokuun vaivattomasti. Asenna tämä tarvittaessa edellä olevan linkin takaa löytyvien ohjeiden mukaisesti.

Sovellus tunnistaa olevansa Herokussa HEROKU-ympäristömuuttujan avustuksella. Moisen saa luotua Herokun komentorivityökalun turvin loitsimalla `heroku config:set HEROKU=1`. Tämän jälkeen sovellus osaa ottaa käyttöönsä Herokun tarjoaman postgresql tietokanta-palvelun automaagisesti.

---