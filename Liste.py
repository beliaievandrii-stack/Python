import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

liste1 = ["Appfel", "Mango", "Ananas"]
liste2 = [5, 10, 20]
liste3 = [13.13, 12.12, 11.11 ]
liste4 = ["1", "11", "111"]
liste5 = ["2", "22", "222"]
# Aufgabe 1

liste1.append("Lemon")
liste1.append("Kiwi")
liste1.append("Melone")
print("Aufgabe 2 :", liste1)

liste1.extend(liste2)
print("Aufgabe 3 :", liste1)

liste1.insert(2, "Andrii")
liste1.insert(3, "Chrisoph")
liste1.insert(5, "Roman")

print("Aufgabe 4 :", liste1)

liste4.remove("1")
print("Aufgabe 5 :", liste4)

liste1.pop()
print("Aufgabe 6 :", liste1)

liste5.clear()
print("Aufgabe 7 :", liste5)

liste2.sort(reverse=True)
print("Aufgabe 8 :", liste2)

liste4_kopie = liste4.copy()
print(f"Aufgabe 9 : Das ist die Kopie von Liste 4: {liste4_kopie}")

liste4_kopie.append("NEU")
print("Aufgabe 10 : Das ist die Kopie", liste4_kopie)
print("Aufgabe 10 : Das ist Original ", liste4)

anzahl_alex = liste1.count("Alex")
print(f"Aufgabe 11: Alex trifft {anzahl_alex} mal")

anzahl_mein_name = liste1.count("Andrii9")
print(f"Aufgabe 12: Mien Name trifft {anzahl_mein_name} mal")

anzahl_3 = liste2.count(3)
print(f"Aufgabe 13: die Zahl 3 trifft {anzahl_3} mal")

liste3.sort()
print("Aufgabe 14 (liste3 sorted):", liste3)

