#How to Create a Tuple
'''
# Using parentheses
my_tuple = (1, 2, 3)

# Without parentheses (still valid)
another_tuple = (4, 5, 6)

# Single element tuple (must include a comma)
single_element = (10,)

# Concatenating all tuples
print(my_tuple + another_tuple + single_element)

'''


#Accessing Tuple Elements
'''
my_tuple = (1, 2, 3)
print(my_tuple[0])   # Output: 1
print(my_tuple[-1])  # Output: 3 (last element)
'''


#Tuple Operations
'''
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2  # (1, 2, 3, 4)

# Repetition
repeat = tuple1 * 2  # (1, 2, 1, 2)
print(repeat)
# Length
print(len(tuple1))  # 2 beacause touple length start from 1 to ..............
'''


# Iterating a Tuple
'''
my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)
'''


#Tuple Methods
'''
sample = (1, 2, 3, 2, 4)

print(sample.count(2))  # 2 (number of times 2 appears)
print(sample.index(3))  # 2 (position of value 3)
'''


# tuple sort
my_tup = (5651,548,51,48,855,489,648,6589,65,89,6531,65859,1186)
sorted_list = sorted(my_tup)  # returns a list, not a tuple
print(sorted_list)