
print("Welkom Bij OmarStore")
print("Kies Een App:")
print("1. GokSpel")
print("2. Galgje")
print("3. Verlaten")

while True:
    kies = input("Voer Het Nummer Van Het App: ")

    if kies == "1":
        import GokSpel
    elif kies == "2":
        import Galgje
    elif kies == "3":
        print("Dank Je en Tot Volgende Keer!")
        break
    else:
        print("Dat is geen optie, sorry")
