# code to Check if Two Strings are Anagram



def is_anagram(str1, str2):
    # Convert both strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character frequencies
    char_freq1 = {}
    char_freq2 = {}

    # Calculate character frequencies for str1
    for char in str1:
        char_freq1[char] = char_freq1.get(char, 0) + 1

    # Calculate character frequencies for str2
    for char in str2:
        char_freq2[char] = char_freq2.get(char, 0) + 1

    # Check if the dictionaries are equal
    if char_freq1 == char_freq2:
        return True
    else:
        return False

# Test the function
print(is_anagram('elle', 'leel'))    # True
print(is_anagram('hello', 'olleh'))  # True
print(is_anagram('elle', 'leele'))   # False
print(is_anagram('hello', 'lehle'))  # False



#The function is_anagram takes two input strings, converts them to lowercase, removes whitespace, and then compares
#  the frequencies of the characters in both strings. 
# If the frequencies are equal, it returns True, indicating that the strings are anagrams. 
# Otherwise, it returns False. The provided examples are tested at the end to demonstrate the function's usage.