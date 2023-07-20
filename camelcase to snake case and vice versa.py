#to convert a variable name from snake_case to camelCase, you need to capitalize the first letter of each word 
#(except the first word) and remove the underscores. 
#Conversely, to convert camelCase to snake_case, you need to insert underscores before capital letters (except the first letter).


#Convert snake_case to camelCase:
def snake_to_camel(snake_case_string):
    words = snake_case_string.split('_')
    camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_string

# Example usage:
snake_case_var = "my_variable_name"
camel_case_var = snake_to_camel(snake_case_var)
print(camel_case_var)  # Output: "myVariableName"


#Convert camelCase to snake_case:

def camel_to_snake(camel_case_string):
    snake_case_string = ''.join('_' + char.lower() if char.isupper() else char for char in camel_case_string)
    return snake_case_string.lstrip('_')

# Example usage:
camel_case_var = "myVariableName"
snake_case_var = camel_to_snake(camel_case_var)
print(snake_case_var)  # Output: "my_variable_name"

#Both functions handle conversions between snake_case and camelCase. 
# However, please note that these functions assume valid input formats and do not handle incorrect or malformed variable names. 
# Additionally, they don't consider edge cases such as acronyms, 
# which might have different rules for conversion. For general use cases, these functions should work as intended.