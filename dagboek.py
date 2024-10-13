def dagboek():
    while True:

        print("\nDagBoek KeuzeMenu:")
        print("1. Schrijf een note")
        print("2. Lees een note")
        print("3. Verlaten")

        kies = input("Kies een optie (1/2/3): ")

        if kies == '1':
            schrijf_note()
        elif kies == '2':
            lees_note()
        elif kies == '3':
            print("Verlaten. . . ")
            import main
        else:
            print("Dat is geen optie, kies 1, 2, of 3")


def schrijf_note():

    datum = input("Voer een datum in (DD/MM/YY): ")

    nieuw_note = input("Schrijf een note voor dit dag: ")


    with open('dagen.txt', 'a') as file:
        file.write(f"Datum: {datum}\n")
        file.write(f"Note: {nieuw_note}\n")
        file.write("-" * 40 + "\n")
        print(f"Note Opgeslagen {datum}!")


def lees_note():
    # verkrijg de datum in het formaat DD/MM/JJ
    datum = input("Voer een datum in (DD/MM/YY): ")

    try:
        # open 'dagen.txt' om de inhoud te lezen
        with open('dagen.txt', 'r') as file:
            note = file.readlines()

        # vlag om bij te houden of er noten voor de opgegeven datum zijn gevonden
        gevonden = False
        print(f"\nNote voor {datum}:\n")
        for i in range(len(note)):
            if note[i].strip() == f"Datum: {datum}":
                gevonden = True
                # Druk de note af en ga verder tot de volgende
                for j in range(i, len(note)):
                    if note[j].strip() == "-" * 40:
                        break
                    print(note[j], end='')
                print("\n" + "-" * 40)

        if not gevonden:
            print(f"Geen note gevonden voor {datum}.")
    except FileNotFoundError:
        print("Geen note gevonden voor dit dag")



dagboek()
