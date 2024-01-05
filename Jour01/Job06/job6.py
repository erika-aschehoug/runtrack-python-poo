class Animal:

    def __init__(self):
        self.age=0
        self.prenom = ""

    def vieillir(self):
        self.age +=1

    def nommer(self,prenom):
        self.prenom= prenom 

animal = Animal()
print(animal.age)
animal.vieillir ()
print(animal.age)
animal.nommer ("Luna")
print("l'animal se nomme", animal.prenom)
