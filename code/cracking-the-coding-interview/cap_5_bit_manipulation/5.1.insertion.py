def insertion(m, n, i, j):
  # Step 1: Clean the bits from i through j
  # Mask for left side: 1s0is
  left = (~ 0) << (i + 1)

  # Mask for right side: 0s1j
  right = (1 << i) - 1 
  
  # Merge masks
  mask = left | right
  cleaned_m = mask & m

  # Step 2: Shift n i times
  shifted_n = n << i

  # Step 3: Merge bits
  return cleaned_m | shifted_n

def tests():
  print(insertion(10000000, 10101, 6, 2))


if __name__== "__main__":
  tests()