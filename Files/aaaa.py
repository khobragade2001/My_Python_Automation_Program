def demo_arg(normal, *arg):
    print(normal)
    for i in arg:
        print(i )
a = [20, "madhu", 51, "madhavi", 33, "sachine",555]
demo_arg("this is normal arguments",*a)
normal = "this is normal arguments"


def demo_kwarg(normal, *arg, **kwarg):
    print(normal)
    for i in arg:
        print(i)
    for key, values in kwarg.items():
        print(key," is a ",values)

ashish = "this is normal statements"
a = ["Ashish","Madhubala","Kanchan"]
k = {"Ashish" : "Tester" ,"Madhubala" : "banker","Kanchan":"Maneger"}
demo_kwarg(ashish,*a, **k)

