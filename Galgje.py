import random
import time

def woord_lezer(file):
    with open(file, 'r') as f:
        woorden = f.readlines()
    woorden = [woord.strip() for woord in woorden]
    return woorden

def woord_kiezer(woorden):
    return random.choice(woorden)

def geheim_woord(woord, geraden_letters):
    woord_ingebruik = []
    for letter in woord:
        if letter in geraden_letters:
            woord_ingebruik.append(letter)
        else:
            woord_ingebruik.append('_')
    return ''.join(woord_ingebruik)

def galgje():
    woorden = woord_lezer('woorden.txt')
    galgje_woord = woord_kiezer(woorden)
    geraden_letters = []
    pogingen = 6

    print('Welkom Bij Het Galgje Spel!')
    while pogingen > 0:
        woord_ingebruik = geheim_woord(galgje_woord, geraden_letters)
        print(f'Het woord is: {woord_ingebruik}')
        print(f'Resterende pogingen: {pogingen}')

        if "_" not in woord_ingebruik:
            print('Gefeliciteerd! Je hebt het woord geraden!')
            break

        letter = input('Gok een letter: ').lower()

        if letter in geraden_letters:
            print('Je hebt dit letter al geraden!')
        elif letter in galgje_woord:
            print('Goed gedaan! De letter zit in het woord.')
            geraden_letters.append(letter)
        else:
            print('Helaas, de letter zit niet in het woord.')
            geraden_letters.append(letter)
            pogingen -= 1

    if pogingen == 0:
        print(f'Je hebt verloren! Het woord was: {galgje_woord}')

    while True:
        print("Wil je nog spelen?")
        print("1: Ja! nog eentje")
        print("2: Terug naar de Menu")

        scelta = input("Kies hier: ")

        if scelta == "1":
            print("Start het spel opnieuw...")
            time.sleep(2)
            galgje()
        elif scelta == "2":
            print("Terug naar de Menu...")
            time.sleep(2)
            import main
            break
        else:
            print("Geen optie, probeer opnieuw.")

galgje()
