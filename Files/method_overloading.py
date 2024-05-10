class A:
    def demo(self):
        print("Welcome")
    def demo(self, name=" "):
        print("Welcome :",name)

    def demo(self, name=" ", last_name=" "):
        print("Welcome:", name, last_name)

obj = A()
obj.demo("ashish","nitin")



