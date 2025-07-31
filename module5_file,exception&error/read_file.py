
# 1:
file1 = open('file.txt','r')
#statement()
reading_file = file1.read() # read(): In Paranthesis to write the number of letter to print [Example : write 5 print only 5 letter in the .txt file. It strats fron counting 1 to 5. It can read fron 1 not 0]
#file1.readline() : It can be show a one line from the file.
#file1.readlines() : It can be show a total lines from the file.
print(reading_file)
file1.close()

'''

# 2:
with open ('file.txt', 'r') as file:
    read_file1= file.read()
print(read_file1)

'''