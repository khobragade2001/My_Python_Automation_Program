from abc import ABC, abstractmethod


class car(ABC):
    def show(self):
        print("every car has 4 wheels")

    @abstractmethod
    def speed(self):
        pass


class Maruti(car):
    def speed(self):
        print("Maruti car speed limit is 120 km/hr")


class BMW(car):
    def speed(self):
        print("BMW car speed limit is 350 km/hr")


class Pagaani(car):
    def speed(self):
        print("Pagaani car speed limit is 450 km/hr")


obj = Maruti()
obj.show()
obj.speed()

bmobj = BMW()
bmobj.show()
bmobj.speed()

pobj = Pagaani()
pobj.show()
pobj.speed()

### we can't create abstract class object
# cobj = car()
# # cobj.speed()   ## Can't instantiate abstract class car without an implementation for abstract method 'speed'
# cobj.show()        ## TypeError: Can't instantiate abstract class car without an implementation for abstract method 'speed'