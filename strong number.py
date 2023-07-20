#to check if a given integer is a strong number (a number that is equal to the sum of the factorials of its digits)

#  Define a helper function to calculate the factorial of a number.
#  Convert the integer to a string to access its individual digits.
#  Calculate the factorial of each digit and sum them up.
# Compare the sum with the original number to determine if it's a strong number.


def factorial(n):
    # Helper function to calculate the factorial of a number
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(num):
    num_str = str(num)
    digit_factorial_sum = sum(factorial(int(digit)) for digit in num_str)

    return num == digit_factorial_sum

# Example usage:
num1 = 145  # 1! + 4! + 5! = 1 + 24 + 120 = 145
num2 = 40585  # 4! + 0! + 5! + 8! + 5! = 24 + 1 + 120 + 40,320 + 120 = 40,585

print(is_strong_number(num1))  # Output: True (145 is a strong number)
print(is_strong_number(num2))  # Output: True (40,585 is a strong number)



#The function returns True if the given integer is a strong number and False otherwise.
#Keep in mind that 0 and 1 are considered strong numbers as they are equal to the factorial of their digits (0! = 1 and 1! = 1).