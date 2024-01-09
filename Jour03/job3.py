class Tache():
    def __init__(self, titre, description, status):
        self.titre = titre
        self.description = description
        self.status = status

class ListeDeTaches():
    def __init__(self, taches) -> None:
        self.taches = taches

    def ajouterTache(self, newtache):
        self.taches.append(newtache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)
    
    def marquerCommeFinie(self , tache):
        if tache.status == "A faire":
            tache.status = "Terminer"
        else:
            print(f"Tache {tache.titre} déjà terminer")

    def afficherListe(self):
        print("Liste de taches:")
        for tache in self.taches:
            print(f"{tache.titre} - {tache.description} - {tache.status}")

    def filtrerListe(self, status):
        print(f"\nTache {status}")
        for tache in self.taches:
            if tache.status == status:
                print(f"[{tache.titre}]")

tache_0 = Tache("Courses", "Faire les courses", "A faire")
tache_1 = Tache("Loyer", "Payer le loyer", "A faire")
tache_2 = Tache("Facture", "Regler les factures", "A faire")

list_tache = ListeDeTaches([tache_0, tache_1])

list_tache.ajouterTache(tache_2)

list_tache.afficherListe()

list_tache.marquerCommeFinie(tache_2)

list_tache.supprimerTache(tache_2)

list_tache.afficherListe()
list_tache.filtrerListe("A faire")