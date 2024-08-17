import re

# split method
text = "Hello! my name is Ashish , I am from Yavatmal? Maharashtra, India - 445001."
pattern = r'[ ,!?.-]+'
split_text = re.split(pattern, text)
print(split_text)       ## ['Hello', 'my', 'name', 'is', 'Ashish', 'I', 'am', 'from', 'Yavatmal', 'Maharashtra', 'India', '445001', '']

# sub method
text = "Hello! my name is Ashish, I am from Yavatmal? Maharashtra, India - 445001."
pattern = r'[,!?.-]'
replace = ''
clean_text = re.sub(pattern, replace, text)
print(clean_text)

# subn method
text = "Hello! my name is Ashish, I am from Yavatmal? Maharashtra, India - 445001."
pattern = r'[,.!?-]'
replace = '_'
subn_text = re.subn(pattern, replace, text)
print(subn_text)        ## ('Hello_ my name is Ashish_ I am from Yavatmal_ Maharashtra_ India _ 445001_', 6)

## match object
para = "decorator is a special kind of function which is used to add extra functionality to existing function without change in it is called decorator"
pattern = r'decorator'
match_method = re.match(pattern, para)
print(match_method)     ##<re.Match object; span=(0, 9), match='decorator'>
if match_method:
    print("match found :",match_method.group())     ## match found : decorator
else:
    print("No Match found....")

# span method in match object
para = "Hello my name is ankush, Hi"
pattern = r'Hello'
match_method = re.match(pattern, para)
print(match_method)     ##<re.Match object; span=(0, 5), match='Hello'>
if match_method:
    print("match found :",match_method.span())     ## match found : (0, 5)
else:
    print("No Match found....")