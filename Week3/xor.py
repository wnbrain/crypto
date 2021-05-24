"""
Create a function named xor which takes two ascii codes,
prints their binary, then performs a bitwise XOR using the ^ (caret) operator,
prints the result of the XOR, then returns the result.
"""
from helper_functions import binary, FIX_ME

"""
Using code from the bitwise_and() function (see helper_functions.py), create an additional function called xor() which perform the XOR operation.
"""


def xor(ascii_code_a, ascii_code_b):
    # FIX_ME('Implement the xor() function')  #  You can delete this line once you implement your function.
    # return 42  # Return the correct result.
    #print(f'The binary of ascii_code_a and ascii_code_b are: {binary(ascii_code_a)} and {binary(ascii_code_b)} ')
    result = ascii_code_a ^ ascii_code_b
    print(f'Result: {binary(result)}')
    return binary(result)


if __name__ == '__main__':
    xor(85, 170)