import random
import names

## print float values
values = random.random()
print(values)


## to display perticular range values but unique
a = random.uniform(1, 50)
print(a)

## to display perticular range values
a = random.randint(1,5)
print(a)

## choice method
initial = ['Shree','Kumar','Shau','Reddy','Kumari','Patil','Haji','Doctor','Engineer']
a= random.choice(initial)
print(a +  '  Ashish')

### random phone number generations
a = random.randint(9100000000,9999999999)
print(a)

### random Email address generations
s = names.get_first_name(gender='mail')
f = names.get_full_name()
d = names.get_last_name()
print(s+'_'+d+'@gmail.com')

