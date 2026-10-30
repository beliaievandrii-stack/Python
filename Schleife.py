import os
import time
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

zahl = 0
zahl1 = 1

while True:
    zahl += zahl1
    zahl1 += 1
    if zahl1 > 100:
        break

print(zahl, "\n")


name = input("Geben Sie ihr Name aus\n")

if len(name) > 2 and " " not in name :
    print(name ," ist gültig")
else:
    print("Name ist ungültig ")

Waren = ["Apfel", "Cola", "Kartofel"]

kauf = input("Welsche ware haben Sie schon gekauft \n")

if kauf in Waren:
    Waren.remove(kauf)
else:
    print("Nicht gefunden.\n")

print(Waren)

liste = []

while True:
    inp = int(input("Geben Sie Noten aus"))
    if inp <= 6 and inp > 0:
        liste.append(inp)

    elif inp == 0:
        break
    else:
        print("ungültige Note\n")
        continue
    

print(liste, "die Durchschnittsnote ist ", sum(liste)/len(liste))



import random

nummer = random.randint(1,20)

print("Erraten Sie die Zahl \n")


while True:
    zahl = int(input("Ihre Zahl\n"))
    if nummer == zahl:
        print("Du hast gewinnen\n")
        break
    
    elif nummer < zahl:
        print("Die zahl ist kleiner\n")
    
    elif nummer > zahl:
        print("Die zahl ist großer\n")

liste = []
while True:
    zahl = int(input("Geben Sie bitte ihre zahl aus wenn Sie beenden möchten geben Sie bitte 0\n"))
    
    if zahl == 0:
        print(liste)
        break

    if zahl > 0:
        liste.append(zahl)
 

namen = ["Lukas", "Anna", "Felix", "Laura", "Jonas", "Mia", "Leon", "Sophie"]

while True:
    name = input("Geben Sie bitte Ihr Name aus wenn Sie beenden möchten geben Sie bitte 0\n")
    if name == "0":
        break
    for i in range(4):
        time.sleep(1)
        print("bearbeitung. Noch ", 3 - i,"Second")

    if name in namen:
        i = namen.index(name)
        namen[i] += " ist 25 Jahre alt"
        print(namen[i])
    else:
        print("der Name ist in der Liste nicht vorhanden ")
    
    