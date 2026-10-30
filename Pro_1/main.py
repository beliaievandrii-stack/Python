from get_all_users import get_all_users
from save_user import save_user
import os
from update import update
from entfernen import entfernen

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Aufgabe 2
# Baut eine Hauptdatei, die ein Programm mit einem Hauptmenü startet mit folgenden Auswahlmöglichkeiten:
# 1: Mitglieder Liste lesen
# 2: Mitglied hinzufügen
# 3: Mitglied bearbeiten
# 4: Mitglied entfernen

while True:
    clear_console();

    auswahl = int(input("1: Mitglieder Liste lesen \n"
                 "2: Mitglied hinzufügen \n"
                 "3: Mitglied bearbeiten \n" 
                 "4: Mitglied entfernen \n"
                 "0: Exit  \n"))
    # Aufgabe 4
# Gebt alle Mitglieder in der Konsole aus, wenn die Auswahl auf Mitglieder Liste lesen fällt.
# Gebt die Werte Name, Alter und Email aus.
    if auswahl == 1:
        users = get_all_users()
        print("\n--- Mitgliederliste ---")
        for user in users:
            print("Name: ",user['name'],
                  "\nAlter: ", user['alter'],
                "\nEmail: ", user['email'])
        warte = input("Geben Sie Enter aus")
    
    elif auswahl == 2:
        users = get_all_users()
        save_user(users)
        warte = input("Geben Sie Enter aus")

    elif auswahl == 3:
        users = get_all_users()
        update(users)
        warte = input("Geben Sie Enter aus")
    
    elif auswahl == 4:
        users = get_all_users()
        entfernen(users)
        warte = input("Geben Sie Enter aus")

    elif auswahl == 0:
        break