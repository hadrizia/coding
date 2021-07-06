"""
A = [1, 3, 5, 8, 0, 0, 0, 0]
B = [1, 2, 5, 9]

A = [1, 1, 2, 3, 5, 5, 8, 9]

i = 7
j = 3
z = 7

while z >= 0 and A[z] != 0:
  z -= 1

z = 3
A[z] > B[j]? A[i] = A[z]; z-= 1 : A[i] = B[j] j -= 1; i -= 1


"""

def sorted_merge(A, B):

  i = len(A) - 1
  j = len(B) - 1

  z = i - len(B)

  while z >= 0 and j >= 0 and i >= 0:
    if B[j] > A[z]:
      A[i] = B[j]
      j -= 1
    else:
      A[i] = A[z]
      z -= 1
    i -= 1

  while i >= 0 and j >= 0:
    A[i] = B[j]
    j -= 1
    i -= 1
  
  while i >= 0 and z >= 0:
    A[i] = A[z]
    z -= 1
    i -= 1

  return A


def tests():
  assert sorted_merge([1, 3, 5, 8, 0, 0, 0, 0], [1, 2, 5, 9]) == [1, 1, 2, 3, 5, 5, 8, 9]
  assert sorted_merge([1, 3, 5, 8, 0, 0, 0, 0], [9, 10, 11, 12]) == [1, 3, 5, 8, 9, 10, 11, 12]
  assert sorted_merge([5, 6, 7, 8, 0, 0, 0, 0], [1, 2, 3, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]


tests()