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

class Professeur:

    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner (self):
        print("Le cours va commencer")

Romi = Personne ()
Robin = Eleve ()

Romi.afficherAge()
Robin.afficherAge()