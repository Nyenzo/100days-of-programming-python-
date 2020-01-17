class Things:
    pass
class Animate(Things):
    pass
class Inanimate(Things):
    pass
class sidewalk(Inanimate):
    pass
class Animals(Animate):
    def breath(self):
        print("Breathing")
    def move(self):
        print("Moving")    
    def eat(self):
        print('Eating')    
    pass
class Mammals(Animals):
    pass
class Giraffes(Mammals):
    def __init__(self,leftfootforward,leftfootback,rightfootforward,rightfootback):
        self.leftfootforward=leftfootforward
        self.leftfootback=leftfootback
        self.rightfootback=rightfootback
        self.rightfootforward=rightfootforward
    def dance(self):
        self.leftfootforward()
        print("Left foot forward")
        self.leftfootback()
        self.rightfootforward()
        self.rightfootback()
        self.leftfootback()
        self.rightfootback()
        self.rightfootforward()
        self.leftfootforward()
Barka = Giraffes("left foot forward","left foot backward","right foot forward","right foot backward")
