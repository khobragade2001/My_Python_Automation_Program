import re

# ## to find name from string
# st = "Ashish age is 30 , Rahul age is 31, Meena age is 35"
# name = re.findall(r'[A-Z][a-z]*', st)
# print("Name is :", name)
#
# ## to find number from string
# number = re.findall(r'\d{2}', st)
# print("Age is :", number)
#
# ## to combine data using dict
# combine = dict(zip(name, number))
# print(combine)
#
# ## to combine data using for loop
# dictionary = {}
# x = 0
# for i in name:
#     dictionary[i] = number[x]
#     x += 1
# print(dictionary)
#
#
# ## search method return match object if there ismatch found then it return.
# st = "raju is good boy and raju studing in yavatmal."
# if re.search("raju", st):
#     match = re.findall("raju", st)
#     print("name is :", match)
#
# ## to find perticular pattern
# st = "Sun Mon Tue Wen Thu Fri Sat"
# #i want to disp words starting with 'T'
# out = re.findall('[T]*', st)
# print(out)      ## ['', '', '', '', '', '', '', '', 'T', '', '', '', '', '', '', '', 'T', '', '', '', '', '', '', '', '', '', '', '']
#
# ## i want to replace sun to SUN
# name = re.compile('[S]un')
# output = name.sub('SUN', st)
# print(output)
#
# ## how to remove new line from para
#
# st = '''my name is ashish
# how are you
# ?'''
# var = re.compile('\n')
# out = var.sub('  ', st)
# print(out)
#
# ### to find number of alphabet in a digit
# num = "123ASD654"
# var = len(re.findall('\D', num))
# print("number of alphabet is : ",var)
#
# ### to find number of digit in a number
# num = "123ASD654"
# var = len(re.findall('\d', num))
# print("number of digit is : ", var)

## find alphabet in number
## find digit in number
#
# ## show 5 to 7 digit number from pattern
# pattern = "12 123 1234 12345 123456 1234567"
# var = len(re.findall('\d{5,7}', pattern))
# print("count of 5 to 7 digit number is :", var)
#
# ## adhar number correct or not
# adhar = input("Enter aadhar after 4 digit give -:")
# if re.search('\d{4}-\d{4}-\d{4}', adhar):
#     print("your Aadhar number is correct : ", adhar)
# else:
#     print("your Aadhar number is Incorrect : ", adhar)

## varify full name
# name = input("Enter full name : ")
# if re.search(r'^\w{2,20}\s\w{2,20}\s\w{2,20}$', name):
#     print("your Enter valid name :", name)
# else:
#     print("Incorrect name Entered :", name)
#
#
# name = input("Enter full name first latter Must be Capital Latter : ")
#
# ## Regex pattern to match three capitalized words separated by spaces
# pattern = r'^[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}$'
#
# if re.search(pattern, name):
#     print("You entered a valid name:", name)
# else:
#     print("Incorrect name entered:", name)

## validate mobile number
num = input("Enter mobile number :")
if re.search(r'^[987]\d{9}$', num):
    print("Valid Mobile Number :", num)
else:
    print("Invalid Mobile Number...........")

## [987] = must start either 9 or 8 or 7
## ^ show start from
## $ end
## When a string is prefixed with r, Python treats the backslashes (\)
# # in the string as literal characters rather than as escape characters