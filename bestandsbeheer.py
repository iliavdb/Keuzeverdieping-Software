with open("voorbeeld.txt", "w") as f:
    f.write("Dit is een voorbeeldbestand.")

with open("voorbeeld.txt", "r") as f:
    inhoud = f.read()
    print(inhoud)
