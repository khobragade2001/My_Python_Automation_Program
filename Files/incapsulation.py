class A:
    _a = 10   ### protected
    __s = 50   ### private
    def demo(self):
        print("this is protected variable :", self._a)
        print("this is private variable :", self.__s)

a = A()
a.demo()

### outside the class
print("potected can be access outside the class ", a._a)
# print("but private can't be access outside the class ",a.__s) ### can't be access outside the class
#
class B(A):
    def demo2(self):
        print("this is class B access the protected variable:", self._a)
#
class C(A):
    def demo3(self):
        print("this is class C access the private variable:", self.__s)

b = B()
b.demo2() ## can be access

# c = C()
# c.demo3()### can't access
