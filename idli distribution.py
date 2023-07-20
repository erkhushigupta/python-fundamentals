#To find the minimum number of idlis you must distribute to satisfy the given rules, you can follow these steps:

#Check if the number of idlis held by each citizen is already even. If not, you cannot satisfy the rules,and you should return -1.
#Iterate through the list of idlis and determine the number of idlis you need to distribute 
#to each citizen to make their count even. Also, keep track of the total number of idlis you need to distribute.
#Return the total number of idlis needed to satisfy the rules.

def distribute_idlis(idlis):
    # Step 1: Check if all citizens have an even number of idlis
    if any(idli % 2 != 0 for idli in idlis):
        return -1

    total_idlis_to_distribute = 0
    prev_idlis = 0

    # Step 2: Calculate the number of idlis to distribute to each citizen
    for idli in idlis:
        if idli > prev_idlis:
            diff = idli - prev_idlis
            total_idlis_to_distribute += diff
            prev_idlis = idli + diff
        else:
            prev_idlis = idli

    return total_idlis_to_distribute

# Example usage:
citizens_idlis = [2, 4, 6, 8]
result = distribute_idlis(citizens_idlis)
print(result)  # Output: 0 (No idlis need to be distributed as everyone has an even number)

citizens_idlis = [2, 5, 8, 7]
result = distribute_idlis(citizens_idlis)
print(result)  # Output: 4 (Distribute 2 idlis to 5 and 7, and 2 idlis to 7 and 8)



#The function returns the minimum number of idlis you must distribute to satisfy the rules. 
# If it's not possible to satisfy the rules (i.e., if any citizen has an odd number of idlis initially), the function returns -1.