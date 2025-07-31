'''
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

dict = {'Alice': 85, 'vinay' : 75, 'deepak' : 95}
name = input("Enter the student's name : ")
if name in dict :
    print(f"{name} marks : {dict[name]} ")
else :
    print ("Your name is not found")