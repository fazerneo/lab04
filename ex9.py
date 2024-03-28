# I define a function that takes the fahrenheit temperature as its input and uses the formula to convert to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# I use another function to check if the value is in range and if it is outside range then I return a string saying "outside_range"
def input_checker(fahrenheit):
    if fahrenheit < -60 or fahrenheit > 130:
        return "outside_range"

# I use a while loop to get user input and the loop breaks if user types end
# the user input is turned into a float and then into an integer as int function cannot run on a string
# we use the value checking function from above
# then we use another while loop that keeps asking for a valid value if the values entered are outside range
# Then we call the converter function inside a f'string to output the temperature in celsius
while True:
    fahrenheit = input("\nplease enter a the daily temperature in fahrenheit: ")
    if fahrenheit.lower() == "end":
        break
    fahrenheit = float(fahrenheit)
    fahrenheit = int(fahrenheit)
    input_checker(fahrenheit)
    while input_checker(fahrenheit) == "outside_range":
        fahrenheit = input("\nplease enter a valid daly temperature between -60 and 130: ")
        fahrenheit = float(fahrenheit)
        fahrenheit = int(fahrenheit)            
    print(f"the daily temperature in celsius is: {fahrenheit_to_celsius(fahrenheit)}")