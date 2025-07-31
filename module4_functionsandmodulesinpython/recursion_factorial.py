#1 = 1*0 = 1
#2 = 2*1 = 2
#3 = 3*2*1 = 6
#4 = 4*3*2*1 = 24
#5 = 5*4*3*2*1 = 120
#6 = 6*5*4*3*2*1 = 720
def factorial(n):
    if (n<2):
        return 1
    else :
        return n * factorial(n-1)
result = factorial(int(input("Enter the number : ")))
print(result)