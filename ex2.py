# Defined a function that takes a sequence of numbers as its only parameter
def Largest(user_sequence):
    # I did it the easy way using the sort function to sort the sequence in ascending order
    largest = user_sequence.sort()
    # I then assign the last number on the list to a variable and return it
    last = user_sequence[-1]
    return last

# I initialize an empty list, this will laster on hold the sequence from the user
sequence = []

# I use initialize a list with five entries, these entries are used while asking the user for input
list = ["first", "second", "third", "fourth", "fifth"]
# I use a for loop to iterate through the items in the list, this allows me to assign the item x to a variable
# This number of iterations also ensure that I get a limited sequence of numbers.
for x in list:
    number = x
    # I take a user input as a float and then turn it into an integer
    user_input = float(input(f"Please enter your {number} number: "))
    user_input = int(user_input)
    # I append each user input to the empty list from before
    sequence.append(user_input)

# I call the function and store its output in a variable and then print it out
largest = Largest(sequence)    
print(f"The largest number is {largest}")

        