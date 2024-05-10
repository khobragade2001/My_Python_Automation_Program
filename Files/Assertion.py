#Assertion is used to check if a perticular condition is satisfied or not
#syntax : assert<condition>,<massage>
# if the condition is true , nothing happen
# if the condition is false , assertion error message will be display

num = int(input("Enter a positive number : "))
assert num >0, "you entered NEGATIVE values"
print("Enter number is  :", num)

##HANDLE ASSERTION ERROR
num = int(input("Enter a + ve number : "))
try:
    assert num >0, "you entered NEGATIVE values"
    print("Entered number is  :", num)
except :
    print("please enter positive number")