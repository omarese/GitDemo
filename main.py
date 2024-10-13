
print("Welkom Bij OmarStore")
print("Kies Een App:")
print("1. GokSpel")
print("2. Galgje")
print("3. Dagboek")
print("4. Even of Oneven")
print("5. Verlaten")

while True:
    kies = input("Voer Het Nummer Van Het App: ")

    if kies == "1":
        import GokSpel
    elif kies == "2":
        import Galgje
    elif kies == "3":
        import dagboek
    elif kies == "4":
        import evenofoneven
    elif kies == "5":
        print("Dank Je en Tot Volgende Keer!")
        break
    else:
        print("Dat is geen optie, sorry")
