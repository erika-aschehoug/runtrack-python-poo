# Instancier un objet Voiture, passer les informations dont la classe a besoin et faites
# appel à la méthode informationsVehicule.

# Créer une classe Moto qui hérite de la classe Vehicule et ajouter l'attribut roue qui
# contient par défaut l’entier 2. Créer à nouveau une méthode informationsVehicule dans
# la classe Moto qui affiche l'intégralité des informations de la moto.

# Instancier un objet Moto et faites appel à la méthode informationsVehicule.

# Créer la méthode demarrer dans la classe Véhicule qui écrit en console “Attention, je
# roule”. Surcharger la méthode demarrer dans la classe Moto et Voiture afin d’afficher un
# message personnalisé. Faites démarrer votre voiture et votre moto.

class Vehicule:

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque du vehicule : {self.marque}")
        print(f"Modele du vehicule : {self.modele}")
        print(f"Annee du vehicule : {self.annee}")
        print(f"Prix du vehicule : {self.prix}")

class Voiture (Vehicule):
    def __init__(self, portes = 4):
        Vehicule.__init__(self)
        self.portes=portes

    def informationsVehicule(self):
        print(f"Nombre de portes : {self.portes}")
        return super().informationsVehicule()
    
audi = Voiture 
        
