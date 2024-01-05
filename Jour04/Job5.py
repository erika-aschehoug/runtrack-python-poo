# Récupérer votre classe Forme crée juste au-dessus.
# Créer une classe fille nommée Cercle qui hérite de la classe Forme et possédant un
# attribut radius.

# Surcharger la méthode aire dans la classe Cercle pour qu'elle renvoie l’aire du cercle.

# Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour tester les
# différentes surcharges de la méthode aire en affichant les résultats en console.

class Forme:

    def __init__(self):
        pass
        
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius=radius
