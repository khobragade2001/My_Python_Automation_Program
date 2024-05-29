#============================= shallow copy =======================
## a shollow copy is a copy of an object that store the reference of the original elements.
## the changes made in one object do affect the other OBJECT.

lst01 = [1,2,3,4]
lst02 = lst01
lst02[1]=200
print(lst01) ###=> [1, 200, 3, 4]
print(lst02) ###=> [1, 200, 3, 4]

import copy

lst01 = [[1,2,3,4],[5,6,7]]
lst02 = copy.copy(lst01)
lst02[1][1] = 600
print(lst01)## => [[1, 2, 3, 4], [5, 600, 7]]
print(lst02) ## => [[1, 2, 3, 4], [5, 600, 7]]


# ============================= Deep copy =========================
## deep copy is a process where we create a new object and copy elements recursively.
## the changes made in one object do NOT affect the other OBJECT.

lst03 = [4,5,6,7]
lst04 = lst03.copy()
lst04[1] = 500
print(lst03) ## => [4, 5, 6, 7]
print(lst04) ## => [4, 500, 6, 7]

import copy

lst01 = [[1,2,3,4],[5,6,7]]
lst02 = copy.deepcopy(lst01)
lst02[1][1] = 600
print(lst01)## => [[1, 2, 3, 4], [5, 6, 7]]
print(lst02) ## => [[1, 2, 3, 4], [5, 600, 7]]

