####@@@@@@@@@@@@@@@@@ using join method @@@@@@@@@@@@@
number = str(input("Enter a number :"))
rev_number = "".join(reversed(number))
if number==rev_number:
    print(number,"is palindrome number")
else:
    print("No, this is not palindrome number")


#### @@@@@@@@@@@@@@@@@@@  using loop @@@@@@@@@@@@@@
number = int(input("Enter a number: "))
a = number
s = 0
while a > 0:
    r = a % 10
    s = (s * 10) + r
    a = a // 10

rev = s
if rev == number:
    print( number, "is a palindrome number by sing loop")
else:
    print(number, "is not palindrome number by sing loop")

