'''
  You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to 
  find the length of the longest sequence of ls you could create.
  EXAMPLE
  Input: 1775 (or: 11011101111)
  Output: 8
'''

def flip_to_win(n):
  curr_length = 0
  previous_length = 0
  max_length = 1

  while n != 0:
    if n & 1 == 1:
      curr_length += 1
    else: # Check the next bit: if it's 0, prev_length is 0. Otherwise is curr_length.
      previous_length = 0 if n & 2 == 0 else curr_length
      curr_length = 0
    max_length = max(max_length, curr_length + previous_length + 1)
    n = n >> 1
  return max_length


def main():
  assert flip_to_win(1775) == 8
  assert flip_to_win(7) == 4

if __name__== "__main__":
  main()