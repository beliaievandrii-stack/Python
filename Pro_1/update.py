import json

def update(users):
    user = input("Welcher Benutzer soll aktualisiert werden?")
    
    for person in users:

        if person["name"] == user:
            

            person["alter"] = int(input("Neues Alter eingeben: "))
            person["email"] = input("Neue Email eingeben: ")
            person["hobby"] = input("Neues Hobby eingeben: ")

            print("Benutzer wurde aktualisiert!")
            with open("Pro_1/users.json", "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
            break
            
    else:
        print("Fehler: Benutzer existiert nicht!")