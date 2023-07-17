#The rot13 function iterates over each character in the input message. 
#If the character is alphabetic, it determines the ASCII offset based on whether it is uppercase or lowercase. 
#It then applies the ROT13 shift of 13 by subtracting the ASCII offset, adding 13, 
#taking the modulus 26 to ensure it stays within the range of alphabetic characters, and adding the ASCII offset back.
#The resulting character is concatenated to the result string.
#If the character is not alphabetic, it is simply added as is. Finally, the function returns the encrypted or decrypted string.



def rot13(message):
    result = ''
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result

# Test the function
encrypted = rot13("Hello, World!")
print(encrypted)  # Output: "Uryyb, Jbeyq!"

decrypted = rot13(encrypted)
print(decrypted)  # Output: "Hello, World!"

#In the example above, the function encrypts the message "Hello, World!" using ROT13 and then decrypts the encrypted message, 
# resulting in the original message again.