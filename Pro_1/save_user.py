import json

def save_user(users):
    name = input("Name: ")
    alter = int(input("Alter: "))
    email = input("Email: ")
    hobby = input("Hobby: ")

    new_user = {
        "name": name,
        "alter":  alter,
        "email": email,
        "hobby": hobby
    }

    users.append(new_user)
    with open("Pro_1/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

    print("Mitglied wurde gespeichert.")