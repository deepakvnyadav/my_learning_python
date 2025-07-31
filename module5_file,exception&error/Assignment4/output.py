user_input = input("Enter some data to write to file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Append additional data
additional_input = input("Enter more data to append to file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

#Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
