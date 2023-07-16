#Finding prime numbers withing a user defined range using the map function



# The filter() function is used within the find_primes() function to filter out non-prime numbers from the range.
 
#The filter() function takes two arguments: the function is_prime() and the iterable range(start, end + 1).
# It applies the is_prime() function to each element in the iterable and returns only those elements 
#for which the function returns True


#We convert the filtered result to a list using the list() function and return it as the result of the find_primes() function.



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    return list(filter(is_prime, range(start, end + 1)))

start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))

prime_numbers = find_primes(start_num, end_num)
print("Prime numbers between", start_num, "and", end_num, "are:")
print(prime_numbers)

#Input: start no:3.End no:76

#expected output:Prime numbers between 3 and 76 are:
#[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]