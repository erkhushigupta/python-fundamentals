#Python code that finds prime numbers within a given range using functions:

#In this code, we define two functions: is_prime(n) to check if a number is prime,
# and find_primes(start, end) to find all prime numbers within a given range.
 
#is_prime(n): This function takes a number n as input and determines if it is a prime number. It performs the following steps:
#If n is less than or equal to 1, it returns False since prime numbers are greater than 1.
#It iterates over the range from 2 to the square root of n (inclusive) using the range() function and the int() function to ensure we get an integer value.
#For each number i in the range, it checks if n is divisible by i. If it is, n is not a prime number and the function returns False.
#If no divisors are found, the function returns True, indicating that n is a prime number.
#find_primes(start, end): This function takes two parameters, start and end, representing the range within which we want to find prime numbers. It performs the following steps:
#It initializes an empty list called primes to store the prime numbers found.
# It iterates over each number in the range from start to end (inclusive) using the range() function.
#For each number num in the range, it calls the is_prime() function to check if num is prime.
#If num is prime, it appends it to the primes list.
#Finally, it returns the primes list containing all the prime numbers found within the specified range.

#The main code prompts the user to enter the start and end numbers, then calls the find_primes() function with the provided range. It displays the prime numbers returned by the function using the print() function.





def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))

prime_numbers = find_primes(start_num, end_num)
print("Prime numbers between", start_num, "and", end_num, "are:")
print(prime_numbers)


#To use the code, you'll need to input the start and end numbers. 
# The code will then call the find_primes() function with the provided range and display the prime numbers it finds.