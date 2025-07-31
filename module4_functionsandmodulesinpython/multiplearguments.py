# function with multiple arguments
#arguments of funtion1
def add(a,b):
    return a+b
#argumensts of function2
def square(x):
    return x*x
#argumensts of function3
def multiply(y,z):
    return z*y
result = square(add(3,4))
print (result)
print(multiply(4,result))

