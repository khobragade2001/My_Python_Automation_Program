###################### reverse string ####################
asd = "My name is Ashish"
reverse = "".join(reversed(asd))
print("Using join method:", reverse)

######################### using loop @@@@@@@@@@@@@@@
a = "My name is Ashish"
b = ""

for i in range(len(a)-1, -1, -1):
    b += a[i]


print("Original string:", a)
print("Reversed string:", b)

########################## using slicing @@@@@@@@@@@@@@@@@@@@@
a = "My name is Ashish"
print("Using slicing method",a[: : -1])
