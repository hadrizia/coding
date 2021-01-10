'''
  Question: Explain what the following code does: ( ( n & (n-1)) == 0).

    The expression (n-1) inverts all 0's and the first bit 1 (LSB).
    When we do an AND expression with n, two things could happen:
    1. We have a bin in format 10's followed by s zeros;
    2. We have all bits 0. This happens when n is pow of 2, 
    cause n only have a single 1 bit to be reverted and 
    the (n-1) will revert all bits, 
    so the AND operation reset all bits.
    So the code check if a number is a pow of 2 or not.
'''

n = 16
print(bin(n), bin(n-1), bin(n & (n-1)))
print(n & (n-1))