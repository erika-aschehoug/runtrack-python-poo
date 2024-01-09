class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(self.x, self.y)

    def afficherX(self):
        print(self.x)
    
    def afficherY(self):
        print(self.y)

    def changerX(self,new_x):
        self.x = new_x
    
    def changerY(self,new_y):
        self.y = new_y


coord = Point(10, 15)

coord.afficherLesPoints()
coord.changerX(8)
coord.afficherX()
coord.changerY(11)
coord.afficherY()
coord.afficherLesPoints()