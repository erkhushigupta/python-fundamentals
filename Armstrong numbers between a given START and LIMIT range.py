#To generate all the Armstrong numbers between a given START and LIMIT range, 
#you can iterate through each number in the range and check if it satisfies the Armstrong number condition.
# If it does, add it to the list of Armstrong numbers.

def gen_armstrong(START, LIMIT):
    armstrong_numbers = []

    for num in range(START, LIMIT + 1):
        num_str = str(num)
        order = len(num_str)
        sum_of_powers = sum(int(digit) ** order for digit in num_str)

        if num == sum_of_powers:
            armstrong_numbers.append(num)

    return armstrong_numbers

# Example usage:
armstrong_numbers = gen_armstrong(100, 2000)
print(armstrong_numbers)  # Output: [153, 370, 371, 407, 1634]

#The function gen_armstrong takes START and LIMIT as input parameters and returns a list containing all the Armstrong numbers 
# In the specified range. It iterates through each number in the range, calculates the sum of the nth powers of its digits,
#  and checks if it equals the original number. If it does, the number is added to the list of Armstrong numbers.

#In the example usage, the function is called with the range (100, 2000), and it returns the list of Armstrong numbers 
# in that range: [153, 370, 371, 407, 1634].

