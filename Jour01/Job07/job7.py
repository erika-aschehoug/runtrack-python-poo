class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1
    
    def position(self):
        print(self.x, self.y)
  
personnage = Personnage(10, 2)
personnage.position()

personnage.gauche()
personnage.position()

personnage.droite()
personnage.position()

personnage.haut()
personnage.position()

personnage.bas()
personnage.position()