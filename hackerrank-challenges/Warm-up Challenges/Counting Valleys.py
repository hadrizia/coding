# Complete the countingValleys function below.
'''
  Time efficienty: O(n)
'''
def countingValleys(n, s):
  count = 0
  if n > 1:
    alt = 0
    for step in s:
      if step == 'U':
        alt += 1
        if alt == 0:
          count += 1 
      else:
        alt -= 1
  return count

n = 8
s = ["U", "D", "D", "D", "U", "D", "U", "U", "D", "D", "U", "U"]

print countingValleys(n, s)