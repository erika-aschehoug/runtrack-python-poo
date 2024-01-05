class CompteBancaire:

    def __init__(self,numero, nom, prenom, solde):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = nom
        self.__solde = solde

    def afficher(self):
        print(f"numero : {self.__numero}")
        print(f"nom : {self.__nom}")
        print(f"prenom : {self.__prenom}")
        print(f"solde : {self.__solde}")
    
    def afficherSolde(self):
        print(f"Votre solde est de : {self.__solde}")
        