#A list is termed special if it has even numbers in even indices and odd numbers in odd indices.
#To check if a given list is a "SpeciaList" (a list with even numbers in even indices and odd numbers in odd indices), 
#you can iterate through the list and verify that the conditions are met for each element at the corresponding index.
 


def is_specialist(lst):
    for index, num in enumerate(lst):
        if index % 2 == 0:  # Even index
            if num % 2 != 0:  # Not an even number
                return False
        else:  # Odd index
            if num % 2 == 0:  # Not an odd number
                return False
    return True


# Example usage:
special_list_1 = [2, 7, 8, 3, 6, 5]
special_list_2 = [1, 6, 3, 8, 5, 4]

print(is_specialist(special_list_1))  # Output: True (even: 2, 8, 6; odd: 7, 3, 5)
print(is_specialist(special_list_2))  # Output: False (even: 6, 8, 4; odd: 1, 3, 5)

#The function returns True if the list is a SpeciaList and False otherwise.
#  Note that an empty list is considered a SpeciaList because it has no elements to violate the conditions.