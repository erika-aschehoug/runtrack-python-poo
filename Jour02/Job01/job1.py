class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # (mutateur)
    def set(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # (assesseurs)
    def get(self): 
        return self.__longueur, self.__largeur


rectangle = Rectangle(10, 5)

print("Longueur et Largeur :", rectangle.get()) 

rectangle.set(20, 10)

print("Longueur et Largeur modifié :", rectangle.get()) 