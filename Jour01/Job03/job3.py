class addition:

    def __init__(self, nombre1, nombre2):
        self.nombre1=nombre1 
        self.nombre2=nombre2
        self.resultat=self.nombre1+self.nombre2

addition_instance = addition (10, 40)   

print("Le résultat de l'opération est" , addition_instance.resultat)