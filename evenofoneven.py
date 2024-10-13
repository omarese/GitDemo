import random

def evenofoneven():
    print("Welkom bij het spel Even of Oneven!")

    # Il giocatore sceglie "pari" o "dispari"
    kies = input("Kies even of oneven: ").lower()

    # Controlla che l'input sia valido
    if kies not in ["even", "oneven"]:
        print("Scelta non valida. Riprova!")
        return

    # Il giocatore inserisce un numero
    speler_nummer = int(input("Kies een nummer (0-10): "))

    # Il computer genera un numero casuale
    computer_nummer = random.randint(0, 10)
    print(f"Het heeft dit nummer gekozen: {computer_nummer}")

    # Calcola la somma dei due numeri
    som = speler_nummer + computer_nummer
    print(f"Het som is: {som}")

    # Determina se la somma è pari o dispari
    if som % 2 == 0:
        risultaat = "even"
    else:
        risultaat = "oneven"

    # Controlla se il giocatore ha vinto
    if kies == risultaat:
        print(f"Je hebt {kies} gekozen, Hoera! Je hebt gewonnen")
    else:
        print(f"Je hebt {kies} gekozen, Jammer, je hebt verloren")

# Avvia il gioco
evenofoneven()
