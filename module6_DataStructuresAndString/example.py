# Create the dictionary
favourite_language = {
    'deepak': 'python',
    'vinay': 'java',
    'rai': 'c',
    'sahu': 'c++',
    'abhi': 'hindi'
}

# Ask for user input (can be one or multiple names, comma separated)
input_names = input("Enter your name(s) separated by commas: ")
friends = [name.strip().lower() for name in input_names.split(',')]

# Loop through the dictionary
for name in favourite_language.keys():
    print(name.title())

    if name in friends:
        language = favourite_language[name].title()
        print(f"Hi {name.title()}, I see your favourite language is {language}.")
