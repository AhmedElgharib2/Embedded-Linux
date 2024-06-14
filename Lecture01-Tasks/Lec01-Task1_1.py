# First Task in task 1
# Write a Python program to count the number 4 in a given list.

# Function to count any number in any list
def countNumber(lst, number):
    count = 0
    for num in lst:
        if int(num) == int(number):
            count += 1
    return count

# Taking the user input
lst = input("Enter your list separated with a ',': ")
lst = lst.split(',')
num = input("Enter number to count: ")

# Print the number of occurrences
print("Number of %d in the list = %d" %(int(num), countNumber(lst, num)))
