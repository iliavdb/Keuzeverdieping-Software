def rekenmachine(a, b, operatie):
    if operatie == "optellen":
        return a + b
    elif operatie == "aftrekken":
        return a - b
    elif operatie == "vermenigvuldigen":
        return a * b
    elif operatie == "delen":
        if b != 0:
            return a / b
        else:
            return "Fout: Delen door nul"
    else:
        return "Onbekende operatie"

print(rekenmachine(10, 5, "optellen"))
