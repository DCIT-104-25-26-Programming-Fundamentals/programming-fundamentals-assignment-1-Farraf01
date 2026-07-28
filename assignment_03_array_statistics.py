# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================  

def finding_sum(numbers):
    nums = 0
    for num in numbers:
        nums += num
    return nums


def finding_average(numbers):
    nums = finding_sum(numbers)
    average = nums / len(numbers)
    return average


def finding_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def finding_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


nods = int(input("How many numbers? "))

if nods <= 0:
    print("Error: Number of values must be a positive integer.")

else:
    numbers = []

    for i in range(nods):
        items = float(input(f"Enter number {i + 1}: "))
        numbers.append(items)

    print("\nResults:")
    print("Sum:", finding_sum(numbers))
    print("Average:", finding_average(numbers))
    print("Maximum:", finding_maximum(numbers))
    print("Minimum:", finding_minimum(numbers))

