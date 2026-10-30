import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_console()

squares = [x**2 for x in range(1, 21)]

print(squares)

zahlen = [10, 15, 23, 42, 55, 68, 73, 80, 87, 93, 96, 99, 110, 111, 120]

zahlen1 = [ x for x in zahlen if x % 2 == 0]

print(zahlen1)

satz = "Zehn zahme Ziegen zogen zehn Zentner Zucker zum Zoo"

liste = [x for x in satz if x in "aeiou"]
print(liste)

liste = [x for x in range(1, 101) if x % 5 == 0 or x % 7 == 0]
print(liste)

woerterliste = ['Apfel', 'Ei', 'Banane', 'Traube', 'Ananas', 'Kiwi', 'Uwe', 'Rettungswagen', 'Schlafmütze']
liste = [ x for x in woerterliste if len(x) < 5]
print(liste)

satz = "Ihr werdet besser und besser. Hört nicht auf zu lernen, ihr seid richtig gut <3"

liste = [len(x) for x in satz.split() ]
print(liste)

zahlen = [1, 2, 3]
buchstaben = ['A', 'B', 'C']

liste = [(z,b) for z in zahlen for b in buchstaben]
print(liste)


import random

vornamen = ["Anna", "Ben", "Clara", "David", "Eva", "Felix", "Greta", "Hannes", "Iris", "Jonas",
            "Klara", "Lukas", "Maria", "Nina", "Oskar", "Paula", "Quentin", "Rosa", "Sebastian", "Tina",
            "Uwe", "Vera", "Walter", "Xenia", "Yannik", "Zoe"]

nachnamen = ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", 
             "Schulz", "Hoffmann", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", 
             "Neumann", "Schwarz", "Zimmermann", "Krüger", "Hartmann", "Lange", "Werner", "Schmitz"]

namen_liste = [f"{random.choice(vornamen)} {random.choice(nachnamen)}" for _ in range(1000)]

name = input("Ihre Name")

