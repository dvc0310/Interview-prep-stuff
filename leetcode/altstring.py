def gcd(num1, num2):
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1

def check_divides(string, divisor):
    repeat_count = len(string) // len(divisor)
    repeated_divisor = divisor * repeat_count
    return repeated_divisor == string

def find_largest_common_divisor(str1, str2):
    # Calculate the greatest common divisor of the lengths.
    gcd_len = gcd(len(str1), len(str2))
    
    # Get the substrings of length gcd_len from both strings.
    substring1 = str1[:gcd_len]
    substring2 = str2[:gcd_len]

    # Check if the substrings are equal and if they can form str1 and str2.
    if substring1 == substring2 and check_divides(str1, substring1) and check_divides(str2, substring2):
        return substring1

    return ""


        