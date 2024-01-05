# À l’aide de la classe Personne , Eleve et Professeur créent au-dessus, faites dire bonjour
# à votre élève grâce à la méthode bonjour ainsi que “Je vais en cours” grâce à la
# méthode allerEnCours. Redéfinir l'âge de l’élève à 15 ans.

# Créer un objet Professeur, 40 ans, faite dire bonjour à votre professeur et commencer le
# cours grâce à la méthode enseigner.

class Personne:

    def __init__(self,age=14):
        self.age = age

    def afficherAge(self):
        print (self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge (self,nouvelAge):
        self.age = nouvelAge
        return self.age

class Eleve(Personne):

    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print (f"j'ai {self.age} ans")

class Professeur(Personne):

    def __init__(self, matiereEnseignee,age=40):
        self.age = age
        self.matiereEnseignee = matiereEnseignee

    def enseigner (self):
        print("Le cours va commencer")


Robin = Eleve ()
MrLoops = Professeur ("Français")

Robin.bonjour()
Robin.allerEnCours()
Robin.modifierAge(15)
Robin.afficherAge

MrLoops.bonjour()
MrLoops.enseigner()
