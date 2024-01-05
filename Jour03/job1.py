#je définis la classe ville

class Ville :

#constructeur de la classe ville avec en attribut nom et nb habitants
    
    def __init__(self,nom,nb_habitants):
        self.__nom = nom
        self.__nb_habitants=nb_habitants

#méthode pour ajouter des habitants à la ville 
        
    def ajout_nouvel_habitant(self, nombre):
        self.__nb_habitants += nombre
        return self.__nb_habitants
    
#méthode pour avoir le nombre d'habitants de la ville
    
    def get_nb_habitants(self):
        return self.__nb_habitants

#classe personne
    
class Personne :

#constructeur de la classe personne avec les attributs nom age ville
    
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

#méthode pour ajouter un nouvel habitants a la population de la ville

    def ajouterPopulation(self):
        self.__ville.ajout_nouvel_habitant(1)

#création des objets 
Paris = Ville("Paris",1000000)
Marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Paris : {Paris.get_nb_habitants()}")
print(f"Population de la ville de Marseille : {Marseille.get_nb_habitants()}")

#création de nouvelles instances et ajout a la population

personne_00 = Personne("John", 45, Paris)
personne_01 = Personne("Myrtille", 4, Paris)
personne_02 = Personne("Chloé", 18, Marseille)

print(f"Nouvelle population de la ville de Paris : {Paris.get_nb_habitants()}")
print(f"Nouvelle population de la ville de Marseille : {Marseille.get_nb_habitants()}")