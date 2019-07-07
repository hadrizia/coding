# Complete the rotLeft function below.
def rotLeft(a, d):
  newPos = []
  if d == 0:
    newPos = a
  else :
    newPos.extend(a[d:])
    newPos.extend(a[0:d])
  
  return newPos


a = [1, 2, 3, 4, 5]
d = 3

print rotLeft(a, d)