class Animal():
    def __init__(self, atribut, edat):
        self.atribut = atribut
        self.edat = edat
    def xerrar(self):
        pass
    def mourem(self):
        pass
    def quisoc(self):
        print("Soc un Cavall")

class Cavall(Animal):
    def xerrar(self):
        print("Iíííííííií")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un Dofi")

class Dofi(Animal):
    def xerrar(self):
        print("IchIchIchIch")
    def mourem(self):
        print("Nedant")
    def quisoc(self):
        print("Soc un animal")

class Abella(Animal):
    def xerrar(self):
        print("Sssssssssss")
    def mourem(self):
        print("Em moc volant")
    def quisoc(self):
        print("Soc una abella")
    def picar(self):
        print("si me emprenyes et picare")

class Huma(Animal):
    def __init__(self, atribut, edat, pares):
        self.atribut = atribut
        self.edat = edat
        self.pares = pares
    def xerrar(self):
        print("Xerram amb diferents idiomes")
    def mourem(self):
        print("Ens movem caminant")
    def quisoc(self):
        print("Soc una persona")
    def nom(self):
        print("Els humans tenim un nom")
    def pares(self):
        print("Els humans tenim pares")

class Centaure(Huma, Cavall):
    def xerrar(self):
        print("Xerram amb diferents idiomes")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un centaure")

class fiet(Huma):
    def __init__(self, atribut, edat, pares):
        self.atribut = atribut
        self.edat = edat
        self.pares = pares
    def xerrar(self):
        print("Ueeeeeeueeeueueueueeee")
    def mourem(self):
        print("Em moc gatejant")
    def quisoc(self):
        print("Soc un fiet")
    def nom_pares():
        for e in self.pares:
            print(e.nom)
class xou():
    def xerrar(self):
        print("Xou")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un centaure")
    
#Si

a = [Cavall("Marró", "4"), Dofi("Gris", "10"), Abella("Negre i groga", "0,5"), Huma("Monica", "Cristia", "7"), Centaure("Jordi", "Negre", "16"), fiet("Sergi", "A", "3")]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()