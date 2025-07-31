#type of collection
#unordered
#unique element

set = {1, 2, 3, 4,5, 6, 7, 8}
set1 = {1, 2, 4, 6, 8}
set.add(9)
set.remove(5)
print(set & set1) # print intersection.
print(set1.union(set)) # print unin of all set.
print(set1.issubset(set)) # true or false.
print(set)
print(type(set))