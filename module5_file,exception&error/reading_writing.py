#---> write and read
file = open('reading_writing.txt','r+')
writing_file = file.write('Welcome to the python')
print(writing_file)
file.close()


file = open('reading_writing.txt','r+')
reading_file = file.read()
print(reading_file)
file.close()