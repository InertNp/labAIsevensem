# Activity-1: Display Maximum Value Among Two Numbers
def maximum(x, y):
    if x > y:
        return x
    else:
        return y

# Activity-2: Display Pass or Fail Based on Marks
def result(marks):
    if marks > 60:
        return "Pass"
    else:
        return "Fail"

# Activity-3: Check if a Number is Even or Odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Activity-4: Check if a Number is Greater Than 5
def check_greater_than_five(number):
    if number > 5:
        return "Greater than 5"
    else:
        return "Not greater than 5"

# Negation in Python (Examples)
print(not (2 == 4))  # True
print(not (3 == 3))  # False
print(not (4 == 4))  # False
print(not (2 == 5))  # True

# Activity-5: Count Up Using a Loop
def count_up(start):
    for i in range(start, 11):
        print(i)

# Activity-6: Print Numbers from 1 to N
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

# Activity-7: For Loop from 3 to N
def for_user_loop():
    n = int(input("Enter a number to end the loop [N]: "))
    for i in range(3, n + 1):
        print(i)

# Activity-8: Find Cube of Numbers from N to 7
def cube(n):
    for i in range(n, 6, -1):
        print(f"Cube of {i} is {i**3}")

# Activity-9: Find Sum of Integers from 1 to N
def sum_of_integers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Running the functions

# Test Activity-1
maximum_result = maximum(4, 8)
print("Maximum value is:", maximum_result)

# Test Activity-2
result_status = result(45)
print("Result:", result_status)

# Test Activity-3
number = 7
print(f"{number} is", check_even_odd(number))

# Test Activity-4
number = 10
print(f"{number} is", check_greater_than_five(number))

# Test Activity-5
count_up(5)

# Test Activity-6
n = int(input("Enter a number: "))
print_numbers(n)

# Test Activity-7
for_user_loop()

# Test Activity-8
cube(10)

# Test Activity-9
n = int(input("Enter a number: "))
print("Sum of integers from 1 to", n, "is:", sum_of_integers(n))
