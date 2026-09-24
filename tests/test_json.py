from pathlib import Path
import json

from src.json_processing import add_heroes_and_sort


DATA = Path(__file__).resolve().parents[1] / "data" / "SuperHero.json"
OUTPUT = Path(__file__).resolve().parents[1] / "output" / "superhero_new.json"


def test_add_two_heroes_and_sort():
    data = json.loads(DATA.read_text(encoding="utf-8"))

    heroes = [
        {
            "name": "Shadow Fox",
            "age": 24,
            "secretIdentity": "Alex Gray",
            "powers": ["Invisibility", "Night vision"]
        },
        {
            "name": "Solar Knight",
            "age": 50,
            "secretIdentity": "Leo Stone",
            "powers": ["Flight", "Solar energy", "Energy shield"]
        }
    ]

    result = add_heroes_and_sort(data, heroes)

    assert len(result["members"]) == 5
    ages = [hero["age"] for hero in result["members"]]
    assert ages == sorted(ages)


def test_output_file_is_sorted():
    data = json.loads(OUTPUT.read_text(encoding="utf-8"))
    ages = [hero["age"] for hero in data["members"]]

    assert len(data["members"]) == 5
    assert ages == sorted(ages)
