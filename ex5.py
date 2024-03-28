# I make a function that takes a string as the parameter. This string is obtained from the user
# I initialize an empty variable to hold integers
# I use a for loop to iterate through the characters in the string
# I use the isdigit function to check if the characters are digits
# If the characters are digits, I increment the value of the empty variable from before by 1
# I return the total number of digits using the variable from before
def count_digits(string):
    total_digits =int()
    for x in string:
        if x.isdigit() == True:
            total_digits += 1
    return total_digits
            
# I use a while loop and continuously take user inputs and call the function and output the number of strings
# I break the loop if the user inputs stop
while True:
    user_input = input("\nPlease enter any string with n number of digits, such as \"we 3 are good\".\nType stop and enter to quit: ")
    if user_input.lower() == "stop":
        break
    else:
        print(f"\nthe total digits in the user generated sting are: {count_digits(user_input)}")    