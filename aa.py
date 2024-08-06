### reverse of steing using slicing method
string = "my name is ashish"
rev = string[::-1]
print("Reverse of string using slicing :", rev)

### reverse of string using loop
string = "ashish yadavrao khobragade"
var = []
for i in reversed(string):
    var.append(i)
output = "".join(var)
print("reverse of string using loop :", output)

### reverse of word
string = "ashish yadavrao khobragade"
var = string.split()
rev = var[::-1]
output = " ".join(rev)
print("reverse of word using slicing :", output)

### revese of word using loop
string = "Ashish Yadavrao Khobragade"
var = string.split()
rev = []
for i in reversed(var):
    rev.append(i)
output = " ".join(rev)
print("revese of word using loop :", output)

### swap of variable without using third variable
a = 50
b = 20
a = a + b
b = a - b
a = a - b
print("value of a :", a)
print("value of b :", b)

### reverse of number using function
s = 0


def rev(n):
    global s
    if (n > 0):
        r = n % 10
        s = s * 10 + r
        n = n // 10
        rev(n)
    return (s)


n = int(input("Enter a number for revser :"))
var = rev(n)
print("Revese of number using function :", var)

### reverse of number using join method
num = input("enter a number for reverse:")
rev = "".join(reversed(num))
print("reverse of number using join method :", rev)

### fibbonacci series
a = 0
b = 1


def fibbo(n):
    global a, b
    if (n < 0):
        return
    else:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        fibbo(n - 1)


num = int(input("Enter a number for fibbonacci series :"))
fibbo(num)

### repetation of alphabet
string = "ashish yadavrao khobragade"
rev = {}
for i in string:
    if i in rev:
        rev[i] += 1
    else:
        rev[i] = 1
print("\nRepetation of character:", rev)

### printing of star pyramid
num = int(input("Entera number for pyramid :"))
for i in range(num):
    for j in range(0, i + 1):
        print("*", end="")
    print("")

### printing of reverse star pyramid
num = int(input("enter a number for reverse of pyramid :"))
for i in range(num, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print("")

### second max number
ls = [1, 2, 3, 4, 5, 6]
ind = ls.index(max(ls))
ls.pop(ind)
print("second max number is :", max(ls))

### sort even number from a list
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("even number is :", end="")
for i in lis:
    if (i % 2 == 0):
        print(i, end=" ")

### sort odd number from a list
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nodd number is :", end="")
for i in lis:
    if (i % 2 == 1):
        print(i, end=" ")

### removing duplicate latter from string
string = "ashish yadavrao khobragade"
var = []
for i in string:
    if i not in var:
        var.append(i)
output = "".join(var)
print("removing duplicate latter from string", output)

### how many alphabet in a string
st = "hello ashish how are you"
var = [i for i in st if i.isalpha()]
print("total number of alphabet is :", len(var))

### how many words in a string
st = "hello ashish how are you"
var = st.split()
print("total number of words is :", len(var))

### i want to display only symbol
para = "hello  #> hpw 21!@<.~%^ are &*() you _+';:`[ ashish ]/{}"
ls = list(para)
alnum = [i for i in ls if i.isalnum()]
result = set(ls) - set(alnum)
# result=set(ls).difference(set(alnum)) or below line also work
output = " ".join(result)
print("only symbol from given string is :", output)

### return only number from a list
ls = ["A", 2, 'S', 3, 'D', 5, 'F', 6, 'G', 7, 'H']
num = [i for i in ls if isinstance(i, (int, float))]
print("only number from string :", num)

### username and domain name
email = "khobragade2001@outlook.com"
user, domain = email.split("@")
print("user name is :", user)
print("domain name is :", domain)

### list of username and domain name
email = ["aykhobragade@outlook.com", "khobragade2001@gmail.com", "ashish999khobragade@hotmail.com"]


def email_sep(email):
    user, domain = email.split("@")
    return user, domain


for i in email:
    user, domain = email_sep(i)
    print("user name is :", user, end=" ")
    print("domain name is :", domain)

### in para each word give the number
ls = "ashish yadavrao khobragade from yavatmal "
st = ls.split()
sets = {}
count = 1
for i in st:
    sets[i] = count
    count += 1
print(sets)

### date function
from datetime import date

today_date = date.today()
indepence_date = date(2024, 8, 15)

if today_date == indepence_date:
    print("Flipkart indepence day offer is ON")

else:
    print("Normal flipkart sell")

### multi threading



