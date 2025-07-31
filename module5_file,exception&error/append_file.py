file1 = open('append_file.txt','w')   # w for write
#statement()
writing_file = file1.write("Hello World!")
print(writing_file)
file1.close()

file1 = open('append_file.txt','r') # r for read
reading_file = file1.read()
print(reading_file)
file1.close()

file1 = open('append_file.txt','a')   # append means give the total no. of character in the file.
#statement()
writing_file = file1.write("Welcome to the programming world.")
print(writing_file)
file1.close()

file1 = open('append_file.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()