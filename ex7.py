# I define a function with one formal parameter
# I initialize an empty variable to hold the shifted string
# I use a for loop to iterate through the characters in the string
# If the char is an empty space than it is added as it is to the shifted string
# elif the character is an alphabet or number then it uses the ord function to get the unicode integer value and increment it by 1
# after the incrementation, the new value is turned into it's corresponding unicode character
# The new character is appended to the shifted string
# If the char is not a space, alphabet or number, then the character is appended as it is
# we return the shifted string
def letter_shift(string):
    shifted_string = ""
    for char in string:
        if char == " ":
            shifted_string = shifted_string + char
        elif char.isalpha() == True or char.isnumeric() == True:
            process_1 = ord(char)
            process_1 += 1
            process_2 = chr(process_1)
            shifted_string = shifted_string + process_2
        else:
            shifted_string = shifted_string + char
    return shifted_string

# we use a while loop to continuously take user input and cal the function
# we state a break function to act if user types any case of stop
while True:
    user_input = input("please enter any string or enter \"stop\" to exit: ")
    if user_input.lower() == "stop":
        break
    print(letter_shift(user_input))