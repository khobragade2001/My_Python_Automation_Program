class Instance_method ():
    def demo_method(self):
        print("this is instance method")

    @staticmethod
    def demo_static_method(str):           ### self not required
        print("this is static method  : ",str)

class_object = Instance_method()
class_object.demo_method()
class_object.demo_static_method("Ashish")


