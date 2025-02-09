
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.

# Function to find the sum
def sum_numbers(number_list):
    total = sum(number_list)
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_numbers(numbers)
print("The sum of the numbers is: ", result)


# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.

numbers = [10, 9876, 534, 23, 234]
average = sum(numbers) / len(numbers)
print ("The average of the numbers is: ", average)




# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

numbers = [234, 3456, 657, 75, 67]
largest = max(numbers)
print("The largest number in the list it: ", largest)