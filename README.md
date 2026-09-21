# USA housing price linear regression data

This repository contains a reproducible generator for a 300-record CSV used to study the relationship between housing price and related factors.

## Generate the CSV

```bash
python generate_housing_csv.py
```

The output is `data/usa_housing_300.csv` with 300 observations and these fields:

- `annual_income_usd`: area annual income in USD
- `house_age_years`: house age
- `number_of_rooms` and `number_of_bedrooms`
- `area_population`
- `house_price_usd`: target variable
- `house_area_proxy_sqft`: transparent proxy calculated as `number_of_rooms * 350`; the source dataset does not provide measured square footage
- `address`: source address when available

## Source and limitations

The records are the first 300 rows downloaded from the public `USA_Housing.csv` dataset:

<https://raw.githubusercontent.com/mofasa-20/USA-Housing/main/USA_Housing.csv>

The source is commonly used for regression demonstrations and is not an official property transaction registry. In particular, its income and population fields are area-level variables, and the square-foot field in the exported CSV is an estimated proxy rather than a measured property area. Use the proxy accordingly, or replace it with measured square footage when available.

The generator intentionally downloads the source instead of embedding a silently modified copy, so the CSV can be regenerated and audited.
