def check_digits_divide_number(n):
    # Convert the number to string to iterate through digits
    str_num = str(n)
    
    for digit in str_num:
        # Convert the digit back to an integer
        d = int(digit)
        
        # Check if the digit is zero or if the number is not divisible by the digit
        if d == 0 or n % d != 0:
            return False
            
    return True

# Example usage
number = int(input("Enter a number: "))
if check_digits_divide_number(number):
    print(f"All digits of {number} divide it.")
else:
    print(f"Not all digits of {number} divide it.")
