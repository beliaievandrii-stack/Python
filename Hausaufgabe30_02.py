zahl_int = 1
zahl_float = 1.1
zahl_str = "zahl"
zahl_bool = True

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

def aufgabe2 (zahl1, zahl2):
    addition = zahl1 + zahl2
    Suobtraktion = zahl1 - zahl2
    Multiplikation = zahl1 * zahl2
    division = zahl1 / zahl2
    modulo = zahl1 % zahl2
    print(f"addition = {addition} \nSuobtraktion = {Suobtraktion} \nMultiplikation = {Multiplikation} \ndivision = {division} \nmodulo = {modulo}")

def aufgabe3(zahl3):
    zahl3 = int(zahl3)
    print("aufgabe3 =",zahl3)
    if zahl3 % 2 == 0:
        print("Die Zahl ist grade")
    else:
        print("Die Zahl ist ungrade")

def aufgabe4():
    alter = int(input(f"Geben Sie Ihres Alter aus: \n"))
    if alter < 18:
        print("Sie dürfen nicht in Dissco (Eintritt ab 18)\n")
    else:
        print("Zeigen Sie Ihres Ausweiß\n")

def aufgabe5(zahl1,zahl2,zahl3):
    result = max(zahl1,zahl2,zahl3)
    print(f"die größte Zahl ist: {result}")

def aufgabe6(zahl1,zahl2):
    if zahl1 == zahl2:
         print("sie gleich")
    elif zahl1 > zahl2:
        print("Zahl1 ist großer als Zahl2\n")
    else:
        print("Zahl2 ist großer als Zahl1\n")

def aufgabe7():
    rolle = str(input("Geben Sie Ihre Rolle aus\n"))
    password = str(input("Geben Sie Ihre Password aus\n"))
    if rolle == "Admin" or rolle == "Superuser" or password == "secret":
        print("Zutritt gestattet\n")
    else:
        print("der Zugriff verweigert\n")

def aufgabe8():
    zahl1 = int(input("Geben Sie Ihre Zahl aus\n"))
    if zahl1 < 10:
        print("Die Zahl ist kleiner 10\n")
    else:
        print("Die Zahl ist großer oder gleich 10\n")

def aufgabe9():
    zahl1 = int(input("Geben Sie Ihre Zahl aus\n"))
    if zahl1 < 0 or zahl1 > 100:
        print("Die Zahl passt")
    else:
        print("Die Zahl passt nicht")

def aufgabe10():
    passwort = input("Gib ein Passwort ein (mindestens 8 Zeichen): ")

    if len(passwort) < 8:
        return False, "Das Passwort ist zu kurz (mindestens 8 Zeichen)."

    sonderzeichen = "@#$%"

    hat_zahl = any(zeichen.isdigit() for zeichen in passwort)
    hat_sonderzeichen = any(zeichen in sonderzeichen for zeichen in passwort)

    if hat_zahl or hat_sonderzeichen:
        return True, "Passwort ist gültig."
    else:
        return False, "Das Passwort muss mindestens eine Zahl oder ein Sonderzeichen (@, #, $, %) enthalten."


# 👉 ВАЖНО: вызвать функцию
 
 

#aufgabe2(10,5)
#aufgabe3(zahl_float)
#aufgabe4()
#aufgabe5(10,20,25)
#aufgabe6(10,15)
#aufgabe7()
#aufgabe8()
#aufgabe9()
ergebnis, meldung = aufgabe10()
print(meldung)
