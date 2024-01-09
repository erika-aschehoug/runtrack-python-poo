menu = [
    {
    "nom": "Pizza",
    "Prix HT": 10,
    "Statut": ""
    },
        {
    "nom": "Burger",
    "Prix HT": 9,
    "Statut": ""
    },
        {
    "nom": "Boeuf",
    "Prix HT": 18,
    "Statut": ""
    }
]

class Commande():
    def __init__(self,nb_cmd, liste_plat, statut):
        self.__nb_cmd = nb_cmd
        self.__liste_plat = liste_plat
        self.__statut = statut
        self.total = 0

    def ajout_plat(self, new_plat):
        self.__liste_plat.append(new_plat)

    def annule(self):
        self.__statut = "Annuler"
    
    def __calcul_commande(self):
        i = 0
        for i in range(2):
            if menu[i]["nom"] in self.__liste_plat:
                nombre = self.__liste_plat.count(menu[i]["nom"])
                self.total += (self.calcul_TVA(i) * nombre)
        
        print(self.total)

    def calcul_TVA(self,plat):
        total = menu[plat]["Prix HT"] * 1.2
        return total

    def affiche_cmd(self):
        print(self.__liste_plat)
        self.__calcul_commande()


commande1 = Commande(1, ("Burger","Pizza","Pizza"), "En cours")

commande1.affiche_cmd()

plat4 =  {
    "nom": "Boeuf",
    "Prix HT": 18,
    "Statut": ""
    }

menu.append(plat4)

print(menu)