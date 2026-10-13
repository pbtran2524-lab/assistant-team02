import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[1] / "data" / "offices.csv"

def get_office_by_name(name: str):
    with open(CSV_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["name"].strip() == name:
                return row
    return None

def test_lookup_admissions_office():
    office = get_office_by_name("Admissions Office")
    assert office is not None, "Cannot find Admissions Office in CSV"
    assert office["room"] == "A.101"

def test_lookup_health_center():
    office = get_office_by_name("Health Center")
    assert office is not None, "Cannot find Health Center in CSV"
    assert office["room"] == "A.102"

