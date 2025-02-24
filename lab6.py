# Activity 1: Factorial of a Number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Activity 2: Sum of Two Numbers Using Input/Output
def sum_two_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = x + y
    print("Sum is:", z)

# Activity 3: Sum of Three Numbers Using Input/Output
def sum_three_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    result = x + y + z
    print("Sum is:", result)

# Activity 4: Maximum of Two Numbers Using Input/Output
def maximum():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = max(x, y)
    print("The greatest number is:", z)

# Activity 5: Minimum of Two Numbers Using Input/Output
def minimum():
    x = int(input("Enter value of X: "))
    y = int(input("Enter value of Y: "))
    z = min(x, y)
    print("Minimum value is:", z)
    if x == y:
        print("Both numbers are equal")
    elif x > y:
        print("X is greater")
    else:
        print("Y is greater")

# Activity 6: Check if a Number is Even or Odd Using Input/Output
def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

# Activity 7: Power of a Number Using Input/Output
def power():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    result = base ** exponent
    print(base, "raised to the power of", exponent, "is:", result)

# Activity 8: Cube of a Number Using Input/Output
def cube():
    num = int(input("Enter a number: "))
    result = num ** 3
    print("Cube of", num, "is:", result)

# Activity 9: Multiplication Table Using Input/Output
def multiplication_table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Running the functions

# Test Activity 1
num = int(input("Enter a number for factorial: "))
result = factorial(num)
print("Factorial of", num, "is:", result)

# Test Activity 2
sum_two_numbers()

# Test Activity 3
sum_three_numbers()

# Test Activity 4
maximum()

# Test Activity 5
minimum()

# Test Activity 6
check_even_odd()

# Test Activity 7
power()

# Test Activity 8
cube()

# Test Activity 9
multiplication_table()
