'''
x=[]
for i in range(10):
    z = i**2
    x.append(z)
print(x)

'''
#syntax :
# [expression foe the item in the list { if (test expression) }]
x = [i**2 for i in range(11) if i**2%2==0]
print(x)

