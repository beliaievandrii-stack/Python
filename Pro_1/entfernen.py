import json

def entfernen(users):
    user = input("Welcher Benutzer soll entfernt werden?")
    
    for person in users:
        if person["name"] == user:
            users.remove(person)
            print("Benutzer wurde entfernt!")
            with open("Pro_1/users.json", "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
            break
            
    else:
        print("Fehler: Benutzer existiert nicht!")