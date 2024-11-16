def reverse_number(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Reverse the string
    reversed_str = number_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)
    
    return reversed_number

# Example usage
number = 12345
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number}")
