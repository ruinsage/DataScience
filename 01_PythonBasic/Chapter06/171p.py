class Flight :
    def fly(self):
        print("날다")

    def where(self):
        print("하늘을")

class Airplane(Flight) :
    def fly(self):
        print("비행기가 날다")
    def see(self):
        print("비행기에서 경치를 보다")
class Bird(Flight) :
    def fly(self):
        print("새가 날다")

    def sing(self):
        print("새가 울다")

class Paper(Flight) :

    def fly(self):
        print("종이비행기가 날다")

    def drop(self):
        print("종이비행기가 떨어진다")

flight = Flight()
air = Airplane()
bird = Bird()
paper = Paper()

flight.where()
flight.fly()
print()

#flight = air
#flight.where()
#flight.see()
#flight.fly()
air.where()
air.see()
air.fly()
print()

#flight = bird
#flight.where()
#flight.fly()
#flight.sing()
bird.where()
bird.fly()
bird.sing()
print()

#flight = paper
#flight.where()
#flight.fly()
#flight.drop()
paper.where()
paper.fly()
paper.drop()
