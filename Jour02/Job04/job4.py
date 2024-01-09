class Student():
    def __init__(self, nom, prenom, id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, nb_credits):
        if nb_credits > 0:
            self.__credits += nb_credits
            self.__level = self.__studentEval()

    def show_credits(self):
        print("Le nombre de credit de " + self.__prenom, self.__nom + " est de " + str(self.__credits))

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        if self.__credits >= 80:
            return "Très bien"
        if self.__credits >= 70:
            return "Bien"
        if self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def studentInfo(self):
        print("Nom = " + self.__nom)
        print("Prenom = " + self.__prenom)
        print("id = " + str(self.__id))
        print("Niveau = " + self.__level)




student1 = Student("Doe", "John", 145)
student1.add_credits(70)
student1.show_credits()
student1.studentInfo()