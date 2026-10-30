import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console() 

# Aufgabe 1
# Erstelle ein Dictionary, das die Noten eines Schülers in verschiedenen Fächern speichert.
# Schreibe ein Programm, das die Note für ein Fach abfragt und ausgibt. Verwende get() und
# fange mit if und else einen Fehler ab, falls das Fach nicht existiert.

noten = {
    "Mathe": 2,
    "Deutsch" : 1,
    "Englisch" : 3
}

fach = input("Gib ein Fach ein: ")

note = noten.get(fach)

if note is not None:
    print(f"Die Note in {fach} ist {note}")
else:
    print("Dieses Fach existiert nicht im Dictionary.")

# AUfgabe 2
# Erstelle ein Dictionary mit den Namen von 5 Mitarbeitern und ihren Positionen in einem Betrieb.
# Schreibe ein Programm, das einen Benutzer nach dem Namen fragt und entweder die Position des 
# Mitarbeiters ausgibt oder "Mitarbeiter konnte nicht gefunden werden" anzeigt, wenn der Name
# nicht im Dicitonary vorhanden ist (benutze get() )

Mitarbeitern = {
    "Andrii" : "Chef",
    "Ivan": "Manager",
    "Natalia": "HR",
    "Oleh": "Developer",
    "Maxim": "QA"
}

inp = input("Gib einen Name oder Position ein: ")

for name, position in Mitarbeitern.items():
    if position == inp:
        print(f"Name: {name} , Position: {position}")
        break
else:
        print("Gibt es kein Mitarbeiter in Dictionary")

# Aufgabe 3
# Erstelle ein Dictionary, das 5 Lebensmittel und ihre Preise enthält. Baue eine Funktion, die neue Produkte und
# deren Preise speichert. Erweitere deine Funktion, indem du nach einem 
# Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde, soll der Artikel gespeichert werden und einen
# Standardpreis von 0 zurückgegeben

produkte = {
    "Brot": 2,
    "Milch": 1.5,
    "Apfel": 3,
    "Käse": 4,
    "Wasser": 1
}

def prod(produkte):
    inp = input("Gib die Produkte ein ")
    ware = produkte.get(inp)
    if ware is not None:
        print(f"Price: {ware}")
    else:
        produkte[inp] = 0
        print(f"{inp} kostet: {produkte[inp]}")

prod(produkte)
# Aufgabe 4
# Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen. Schreibe ein Programm, das durch die Schlüssel des 
# Dictionaries iteriert und nur die Namen der Personen ausgibt

namenUndAlter = {
    "Andrii" : 28,
     "Ivan": 25,
     "Natalia": 26,
     "Oleh": 30,
     "Maxim": 18
}

for name in namenUndAlter:
    print(name)

# Aufgabe 5 
# Gegeben ist ein Dictionary, das die Lagerbestände eines Geschäfts speichert.
# Schreibe ein Programm, das alle Artilkel ausgibt, die aktuell im Lager sind
# (Tipp: Schlüssel mit Wert > 0)

articles = {
    "Screws": 10000,
    "Wood": 0,
    "Nails": 100,
    "toolkit": 10,
    "scanner": 2,
    "paper": 0,
}

for name in articles:
    if articles[name] > 0:
        print(name)

# Aufgabe 6
# Du findest ein Dictionary mit Ländern als Schlüssel und deren Bevölkerungszahlen als Wert.
# Schreibe ein Programm, das die Länder nach Namen sortiert und in alphabetischer Reihenfolge
# die Namen ausgibt

countries = {
    "Deutschland": 85000000,
    "Frankreich": 68000000,
    "Spanien": 47000000,
    "Polen": 36000000,
}

for name in sorted(countries):
    print(name, countries[name])

# Aufgabe 7
# Erstelle ein Dictionary mit fünf Tieren und deren Anzahl im Lager aus einem Tierhandel. Schreibe ein
# Programm, das die Summe aller Werte im Dicitonary berechnet und ausgibt.

tiere = {
    "Hund" : 5,
    "Katze" : 10,
    "Affe" : 3
}
total = 0
for value in tiere.values():
    total += value
print(total)

gesamt = sum(tiere.values())

print(gesamt)

# Aufgabe 8
# Du findest ein Dictionary mit den Namen von Schülern als Schlüssel und deren Noten als Werte.
# Schreibe ein Programm, das den Notendurchschnitt aller Noten berechnet (benutze values() und keys())

students = {
    "Alan": 1,
    "Jacques": 6,
    "Gerhard": 1,
    "Willi": 4,
    "Susanne":2
}

note = sum(students.values()) / len(students)
print(note)

# Aufgabe 9
# Erstelle ein Dictionary, das den Umsatz verschiedener Filialen eines Unternehmens speichert.
# Nutze den Filialnamen als Schlüssel und den Umsatz als Wert.
# Schreibe ein Programm, das die Filiale mit dem höchsten Umsatz identifiziert und den Namen
# der Filiale sowie den Umsatz ausgibt

unternehmen = {
    "Filiale_A1": 5000444,
    "Filiale_B2": 1500000,
    "Filiale_C3": 5900023,
    "Filiale_D4": 70000,
    "Filiale_E5": 99999999,
}

max =  max(unternehmen.values())

for name in unternehmen:
    if unternehmen[name] == max:
        print(name, max ) 


# Aufgabe 10
# Erstelle ein Dictionary, welches die Preise von 5 Artikeln speichert. Verwende items() um durch die Schlüssel Wert Paare zu iterieren
# und alle Artikel, deren Preis über 10 € liegt, auszugeben

produkte = {
     "Brot": 20,
     "Milch": 15,
     "Apfel": 13,
     "Käse": 4,
     "Wasser": 10
}

for name, price in produkte.items():
    if price > 10:
        print(name, price)
# Aufgabe 11
# Erstelle ein Dictionary, das die Punktzahl von Spielern in einem Videospiel speichert.
# Der Spielername ist der Schlüssel und die Punktzahl der Wert. Schreibe ein Programmm, welches den Spieler ausgibt,
# der die höchste Punktzahl hat. (Benutze items())

spilers = {
    "Allan" : 104,
    "Andrii": 991,
    "Somebody": 992
}
max = max(spilers.values())
for name, res in spilers.items():
    if res == max:
        print("The best is ",name," with result ", res)

# AUfgabe 12
# Erstelle ein Dictionary mit Informationen über einen Film (z.B.: Titel, Jahr, Genre). Schreibe ein Programm dass das Dictionary 
# mithilfe von update um die Bewertung des Films erweitert.

films = {
    "Name" : "Avatar",
    "Jahr" :  "2025",
    "Genre" : "Fantasy"
}

films.update({"Bewertung":9.0})
print(films)

# Aufgabe 13
# Erstelle 2 Dictionaries die jeweils den Lagerbestand in zwei verschiedenen Filialen eines Geschäfts darstellen.
# Schreibe ein Programm das den Lagerbestand der beiden Filialen zusammenführt (benutze Update) und gib das 
# kombinierte Dicitonary aus

filiale_West = {
    "Wasser" : 1000,
    "Cola": 200,
}


filiale_Ost = {
    "Bier": 9999
}

gesamt = filiale_West.copy()
gesamt.update(filiale_Ost)
print(gesamt)

# Aufgabe 14
# Du findest ein Dictionary mit Produkten und ihren Preisen Schreibe ein Programm, das den Benutzer auffordert, den Preis eines Produkts zu
# aktualisieren. Verwende update() um das Produkt mit dem neuen Preis im Dicitonary zu aktualisieren.

produkte = {
     "Brot": 20,
     "Milch": 15,
     "Apfel": 13,
     "Käse": 4,
     "Wasser": 10
}

produkt = input("Geben Sie das Produkt ein, das Sie ändern möchten ")
updata = input("Geben Sie price die ändern möchte")

for ware in produkte.keys():
    if ware == produkt:
        produkte.update({ware: updata})

print(produkte)

# Aufgabe 15
# Erstelle ein Dictionary mit dem Namen von drei Klassenkameraden und deren Handynummern. Schreibe ein Programm,
# dass das Dicitonary mit clear() leert und überprüft, ob es nun leer ist.

Klassenkameraden  = {
    "Allan" : 88888,
    "Andrii": 77777,
    "Somebody": 66666
}

Klassenkameraden.clear()

if not Klassenkameraden:
    print("Das Dictionary ist leer.")
else:
    print("Das Dictionary ist nicht leer.")

# Aufgabe 16
# Du findest ein Dictionary mit 5 Studenten und deren Noten.

students = {
    "Alan": 1,
    "Jacques": 6,
    "Gerhard": 1,
    "Willi": 4,
    "Susanne":2
}

# Aufgabe 16.1
# Erstelle eine Funktion, die einen neuen Studenten und seine Note nach der Eingabe eines Benutzers in dem Dictionary speichert, allerdings nur, wenn weniger als 
# 5 Studenten in dem Dictionary gespeichert sind.

new_student = input("Geben Sie neue Name \n")
new_note = input("Geben Sie neue Note \n")

# Aufgabe 16.2
# Falls schon 5 Studenten in dem Dicitonary gespeichert sind, weise darauf hin, dass schon 5 Studenten gespeichert sind und
# stelle den Benutzer vor eine Wahl, ob er das aktuelle Dictionary löschen möchte um den neuen Studenten dort abspeichern zu können, gib währenddessen den
# Notendurchschnitt aller Studenten aus.

if len(students) >= 5:
    print("Schon 5 Studenten haben wir")
    note = sum(students.values()) / len(students)
    print(note)

while True:
    wahl = input("Möchten Sie das aktuelle Dictionary löschen? Geben Sie Y or N \n")
    if wahl == "Y" or  wahl == "N":
        break
    else:
        print("Falscher Wert \n")

# Aufgabe 16.3
# Wenn der Benutzer sich gegen das Löschen der Daten entscheidet, beende das Programm.

if wahl == "N":
    print("Bis bald, program ist geschloßen \n")

# Aufgabe 16.4
# Wenn der Benutzer die Daten löschen will, rufe eine neue Funktion die du jetzt neu bauen wirst auf, 
# welche als Parameter die Daten des neuen Studenten als Dictionary empfängt,

def newfunk (name, note) :

    # Aufgabe 16.5
    # lösche in deiner neuen Funktion, die du sinnvoll benannt hast alle Daten in dem Dicitonary student_graduations

    students.clear()

    # Aufgabe 16.6
    # Stelle den Benutzer noch einmal in deiner neuen Funktion vor eine Auswahl, ob er die Daten die du Übergeben hast, in dem Dictionary student_graduations speichern will.   
    while True:
        
        # Entscheidet sich der Benutzer die Daten zu speichern, speichere die neuen Daten in dem Dicitonary und gib dein Dictionary aus.

        wahl = input("Möchten Sie neue Student speichern? Geben Sie Y or N \n")
        if wahl == "Y" or  wahl == "N":
            break
        else:
            print("Falscher Wert ")

    if wahl == "Y":
        students.update({name:note})
        print(students)
    else:
         # Entscheidet sich der Nutzer gegen das speichern, sollte ein leeres Objekt angezeigt werden
        print(students)



if wahl == "Y":
    newfunk(new_student,new_note)
