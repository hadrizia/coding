'''
  Given two arrays (A and B) sorted in ascending order, and an integer x. 
  we need to find i and j, such that a[i] + b[j] is equal to X.
'''

def check_sum(a, b, num):
  i = 0
  j = len(b) - 1

  while i < len(a) and j >= 0:
    sum_value = a[i] + b[j]

    if sum_value == num:
      return True
    elif sum_value > num:
      j -= 1
    else:
      i += 1
  
  return False


a = [1, 2, 3, 4, 5, 6]
b = [2, 4, 5, 8, 9]

assert check_sum(a, b, 7)
assert not check_sum(a, b, 21)