# This program can be used to find the factors of an entered number using for loops

num = int(input("Enter a number: "))

print("The factors of", num, "are:")

# loop from 1 to num
for i in range(1, num + 1):
  
  # check if num is divisible by i, if yes print it
  if num % i == 0:
    print(i, end=' ')

#Input: 190
#Expected output: The factors of 190 are:
#1 2 5 10 19 38 95 190 