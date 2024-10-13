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

    # Ask the user to enter their notes
    nieuw_note = input("Schrijf een note voor dit dag: ")

    # Open 'dagen.txt' and append the new note with the date
    with open('dagen.txt', 'a') as file:
        file.write(f"Datum: {datum}\n")
        file.write(f"Note: {nieuw_note}\n")
        file.write("-" * 40 + "\n")  # Separator for readability
        print(f"Note Opgeslagen {datum}!")


def lees_note():
    # Get the date from the user in DD/MM/YY format
    datum = input("Voer een datum in (DD/MM/YY): ")

    try:
        # Open 'dagen.txt' to read the content
        with open('dagen.txt', 'r') as file:
            note = file.readlines()

        # Flag to track if any notes for the specified date were found
        found = False
        print(f"\nNote voor {datum}:\n")
        for i in range(len(note)):
            if note[i].strip() == f"Datum: {datum}":
                gevonden = True
                # Print the note and continue until the next separator
                for j in range(i, len(note)):
                    if note[j].strip() == "-" * 40:
                        break
                    print(note[j], end='')
                print("\n" + "-" * 40)

        if not gevonden:
            print(f"Geen note gevonden voor {datum}.")
    except FileNotFoundError:
        print("Geen note gevonden voor dit dag")


# Call the diary function to start the menu
dagboek()
