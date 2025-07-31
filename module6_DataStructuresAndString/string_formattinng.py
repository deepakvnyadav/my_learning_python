name= 'Deepak'
number= len(name)*7 #this function can multiply with no. of letter.
print("Hello, {} is your lucky number is : {} ". format(name,number))


example = "format () method"
string = "This is the example of {} on a string.".format(example)
print(string)



first = "deepak"
second = "vinay"
third = "bipin"
string = "i am {} and my second name {} and my brother name {}".format(first,second,third)
print(string)


price = 100
price_with_tax = 100+18
print(f"total price_with_tax : Rs. : {price_with_tax}")
print("real price of icecream Rs.{:.2f} and with the tax price Rs.{:.2f}".format(price,price_with_tax))
# the meaning of 2f is number can store with two digit of float.
