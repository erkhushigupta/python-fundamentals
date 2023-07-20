#To convert a given number to words in either Indian or Western form, you can implement a Python function that handles both cases. 
#The function should take the number as input and a flag to indicate whether to use the
# Indian or Western naming system for numbers

def number_to_words(num, indian_format=True):
    # Define the words for the digits in Indian and Western format
    indian_words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    western_words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    # Words for the multiples of ten up to 90
    tens_words = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # Words for special numbers from 11 to 19
    special_words = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    if indian_format:
        # For Indian format, add "Hundred", "Thousand", "Lakh", and "Crore" as required
        scales_words = ["", "Hundred", "Thousand", "Lakh", "Crore"]
    else:
        # For Western format, add "Hundred", "Thousand", "Million", and "Billion" as required
        scales_words = ["", "Hundred", "Thousand", "Million", "Billion"]

    # Function to convert a three-digit number to words
    def convert_three_digits(number):
        hundreds_digit = number // 100
        tens_digit = (number % 100) // 10
        units_digit = number % 10

        words = ""
        if hundreds_digit > 0:
            words += indian_words[hundreds_digit] + " " + scales_words[1] + " "

        if tens_digit > 1:
            words += tens_words[tens_digit] + " "
            if units_digit > 0:
                words += indian_words[units_digit] + " "
        elif tens_digit == 1:
            words += special_words[units_digit] + " "
        else:
            if units_digit > 0:
                words += indian_words[units_digit] + " "

        return words

    # Handle special cases for zero and negative numbers
    if num == 0:
        return "Zero"
    elif num < 0:
        return "Minus " + number_to_words(-num, indian_format)

    # Convert the number to words
    words = ""
    num_str = str(num)
    num_len = len(num_str)

    while num_len > 0:
        if num_len % 2 == 0:  # Group the number in sets of three digits
            group = int(num_str[:3])
            num_str = num_str[3:]
            num_len -= 3
            words += convert_three_digits(group) + scales_words[num_len // 2] + " "
        else:  # Handle the first one or two digits separately
            group = int(num_str[:2])
            num_str = num_str[2:]
            num_len -= 2
            words += convert_three_digits(group) + scales_words[num_len // 2] + " "

    return words.strip()

# Example usage:
num = 987654321
print("Indian format:", number_to_words(num, indian_format=True))
print("Western format:", number_to_words(num, indian_format=False))


#The function number_to_words converts a given number to words either in Indian or Western form based on the indian_format flag. 
# It supports numbers up to the billions place. For larger numbers, you can add more scale words as required.

 