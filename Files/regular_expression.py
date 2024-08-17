import re

# ## to find name from string
st = "Ashish age is 30 , Rahul age is 31, Meena age is 35"
pattern = r'[A-Z][a-z]*'
name = re.findall(pattern, st)
print("Name is :", name)        ## Name is : ['Ashish', 'Rahul', 'Meena']

## to find number from string
patte = r'\d{2}'
number = re.findall(patte, st)
print("Age is :", number)       ## Age is : ['30', '31', '35']

## to combine data using dict
combine = dict(zip(name, number))
print(combine)          ## {'Ashish': '30', 'Rahul': '31', 'Meena': '35'}
#
# ## to combine data using for loop
dictionary = {}
n = 0
for i in name:
    dictionary[i] = number[n]
    n += 1
print(dictionary)       ## {'Ashish': '30', 'Rahul': '31', 'Meena': '35'}


## search method return match object if there is match found then it return.
st = "raju is good boy and raju studying in yavatmal."
if re.search("raju", st):
    match = re.findall("raju", st)
    print("name is :", match)       ## name is : ['raju', 'raju']

## i want to disp those words starting with 'T'
st = "Sun Mon Tue Wen Thu Fri Sat"
pattern = r'\bT\w*'
out = re.findall(pattern, st)
print(out)      ## ['Tue', 'Thu']

## i want to replace sun to SUN
name = re.compile('[S]un')
output = name.sub('SUN', st)
print(output)           ## SUN Mon Tue Wen Thu Fri Sat

## how to remove new line from para

st = '''my name is ashish
how are you
?'''
var = re.compile('\n')
out = var.sub('  ', st)
print(out)          ## my name is ashish  how are you  ?

### to find number of alphabet in a digit
num = "123ASD654"
var = len(re.findall(r'\D', num))
print("number of alphabet is : ",var)       ## number of alphabet is :  3

### to find  alphabet from a  string
num = "123ASD654"
var = re.findall(r'\D', num)
print("alphabet is : ",var)             ## alphabet is :  ['A', 'S', 'D']

### to find number of digit in a number
num = "123ASD654"
var = len(re.findall(r'\d', num))
print("number of digit is : ", var)         ## number of digit is :  6

### to short only number from a string
num = "123ASD654"
var = re.findall(r'\d', num)
print("number is : ", var)          ## number is :  ['1', '2', '3', '6', '5', '4']



## show 5 to 7 digit number from pattern
pattern = "12 123 1234 12345 123456 1234567"
var = len(re.findall(r'\d{5,7}', pattern))
print("count of 5 to 7 digit number is :", var)     ## count of 5 to 7 digit number is : 3

## adhar number correct or not
adhar = input("Enter aadhar after 4 digit give -:")     ##Enter aadhar after 4 digit give -:3652-3652-63251
if re.search(r'^\d{4}-\d{4}-\d{4}$', adhar):
    print("your Aadhar number is correct : ", adhar)
else:
    print("your Aadhar number is Incorrect.......... ")     ## your Aadhar number is Incorrect..........

### varify full name
name = input("Enter full name : ")
pattern = r'^\w{2,15}\s\w{2,15}\s\w{2,25}$'
if re.search(pattern, name):
    print("your Enter valid name :", name)
else:
    print("Incorrect name Entered.......................... :")

### varify full name
name = input("Enter full name first latter Must be Capital Latter : ")
## Regex pattern to match three capitalized words separated by spaces
pattern = r'^[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}$'
if re.search(pattern, name):
    print("You entered a valid name:", name)
else:
    print("Incorrect name Entered....................")

## validate mobile number
num = input("Enter mobile number :")
pattern = r'^[987]\d{9}$'
if re.search(pattern, num):
    print("Valid Mobile Number :", num)
else:
    print("Invalid Mobile Number...........")

# [987] = must start either 9 or 8 or 7
# ^ show start from
# $ end
# When a string is prefixed with r, Python treats the backslashes (\)
# in the string as literal characters rather than as escape characters

## VALIDATE EMAIL ADDRESS
email = input("Enter your email address: ")
pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,6}$'

if re.search(pattern, email):
    print("Valid Email Address:", email)
else:
    print("Invalid Email Address.............")

