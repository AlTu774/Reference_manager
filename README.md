# Lahdehallinta
![GHA workflow badge](https://github.com/AlTu774/Lahdehallinta/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/AlTu774/Lahdehallinta/graph/badge.svg?token=OSUNJZUSTT)](https://codecov.io/gh/AlTu774/Lahdehallinta)


[Linkki sovellukseen](https://lahdehallintasovellus.fly.dev/)
## Product backlog
Linkki taulukkoon joka sisältää product backlogin (ja sprint backlogin):
[Product backlog/Sprint backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/mseppi_ad_helsinki_fi/EQIaYfH__HREsC9fgOU2kWkBzfAX5RP9uAoUaCY_Hi62qg)

## Definition of done
- Hyväksymiskriteerit saavutettu
- Integroitu tuotantoversioon
- Automaattiset regressiotestit menevät läpi
- Toiminnallisuuden yksikkötestit menevät läpi
- Käyttäjän hyväksymistesti suoritettu storylle

.env-tiedosto ohjeet kehittäjille:

```
DATABASE_URL=postgresql:///<postgres-käyttäjänimesi>
SECRET_KEY=<numerosarja, esim. python-komennolla secrets.token_hex(16)>
```
