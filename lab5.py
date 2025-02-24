# Activity 1: Sum of Two Numbers
def sum_two_numbers(x, y):
    return x + y

# Activity 2: Sum of Three Numbers
def sum_three_numbers(x, y, z):
    return x + y + z

# Activity 3: Maximum of Two Numbers
def maximum(x, y):
    return max(x, y)

# Activity 4: Minimum of Two Numbers
def minimum(x, y):
    return min(x, y)

# Activity 5: Check if a Number is Even
def is_even(x):
    return x % 2 == 0

# Activity 6: Check if a Number is Odd
def is_odd(x):
    return x % 2 != 0

# Activity 7: Check if a Number is Divisible by 5
def divisible_by_5(x):
    return x % 5 == 0

# Activity 8: Check if a Number is Prime
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Activity 9: GCD of Two Numbers
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Activity 10: LCM of Two Numbers
def lcm(x, y):
    return (x * y) // gcd(x, y)


# Test the functions

# Test Activity 1
result = sum_two_numbers(2, 3)
print("Sum of 2 and 3:", result)

# Test Activity 2
result = sum_three_numbers(1, 2, 3)
print("Sum of 1, 2, and 3:", result)

# Test Activity 3
result = maximum(5, 1)
print("Maximum of 5 and 1:", result)

# Test Activity 4
result = minimum(5, 1)
print("Minimum of 5 and 1:", result)

# Test Activity 5
print("Is 4 even?", is_even(4))
print("Is 5 even?", is_even(5))

# Test Activity 6
print("Is 5 odd?", is_odd(5))
print("Is 4 odd?", is_odd(4))

# Test Activity 7
print("Is 10 divisible by 5?", divisible_by_5(10))
print("Is 12 divisible by 5?", divisible_by_5(12))

# Test Activity 8
print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))

# Test Activity 9
result = gcd(12, 18)
print("GCD of 12 and 18:", result)

# Test Activity 10
result = lcm(12, 18)
print("LCM of 12 and 18:", result)
