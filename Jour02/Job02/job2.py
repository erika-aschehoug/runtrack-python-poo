class Livre:

    def __init__(self,titre,auteur,page):
        self.__titre = titre
        self.__auteur = auteur
        self.__page = page

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_page(self):
        return self.__nbpage
    
    def set_titre(self,titre):
        self.__titre= titre
    def set_auteur(self,auteur):
        self.__auteur= auteur
    def set_page(self, page):
        if type (page) == int and page >= 0:
            self.__nbpage= page
        else:
            print("erreur")

livre = Livre ("le meilleur des mondes", "Aldous Huxley",399)


