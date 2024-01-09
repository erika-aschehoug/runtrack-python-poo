class Livre():
    def __init__(self, titre, auteur, pages) -> None:
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def get(self):
        return self.__titre, self.__auteur, self.__pages
    
    def set(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        if pages > 0:
            self.__pages = pages
        else:
            print("Un nombre de pages négatif est impossible")
        
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Ce livre n'est pas disponible")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else:
            print("Vous avez emprunter le livre")

livre1 = Livre("harry_potter", "JK", 430)

print(livre1.verification())
livre1.emprunter()
print(livre1.verification())
livre1.rendre()
print(livre1.verification())