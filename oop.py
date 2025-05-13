class Persoon:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def begroet(self):
        print(f"Hoi, ik ben {self.naam} en ik ben {self.leeftijd} jaar oud.")

persoon1 = Persoon("Alice", 30)
persoon1.begroet()
