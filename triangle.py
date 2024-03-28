# I define a function which takes one integer parameter
# we then use a for loop that iterates through i in a range from 1 and ends at num + 1 as we want the range to be inclusive of num
# We then initialize j as zero
# we use a while loop which iterates as long as j is less than i
# we print num and use end = "" so that in that iteration, a new line is not created
# we increment and use a blank print function outside to move to the next line
# we return the output
def triangle_maker(num):
    for i in range(1, num + 1):
        j = 0
        while j < i:
            print(num, end = "")
            j += 1
        print() 
    return