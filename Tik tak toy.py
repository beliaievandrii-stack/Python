import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



spielfeld = [[' ' for _ in range(3)] for _ in range(3)]
win = []
def zeichne_spielfeld (spielfeld):
    clear_console() 
    for x in spielfeld:
        print(" | ".join(x))
        print("-" * 9)

zeichne_spielfeld(spielfeld)


def gewonen(spielfeld, aktueller_spieler):
    if (
        spielfeld[0][0] == spielfeld[0][1] == spielfeld[0][2] == aktueller_spieler or
        spielfeld[1][0] == spielfeld[1][1] == spielfeld[1][2] == aktueller_spieler or
        spielfeld[2][0] == spielfeld[2][1] == spielfeld[2][2] == aktueller_spieler or

  
        spielfeld[0][0] == spielfeld[1][0] == spielfeld[2][0] == aktueller_spieler or
        spielfeld[0][1] == spielfeld[1][1] == spielfeld[2][1] == aktueller_spieler or
        spielfeld[0][2] == spielfeld[1][2] == spielfeld[2][2] == aktueller_spieler or

        spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] == aktueller_spieler or
        spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] == aktueller_spieler
    ):
        return True
    return False

def starte_spiel(spielfeld,aktueller_spieler):
    while True:        
        zeile = int(input("Wähle eine Zeile Vertikal (1-3): ")) - 1
        zeile2 = int(input("Wähle eine Zeile Horizontal (1-3): ")) - 1
        
        if zeile not in [0,1,2] or zeile2 not in [0,1,2]:
                print("Falscher Wert!")
                continue
        if spielfeld[zeile][zeile2] == " " :
                spielfeld[zeile][zeile2] = aktueller_spieler
                zeichne_spielfeld(spielfeld)
                
                if not any(" " in Unentschieden for Unentschieden in spielfeld):
                    print("Unentschieden")
                    exit()

                break
        else:
                print("Dieses Feld ist bereits belegt!")
        

while True:

            for i in range(2):
                i = "X" if i == 0 else "O"
                starte_spiel(spielfeld, i)
                if gewonen(spielfeld, i):
                    zeichne_spielfeld(spielfeld)
                    print("Player", i, "gewonen!")
                    exit()
