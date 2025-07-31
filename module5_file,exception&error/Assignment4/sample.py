'''
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

'''

# Step 1: Open the file in 'r+' mode and write multiline content
file = open('sample.txt', 'r+')
file.write('''This is the sample of line. 
It contains multiple lines.''')  # '''...''' allows multiline text
file.close()

# Step 2: Open the file again to read line by line
file = open('sample.txt', 'r+')
reading_file1 = file.readlines()
print("Reading file line by line: ")
for line in reading_file1:
    print(line.strip())
file.close()
