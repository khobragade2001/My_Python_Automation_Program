# ################ @@@@@@@  lambda function   @@@@@@@@@@@@ #############
# A function which has no name, is known as lambda function.
# This is also known as anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# @@@@@ Syntax@@@@@
# lambda arguments : expression

add = lambda a, b: a+b
ad = add(5,20)
print(ad)

percentage = lambda obtain_marks, Total_marks : (obtain_marks/Total_marks)*100
print(percentage(650,750))
