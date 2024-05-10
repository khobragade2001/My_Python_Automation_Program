# String="Credence"
# print("$".join(String))
# print(",".join(String))
# s = 'credence for credence'
# print(s.title())

# list1 = [12, 15, 14, 22, 16,24,  18, 20]
# print(list1*2)

# my_list = [1, 2, 3, 4, 5]
# print(my_list[2:4])

# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4:2])

# list1=[1,2,3,4,5,6,7,8,9]
# for i in list1:
#     print(i)

# list = ['cat', 0, 6.7]
# copy_list = list.copy()
# copy_list_02 = list[ : ]
# print(copy_list)
# print(copy_list_02)

# odd_numbers = [1, 3, 5]
# numbers = [1, 4]
# odd_numbers.extend(numbers)
# print(odd_numbers)
# odd_numbers.append(numbers)
# print(odd_numbers)

# prime_numbers = [2, 3, 9, 5, 7, 9, 11]
# prime_numbers.remove(9)
# print(prime_numbers)

# T = ('red', 'green', 'blue')
# # T[0] = 'black'
# print(T[0])
# print(T[2])
# T = ('red', 'green', 'blue')
# del T
# print(T)

# a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
# print(a.count(1))
# print(a.index(5))
# abc=("Yusuf","Amit","Pooja","raj","Pritesh","Priya","Yusuf")
# # print(abc.count("Yusuf"))
# # print(abc.index("Yusuf"))
# # print(abc.index("Yusuf",1,7))
# # print(abc.index("Yusuf",-7,-1))
# print(abc.index("Yusuf",-1,-7))

# a_list = [1,2,3,4,5]
# print(a_list)
# print(type(a_list))  # list
# b_tuple = tuple(a_list)
# print(b_tuple)
# print(type(b_tuple)) #tuple
#
# print(a_list)
# print(type(a_list))
#
# a_list = tuple(a_list)
# print(a_list)
# print(type(a_list))
# empty_set = set()
# empty_dictionary = {}
# print(type(empty_set))
# print(type(empty_dictionary))

# demo_set = {6,4,3,1,6,8,5}
# demo_set.clear()
# print(demo_set)
# A = {2, 3, 5}
# B = {1, 2, 6}
# # perform difference operation using &
# print(A ^ B)
# print(A & B)

# x = {'a','b','c'}
# y = {'a','b','c'}
# print('Set x: ', x)
# print('Set y: ', y)
# print('Set x == y: ', x==y)
# print('Set x != y: ', x != y)

x = {1,2}
y = {1,2,3,4}
print('Set x: ', x)
print('Set y: ', y)
print('Set x <= y: ', x <= y)
print('Set x < y: ', x < y)
