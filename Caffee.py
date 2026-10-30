import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

coffee_prices = {1: 1.99, 2: 2.99, 3: 3.99}
coffee_names = {1: "Kleiner Kaffee", 2: "Mittlerer Kaffee", 3: "Großer Kaffee"}
order_counts = {1: 0, 2: 0, 3: 0}

def change_price():
    while True:
        
        pos = int(input("Welche Position möchten Sie ändern? (1-3): "))
        if 0 < pos <= len(coffee_prices):
            new_price = float(input(f"Schreiben Sie neues Preis für {coffee_names[pos]}: "))
            coffee_prices[pos] = new_price
            print("Preis geändert!")
            return 
        else:
            print("Falsche Position!")



def choice_menu():
    while True:

        print("\n--- Herzlich willkommen ---")
        print(f"1. Kleiner Kaffee   ({coffee_prices[1]}$)")
        print(f"2. Mittlerer Kaffee ({coffee_prices[2]}$)")
        print(f"3. Großer Kaffee    ({coffee_prices[3]}$)")
        print("4. Admin: Preis ändern")
        print("0. Bestellung fertig")
        
        try:
            decid = int(input("\nBitte wählen: "))
            if 0 <= decid <= 4:
                return decid
            print("Fehler: 0-4 wählen.")
        except ValueError:
            print("Fehler: Zahl eingeben!")

total_rechnung = 0.0

while True:
    
    choice = choice_menu()

    if choice == 0:
        break
    
    if choice == 4:
        change_price()
        continue 

    anzahl = int(input(f"Wie viel Stück {coffee_names[choice]}? "))
    
    order_counts[choice] += anzahl
    current_cost = round(coffee_prices[choice] * anzahl, 2)
    total_rechnung = round(total_rechnung + current_cost, 2)

    print(f"Hinzugefügt: {anzahl}x {coffee_names[choice]}")
    

    input("Drücken Sie die Eingabetaste, um fortzufahren...")
    clear_console()

print(f"\nIhre Bestellung ist fertig! Gesamt: {total_rechnung}$")