######################## METHOD OVERRIDING ######################
class A:   ### parent class
    def demo(self):
        print("this is parent class of A")

class B(A):   #### child class
    def demo(self):
        super().demo()         ### call by parent class method
        print("this is child class of B")

bobj = B()
bobj.demo()