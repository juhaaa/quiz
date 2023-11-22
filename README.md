# Ohjelmistotekniikka

## Harjoituksia

Tämä repositorio on Helsingin yliopiston kurssin ohjelmistotekniikka palautuksia varten.
Repositoriossa on viikkoharjoitusten palautuksia sekä harjoitustyö.

## Harjoitustyö

Kurssilla toteutan harjoitustyönä visailu-ohjelman, aiheena maantiede.
Sovelluksessa käyttäjä vastaa pääkaupunkiaiheisiin kysymyksiin.
Kysymykset on tallennettu tietokantaan ja pelissä tarpeeksi hyvät pisteet
tallennetaan .csv tiedostoon.

- [Changelog](python-quiz/dokumentaatio/changelog.md)

- [Vaatimusmaarittely](python-quiz/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](python-quiz/dokumentaatio/tuntikirjanpito.md)

- [Arkkitehtuuri](python-quiz/dokumentaatio/arkkitehtuuri.md)

- [Release](https://github.com/juhaaa/ot-harjoitustyo/releases)

- [Testikattavuus](python-quiz/dokumentaatio/testidokumentti.md)

## Ohjelman käyttö

Navigoi ensin python-quiz kansioon ja kirjoita seuraavat komennot terminaalissa:

```bash
poetry install

poetry run invoke start
```

- Ohjelmassa navigoidaan nuolinäppäimillä
- Valinta vahvistetaan joko Enterillä tai välilyönnillä

## Muita komentoja

1. Testit

```bash
poetry run invoke test
```

2. Testiraportti

```bash
poetry run invoke coverage-report
```

3. Pylint

```bash
poetry run invoke lint
```

## Käyttöohje

- Ohjelma käynnistyy seuraavassa näkymässä:

![](.python-quiz/dokumentaatio/kuvat/start.png)

- Voit liikkua ylös tai alas nuolinäppäimillä ja hyväksyä valinnan enterillä tai välilyönnillä.
- Play aloittaa uuden pelin.
- Higscores tulostaa näytölle huipputulokset.
- Quit lopettaa ohjelman suorituksen.

## Pelaaminen

- Kun olet aloittanut pelin, esittää peli sinulle 10 pääkaupunkiaiheista kysymystä,
joihin sinun pitään yrittää vastata oikein 4 vaihtoehdosta.
- Voit valita kaupungin nuolinäppäimillä ylös tai alas, ja hyväksyä valinnan enterillä
tai välilyönnillä.
- Alareunassa näkyy ajankohtainen pistetilanne. 

![](.python-quiz/dokumentaatio/kuvat/game.png)

- Mikäli sait pelin päättyessä tarpeeksi pisteitä saadaksesi nimesi top-10 listalle,
kysyy peli sinulta nimeä. Voit syöttää max 15 merkkiä.

![](.python-quiz/dokumentaatio/kuvat/user_name.png) 


## Muita ohjeita

- Pelin aikana on hyvä välttää terminaali-ikkunan koon pienentämistä.
		

