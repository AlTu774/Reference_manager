# Reference manager
![GHA workflow badge](https://github.com/AlTu774/Lahdehallinta/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/AlTu774/Lahdehallinta/graph/badge.svg?token=OSUNJZUSTT)](https://codecov.io/gh/AlTu774/Lahdehallinta)


[Link to the application](https://lahdehallintasovellus.fly.dev/)
## Product backlog
Link to the product backlog (and sprint backlog):
[Product backlog/Sprint backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/mseppi_ad_helsinki_fi/EQIaYfH__HREsC9fgOU2kWkBzfAX5RP9uAoUaCY_Hi62qg)

## Definition of done
- Acceptance criteria met
- Integrated into the production version
- Automated regression tests pass
- Unit tests for functionality pass
- User acceptance test conducted for the story

.env file instructions for developers:

```
DATABASE_URL=postgresql:///<postgres-username>
SECRET_KEY=<number series, e.g. with a Python command secrets.token_hex(16)>
```
