# Function to calculate factorial
def factorial(n):
    if n == 1 or n == 0:  # Base case
        return 1
    else:
        return n * factorial(n-1)  # Recursive call

# Input: Number to find factorial of
number = int(input("Enter a number: "))

# Output: Factorial of the number
result = factorial(number)
print(f"The factorial of {number} is {result}")
