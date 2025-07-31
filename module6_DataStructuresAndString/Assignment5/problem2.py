'''
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

'''

original_list = [1,2,3,4,5,6,7,8,9,10]
print("orginal list : ", original_list)
print("Extracted first five element is : ",original_list[0:5])
reversed = original_list[0:5][::-1]
print("Reversed first five elements:", reversed)