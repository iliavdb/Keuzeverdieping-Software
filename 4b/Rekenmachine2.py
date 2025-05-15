def optellen(a, b):
    return a + b

def aftrekken(a, b):
    return a - b

def vermenigvuldigen(a, b):
    return a * b

def delen(a, b):
    if b != 0:
        return a / b
    else:
        return "Fout: delen door nul kan niet."

def main():
    print("Welkom bij rekenmachine!")
    print("Kies een bewerking:")
    print("1. Optellen")
    print("2. Aftrekken")
    print("3. Vermenigvuldigen")
    print("4. Delen")

    keuze = input("Voer een nummer in (1/2/3/4): ")

    if keuze in ('1', '2', '3', '4'):
        try:
            getal1 = float(input("Voer het eerste getal in: "))
            getal2 = float(input("Voer het tweede getal in: "))
        except ValueError:
            print("Ongeldige invoer! Gebruik alleen getallen.")
            return

        if keuze == '1':
            print("Resultaat:", optellen(getal1, getal2))
        elif keuze == '2':
            print("Resultaat:", aftrekken(getal1, getal2))
        elif keuze == '3':
            print("Resultaat:", vermenigvuldigen(getal1, getal2))
        elif keuze == '4':
            print("Resultaat:", delen(getal1, getal2))
    else:
        print("Ongeldige keuze.")

if __name__ == "__main__":
    main()
