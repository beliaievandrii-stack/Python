import urllib.request
import json
import random
from datetime import datetime

API_RACES = "https://www.dnd5eapi.co/api/races"
API_CLASSES = "https://www.dnd5eapi.co/api/classes"


# Aufgabe 1 und 2:
# Zufällige Rasse und Klasse über die API auswählen
def get_random_item(api_url):
    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read().decode("utf-8"))

    items = data["results"]
    return random.choice(items)["name"]


# Aufgabe 3:
# Zufällige Charakterattribute erstellen
def generate_attributes():
    attributes = {
        "Stärke": random.randint(1, 50),
        "Intelligenz": random.randint(1, 50),
        "Agilität": random.randint(1, 50)
    }

    return attributes


# Aufgabe 4:
# Einen Charakter erstellen und den Zeitstempel speichern
def create_character():
    character = {
        "Rasse": get_random_item(API_RACES),
        "Klasse": get_random_item(API_CLASSES),
        "Attribute": generate_attributes(),
        "Erstellt_am": datetime.now().isoformat(timespec="seconds")
    }

    return character


# Aufgabe 5:
# Mehrere Charaktere in einer JSON-Datei speichern
def save_character(character, filename="characters.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            characters = json.load(file)
    except FileNotFoundError:
        characters = []
    except json.JSONDecodeError:
        characters = []

    characters.append(character)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(characters, file, indent=4, ensure_ascii=False)


# Hauptprogramm
anzahl = int(input("Wie viele Charaktere möchtest du erstellen? "))

for i in range(anzahl):
    try:
        character = create_character()
        save_character(character)

        print(f"\nCharakter {i + 1} wurde erstellt:")
        print(json.dumps(character, indent=4, ensure_ascii=False))

    except Exception as error:
        print(f"Fehler beim Erstellen des Charakters: {error}")

print("\nAlle erfolgreich erstellten Charaktere wurden gespeichert!")
