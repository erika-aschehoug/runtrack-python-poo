import math   

class cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.calccirconf =0

    def changerrayon(self,nouveaurayon):
        self.rayon = nouveaurayon

    def circonference (self):
        return 2 * self.rayon* math.pi
    
    def aire (self):
        return math.pi * self.rayon **2
    
    def diametre (self):
        return self.rayon *2
    
    def afficherInfos(self):
        print(f"le rayon est de {self.rayon}, la circonférence est de {self.circonference()}, et l'aire est de {self.aire()}")


cercle1=cercle(4)
cercle1.afficherInfos()

cercle2=cercle(7)
cercle2.afficherInfos()
