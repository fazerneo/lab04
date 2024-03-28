# I define a function that takes a single parameter, which will be from the user input
def next_letter(char):
    # I check if the input is an english alphabet
    if char.isalpha() == True:
        # I use the ord function to find the integer value of the input character's unicode and store in a var
        process_1 = ord(char)
        # I increase the var value by 1
        process_1 += 1
        # I then turn this new increased value into it's string value from unicode
        process_2 = chr(process_1)
        return process_2
    # If the character is not an english alphabet then we return the character as it is
    else:
        return char

# We take a user input and then call the function inside a print function to display the output
user_input = input("Please enter an english alphabet: ")
print(next_letter(user_input))