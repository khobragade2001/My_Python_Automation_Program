#@@@@@@@@@@@@@@   *argument @@@@@@@@@@@@
def demo(normal, *ashish):
    print(normal )
    for i in ashish:
        print(i)

a = ("ashish", "madhu","vidhyadevi","madhavi","suraj")
s = "this is normal statements"
demo (s,*a)
###-------------------------------------------------------- OR ---------------------------------------------------------------------------
def additon(*number):
    a = 0
    for i in number:
        a = a+i
    print(a)
## calling
additon(5,6,7)


## @@@@@@@@@@@@ **keywords arguments #############
def demo_2(normal, *madhu, **sanju): ## * madhu parameter convert into tuple
    print(normal)
    for i in madhu:
        print(i)
    for j, k in sanju.items():
        print(f"{j} is a {k} ")

a = "this is normal arguments from keyword arguments "
s = ("ashish","kanchan","rutuja","mahesh")
d = {"khobragade":"testor","dhanavij":"Testor","wase":"stenographer","thakre":"raymond worker"}

demo_2(a,*s,  **d)
###----------------------------------------------------------------- OR ----------------------------------------------------------
def demo(*number,**name):### ** name parameter convert into dictionary
    c= 0
    for i in number:
        c +=i
    print(c)
    for j, k, in name.items():
        print(f"{j} is a {k}")
        print(f'{k} is a job of {j}')

number = (5,35,70,2)
name ={"rahul":"pilot","madhu":"banker"}
name1 = {"ram":"DJ"}
demo(*number, **name1,**name)
