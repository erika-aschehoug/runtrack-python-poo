class Joueur():
    def __init__(self,nom, numero, position, nb_buts, passes_D, cartons_J, cartons_R):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_buts, self.passes_D = nb_buts, passes_D
        self.cartons_J, self.cartons_R = cartons_J, cartons_R

    def marquer_but(self):
        self.nb_buts += 1
        return self.nb_buts

    def effectuer_passe_decisive(self):
        self.passes_D += 1
        return self.passes_D

    def recevoir_carton_jaune(self):
        self.cartons_J += 1
        return self.cartons_J

    def recevoir_carton_rouge(self):
        self.cartons_R += 1
        return self.cartons_R

    def afficher_stats(self):
        print(f"______________________________"
              f"\nNom: {self.nom}"
              f"\nNuméro: {self.numero}"
              f"\nPosition: {self.position}"
              f"\nNombre de buts: {self.nb_buts}"
              f"\nNombre de passes décisives: {self.passes_D}"
              f"\nNombre de carton jaune: {self.cartons_J}"
              f"\nNombre de carton rouge: {self.cartons_R}")
        
class Equipe:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    def ajouter_joueur(self, joueur):
        if joueur not in self.joueurs:
            self.joueurs.append(joueur)

    def afficher_stats_joueurs(self):
        for joueur in self.joueurs:
            joueur.afficher_stats()

    def mettre_a_jour_statistiques_joueurs(self):
        print("\nMise à jour des statistiques")
        self.afficher_stats_joueurs()
    

# Composition équipe numéro 1
joueur_0 = Joueur("Jean", 56, "Gardien", 0, 0, 0, 0)
joueur_1 = Joueur("Pierre", 3, "Libéro", 0, 0, 0, 0)
joueur_2 = Joueur("Alex", 12, "Attaquant", 0, 0, 0, 0)
joueur_3 = Joueur("Guillaume", 20, "Remplaçant", 0, 0, 0, 0)

# Composition équipe numéro 2
joueur_4 = Joueur("Remy", 41, "Gardien", 0, 0, 0, 0)
joueur_5 = Joueur("Pasacal", 51, "Libéro", 0, 0, 0, 0)
joueur_6 = Joueur("Paul", 1, "Attaquant", 0, 0, 0, 0)
joueur_7 = Joueur("Maxime", 2, "Remplaçant", 0, 0, 0, 0)

equipe_0 = Equipe("Equipe 0", [joueur_0, joueur_1, joueur_2])
equipe_1 = Equipe("Equipe 1", [joueur_4, joueur_5, joueur_6, joueur_7])

equipe_0.afficher_stats_joueurs()
equipe_0.ajouter_joueur(joueur_3)

joueur_3.effectuer_passe_decisive()
joueur_1.marquer_but()

joueur_4.recevoir_carton_jaune()
joueur_2.recevoir_carton_rouge()

equipe_0.mettre_a_jour_statistiques_joueurs()