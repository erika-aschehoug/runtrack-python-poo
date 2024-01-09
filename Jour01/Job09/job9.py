class Produit():
    def __init__(self, name, prixHT, TVA):
        self.nom = name
        self.prixHT = prixHT
        self.TVA = TVA
        

    def CalculerPrixTTC(self):
        return (self.prixHT + self.prixHT * self.TVA)
    
    def afficher(self):
        print(self.nom, self.prixHT, self.TVA)

    def change_name_price(self,name,price):
        self.nom = name
        self.prixHT = price

switch = Produit("switch", 300, 0.2)
switch.afficher()
print(switch.CalculerPrixTTC())

switch.change_name_price("Ordinateur", 1000)
switch.afficher()
print(switch.CalculerPrixTTC())
