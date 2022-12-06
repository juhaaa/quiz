# Ohjelmistotekniikka

## Harjoituksia

Tämä repositorio on Helsingin yliopiston kurssin ohjelmistotekniikka palautuksia varten.
Repositoriossa on viikkoharjoitusten palautuksia sekä harjoitustyö.

## Harjoitustyö

Kurssilla toteutan harjoitustyönä visailu-ohjelman, aiheena maantiede.
Sovelluksessa käyttäjä vastaa pääkaupunkiaiheisiin kysymyksiin.
Kysymykset on tallennettu tietokantaan ja pelissä tarpeeksi hyvät pisteet
tallennetaan .csv tiedostoon.

- [Changelog](python-quiz/dokumentaatio"changelog.md)

- [Vaatimusmaarittely](python-quiz/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](python-quiz/dokumentaatio/tuntikirjanpito.md)

- [Arkkitehtuuri](python-quiz/dokumentaatio/arkkitehtuuri.md)

## Ohjelman käyttö

Kirjoita seuraavat komennot:

'''bash
poetry install

poetry run invoke start
'''

## Muita komentoja

1. Testit

'''bash
poetry run invoke test
'''

2. Testiraportti

'''bash
poetry run invoke coverage-report
'''

3. Pylint

'''bash
poetry run invoke lint
'''


		

