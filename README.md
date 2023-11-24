# Lahdehallinta
![GHA workflow badge](https://github.com/AlTu774/Lahdehallinta/workflows/CI/badge.svg)


[Linkki sovellukseen](https://lahdehallintasovellus.fly.dev/)
## Product backlog
Linkki taulukkoon joka sisältää product backlogin (ja sprint backlogin):
[Product backlog/Sprint backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/mseppi_ad_helsinki_fi/EQIaYfH__HREsC9fgOU2kWkBV-iNEZ-LmgMrs8Rvv2edrQ?e=hAhW0N)

## Definition of done
- Hyväksymiskriteerit saavutettu
- Integroitu tuotantoversioon
- Automaattiset regressiotestit menevät läpi
- Toiminnallisuuden yksikkötestit menevät läpi
- Käyttäjän hyväksymistesti suoritettu storylle

(Ensin kirjan lisäys:
- nimi
- kirjoittaja
- julkaisuvuosi
- julkaisija)

.env-tiedosto ohjeet kehittäjille:

```
DATABASE_URL=postgresql:///<postgres-käyttäjänimesi>
SECRET_KEY=<numerosarja, esim. python-komennolla secrets.token_hex(16)>
```
