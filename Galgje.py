
import random
import time

def woord_lezer(file):
    #functie om woorden uit een bestand te lezen
    with open(file, 'r') as f:
        woorden = f.readlines()
    woorden = [woord.strip() for woord in woorden]  # verwijder witruimtes van elk woord
    return woorden

def woord_kiezer(woorden):
    # functie om een woord uit de lijst te kiezen
    return random.choice(woorden)

def geheim_woord(woord, geraden_letters):
    # functie om de weergave van het geheime woord te genereren
    woord_ingebruik = []
    for letter in woord:
        if letter in geraden_letters:
            woord_ingebruik.append(letter)  # voeg de letter toe als deze is geraden
        else:
            woord_ingebruik.append('_')  # voeg '_' toe als de letter niet is geraden
    return ''.join(woord_ingebruik)

def galgje():

    woorden = woord_lezer('woorden.txt')  # lees de woorden uit het bestand
    galgje_woord = woord_kiezer(woorden)  # kies een willekeurig woord
    geraden_letters = []
    pogingen = 6  # aantal pogingen

    print('Welkom Bij Het Galgje Spel!')
    while pogingen > 0:
        woord_ingebruik = geheim_woord(galgje_woord, geraden_letters)
        print(f'Het woord is: {woord_ingebruik}')  # toon het woord met geraden letters
        print(f'Resterende pogingen: {pogingen}')  # toon het aantal resterende pogingen

        if "_" not in woord_ingebruik:
            print('Gefeliciteerd! Je hebt het woord geraden!')
            break

        letter = input('Gok een letter: ').lower()  # vraag de speler om een letter

        if letter in geraden_letters:
            print('Je hebt dit letter al geraden!')  # gegeven letter is al geraden
        elif letter in galgje_woord:
            print('Goed gedaan! De letter zit in het woord.')  # gegeven letter zit in het woord
            geraden_letters.append(letter)  # voeg de letter toe aan de lijst van geraden letters
        else:
            print('Helaas, de letter zit niet in het woord.')  # gegeven letter zit niet in het woord
            geraden_letters.append(letter)  # voeg de letter toe aan de lijst van geraden letters
            pogingen -= 1

    if pogingen == 0:
        print(f'Je hebt verloren! Het woord was: {galgje_woord}')

    while True:
        print("Wil je nog spelen?")  # vraag of ze opnieuw willen spelen
        print("1: Ja! nog eentje")
        print("2: Terug naar de Menu")

        keuze = input("Kies hier: ")  # vraag om een keuze

        if keuze == "1":
            print("Start het spel opnieuw...")  # herstart het spel
            time.sleep(2)
            galgje()
        elif keuze == "2":
            print("Terug naar de Menu...")  # ga terug naar het menu
            time.sleep(2)
            import main
            break
        else:
            print("Geen optie, probeer opnieuw.")

galgje()
