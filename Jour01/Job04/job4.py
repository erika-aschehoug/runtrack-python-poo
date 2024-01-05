class personne:
    def __init__ (self, prenom, nom):
        self.prenom=prenom
        self.nom=nom

    def SePresenter(self):
        return (f"Je suis {self.prenom}{self.nom}")
    
erika=personne ("erika", " aschehoug")
thomas=personne ("thomas", " Jojo")
print (erika.SePresenter())
print (thomas.SePresenter())
