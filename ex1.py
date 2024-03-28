# I define a function that takes two formal parameters
# I then return the average of the two parameters
def average(a, b):
    return (a + b) / 2

# I take two user inputs and store them in their respective variables. I take them as floats
a = float(input("please enter your first number: "))
b = float(input("please enter your second number: "))

# I convert the initial inputs into integers
a = int(a)
b = int(b)

# I call the function and store the output into a variable and print the results
Average = average(a,b)
print(f"Average of {a} and {b} is {Average}")