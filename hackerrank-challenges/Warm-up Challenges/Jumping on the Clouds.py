
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
  jumps = 0
  if len(c) > 1:
    current = 0
    while current < len(c) - 2: 
      if c[current + 2] == 0:
        current += 2
        jumps += 1
      elif c[current + 1] == 0:
        current += 1
        jumps += 1
    if current < len(c) - 1:
      current += 1
      jumps += 1

  return jumps


#c = [0, 0, 1, 0, 0, 1, 0]
#c = [0, 0, 0, 0, 1, 0]
c = [0, 0, 1, 0, 0, 1, 0]
#c = [0, 0, 0, 1, 0, 0]

print jumpingOnClouds(c)