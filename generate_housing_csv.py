#!/usr/bin/env python3
"""Download the public USA_Housing dataset and export a 300-row regression CSV."""
from pathlib import Path
from urllib.request import urlopen
import csv, io

SOURCE_URL = "https://raw.githubusercontent.com/mofasa-20/USA-Housing/main/USA_Housing.csv"
OUTPUT = Path(__file__).resolve().parent / "data" / "usa_housing_300.csv"


def main() -> None:
    with urlopen(SOURCE_URL, timeout=30) as response:
        raw = response.read().decode("utf-8")
    rows = list(csv.DictReader(io.StringIO(raw)))[:300]
    if len(rows) != 300:
        raise RuntimeError(f"Expected 300 records, received {len(rows)}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "record_id", "annual_income_usd", "house_age_years",
        "number_of_rooms", "number_of_bedrooms", "area_population",
        "house_price_usd", "house_area_proxy_sqft", "address",
    ]
    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for index, row in enumerate(rows, start=1):
            # The public source has room count, not measured square footage.
            # This transparent proxy is useful for regression demonstrations:
            # estimated area = 350 sq ft per room.
            rooms = float(row["Area No of Rooms"])
            writer.writerow({
                "record_id": index,
                "annual_income_usd": row["Area Income"],
                "house_age_years": row["Area House Age"],
                "number_of_rooms": row["Area No of Rooms"],
                "number_of_bedrooms": row["Area No of Bedrooms"],
                "area_population": row["Area Population"],
                "house_price_usd": row["Price"],
                "house_area_proxy_sqft": f"{rooms * 350:.2f}",
                "address": row.get("Address", ""),
            })

    print(f"Wrote {len(rows)} records to {OUTPUT}")


if __name__ == "__main__":
    main()
