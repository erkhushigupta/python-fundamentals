# code to implement Euler 001:

# Euler: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

def sum_multiples_3_5(limit):
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

result = sum_multiples_3_5(1000)
print(result)

#When you run this code, expected is:
# it will calculate the sum of all the multiples of 3 or 5 below 1000 and print the result, which should be 233168.