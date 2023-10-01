"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# A ValueError will occur if you enter a value that cannot be converted to an integer
# when you are prompted to enter the numerator or denominator. For example, if you
# enter a non-numeric value like "abc," it will raise a ValueError.

# When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur if you enter 0 as the denominator because dividing by
# zero is mathematically undefined.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, you can change the code to avoid the possibility of a ZeroDivisionError by
# adding a conditional statement that checks if the denominator is zero before
# performing the division. Here's the modified code:


