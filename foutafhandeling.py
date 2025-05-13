try:
    resultaat = 10 / 0
except ZeroDivisionError:
    print("Je kunt niet delen door nul!")
finally:
    print("Foutafhandeling afgerond.")
