try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError:
    print("This is an error")
finally:
    print("Continue with the following error")