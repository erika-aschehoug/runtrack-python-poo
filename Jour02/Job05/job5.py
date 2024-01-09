class Voiture():
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 4

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("Je demarre")
        else:
            print("Pas assez d'essence pour démarrer")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir
    
voiture1 = Voiture("audi"," A1", 2020, 90000)
voiture1.demarrer()