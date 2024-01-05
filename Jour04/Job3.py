# Créer une classe Rectangle avec comme attribut privé longueur et largeur. Créer la
# méthode perimètre permettant de calculer le périmètre du rectangle ainsi que la
# méthode surface permettant de calculer la surface du rectangle.

# Créer les assesseurs et mutateurs permettant de manipuler les attributs de la classe.

# Créer une classe Parallelepipede héritant de la classe Rectangle avec en plus un
# attribut hauteur et une autre méthode volume, permettant de calculer le volume du
# parallélépipède.

# Instancier la classe Rectangle et assurez-vous que toutes les méthodes fonctionnent.

class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre (self):
        return (2 * self.__longueur) + (2 * self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self,longueur,largeur)
        self.hauteur = hauteur

    def volume(self):
        return (super().surface() * self.hauteur)
    
parall = Parallelepipede(10, 5, 3)

print(parall.volume())



