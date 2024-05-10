from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def show(self):
        pass

class square(shape):
    def show(self):
        print("square has 4 side ....")

class circle(shape):
    def show(self):
        print("circle has round shape ....")

c= circle()
c.show()
s= square()
s.show()