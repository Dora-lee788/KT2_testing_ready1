import json


def load_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def add_heroes_and_sort(data, heroes):
    data["members"].extend(heroes)
    data["members"].sort(key=lambda hero: hero["age"])
    return data


def save_data(data, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    data = load_data("data/SuperHero.json")

    new_heroes = [
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

    data = add_heroes_and_sort(data, new_heroes)
    save_data(data, "output/superhero_new.json")

    print("Супергерои отсортированы по возрасту.")
