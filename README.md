# HealthFlow Egypt backend localization


> **HealthFlow Payer System — Egypt context**
>
> This repository is maintained under [HealthFlow Payer System](https://github.com/HealthFlow-Payer-System), an Egypt-focused health-insurance platform built on openIMIS foundations. Egypt-specific localization is applied at the assembly and module boundaries; consult the repository-specific configuration and deployment documentation for the capabilities enabled here.

This package is the first Tier B foundation for Egypt-specific HealthFlow Payer behavior. It is intentionally independent of proprietary services and contains only AGPL-compatible, presentation and validation-layer helpers that can later be wired into the openIMIS backend assembly.

The initial increment validates Egyptian National IDs structurally: fourteen digits, century and Gregorian birth date, governorate code, sequence/gender parity, and the Luhn check digit. It also validates Egyptian mobile numbers in E.164 form. The module does not change GraphQL, REST, FHIR, database, or configuration identifiers.

Future increments will add a Django app integration, EGP currency defaults, the 27-governorate location seed hierarchy, Arabic and transliterated name fields, and an asynchronous E-KYC adapter boundary. Any Digital Egypt connector must remain an external service communicating over an API boundary.
