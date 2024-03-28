# I firstly define a function with a string as it's formal parameter
# I then initialize an empty variable to hold the digits as strings
# Then I use a for loop to iterate through the characters in the string
# I use the isdigit function to check if a character is a digit
# If the character being iterated is a digit, then it is appended to the empty variable using +
# We finally return the initial variable, which is now full of the digits in sequence.
# I also researched about join method but was a bit confused about applying that here
def attach_digits(string):
    empty =""
    for x in string:
        if x.isdigit() == True:
            empty = empty + x
    return empty

# I use a while loop to continuously take user inputs and call the function inside a print function
# I break the loop if the user enters stop
while True:
    user_input = input("Please enter a string that contains some digits: ")
    if user_input.lower() == "stop":
        break
    print(attach_digits(user_input))
    