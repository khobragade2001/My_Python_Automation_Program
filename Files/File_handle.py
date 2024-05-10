## create file by using x parameter
a = open("ashish.txt","x")
a.write("this file is created by using X parameters \nthank you")

## read file by using r parameteres
f = open("demo.txt","r")
a = f.read()

## append file by using a paramateres
s = open("demo.txt","a")
print(s.write("\nwe can write using write method"))


### try block using file handle
try:
    q = open("demos.txt","r")
except:
    print("File not found")
else :
    print(q.read())


#### WITH STATEMENTS
# ## w : write , a : append , r : read
with open("demo.txt","w") as x:
    con = x.write("writing using with method")
    x.close()

with open("demo.txt","a") as z:
    sed = z.write("writing using with method")
    z.close()