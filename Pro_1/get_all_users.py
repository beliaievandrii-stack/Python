# Aufgabe 3
# Baut eine Datei mit dem Namen get_all_users.py welche alle Mitglieder in einer Funktion aus der JSON Datei
# users.json liest und eine Variable erzeugt, die den Wert der Mitgliederliste enthält und in die Hauptdatei
# importiert werden kann
import json


def get_all_users():

    with open("Pro_1/users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    return users