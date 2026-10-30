import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# Aufgabe 1
# Füge mit der `add()` Methode ein weiteres Tier, z.B. "Elefant", hinzu
# tiere = {"Hund", "Katze", "Vogel"}

# tiere.add("Elefant")
# print(tiere)

# # Aufgabe 2
# # Entferne die Zahl 3 mit der `remove()` Methode
# zahlen = {1, 2, 3, 4, 5}

# zahlen.remove(3)
# print(zahlen)
# # Aufgabe 3
# # Verwende `discard()` für die Farbe "blau" und gib dein set aus
# farben = {"rot", "gelb", "grün", "schwarz", "weiß"}

# farben.discard("blau")
# print(farben)

# Aufgabe 4
# Verwende `union()`, um ein Set mit allen Früchten und Gemüsen zu erstellen und gib es aus
# obst = {"Apfel", "Banane", "Kirsche", "Pflaume", "Mango"}
# gemüse = {"Karotte", "Tomate", "Salat", "Brokkoli", "Kartoffel"}

# gesamt = obst.union(gemüse)
# print(gesamt)

# # Aufgabe 5
# # Verwende `intersection()` für die gemeinsamen Städte heruaszufiltern und gib sie aus
# staedte = {"Berlin", "Hamburg", "München", "Köln", "Stuttgart"}
# staedte2 = {"München", "Düsseldorf", "Berlin", "Leipzig"}

# gesamt = staedte.intersection(staedte2)
# print(gesamt)
# Aufgabe 6
# Verwende `difference()`, um die Sportarten zu finden, die nur in deinem Lieblings-Set sind
sportarten_studio1 = {"Fußball", "Basketball", "Tennis"}
hasssport = {"Tennis", "Golf", "Schwimmen"}

Lieblings_Set = sportarten_studio1.difference(hasssport)
print(Lieblings_Set)
# sportarten_studio = sportarten_studio1.difference(sportarten_studio2)
# print(sportarten_studio)
# # Aufgabe 7
# # Finde die Tiere, die nur in einem der beiden Gehege vorkommen (nicht in beiden). 

# gehege_1 = {"Löwe", "Tiger", "Elefant", "Zebra"}
# gehege_2 = {"Tiger", "Elefant", "Giraffe", "Nashorn"}

# gehege = gehege_1.difference(gehege_2)
# print(gehege)