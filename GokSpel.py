import random
import time


def GokSpel():
    print("Welkom bij het gokspel!")
    max_cijfer = 10
    geheim_nummer = random.randint(1, max_cijfer)  # genereer een geheim nummer
    aantal_kansen = int(input("Hoeveel kansen wil je hebben om het juiste nummer te raden? "))

    print(f"Je moet het getal raden tussen 1 en {max_cijfer}. Je hebt {aantal_kansen} kansen.")

    for poging in range(1, aantal_kansen + 1):  # loop door de aantal pogingen
        gok = int(input(f"Poging {poging}: Raad het nummer: "))  # vraag om een gok

        # Controleer of de gok correct is
        if gok == geheim_nummer:
            print(f"Gefeliciteerd! Je hebt het nummer {geheim_nummer} geraden in {poging} poging(en)!")
            break
        elif gok < geheim_nummer:
            print("Het nummer is hoger.")  # geef aanwijzing dat het nummer hoger is
        else:
            print("Het nummer is lager.")  # geef aanwijzing dat het nummer lager is


    if gok != geheim_nummer:
        print(f"Helaas, je hebt geen kansen meer. Het juiste nummer was {geheim_nummer}.")


    while True:
        print("Wil je nog spelen?")
        print("1: Ja! nog eentje")
        print("2: Terug naar de Menu")

        kies = input("Kies hier: ")  # vraag om een keuze

        # Verwerk de keuze
        if kies == "1":
            print("Start het spel opnieuw...")
            time.sleep(2)
            GokSpel()
            break  #
        elif kies == "2":
            print("Terug naar de Menu...")
            time.sleep(2)
            import main
            break
        else:
            print("Geen optie, probeer opnieuw.")


GokSpel()
