
import random

def evenofoneven():
    print("Welkom bij het spel Even of Oneven!")

    # kiest 'even' of 'oneven'
    kies = input("Kies even of oneven: ").lower()


    if kies not in ["even", "oneven"]:
        print("Scelta non valida. Riprova!")
        return

    # kies een getal in
    speler_nummer = int(input("Kies een nummer (0-10): "))

    # de computer genereert een getal
    computer_nummer = random.randint(0, 10)
    print(f"Het heeft dit nummer gekozen: {computer_nummer}")

    # bereken de som van de twee getallen
    som = speler_nummer + computer_nummer
    print(f"Het som is: {som}")

    # bepaal of de som even of oneven is
    if som % 2 == 0:
        risultaat = "even"
    else:
        risultaat = "oneven"

    # Controleren wie heeft gewonnen
    if kies == risultaat:
        print(f"Je hebt {kies} gekozen, Hoera! Je hebt gewonnen")
    else:
        print(f"Je hebt {kies} gekozen, Jammer, je hebt verloren")


evenofoneven()
