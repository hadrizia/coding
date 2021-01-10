'''
  Given n numbers, find pairs with difference x.
'''

def find_pairs(n, x):
  n.sort()
  i = 0
  pairs = []

  while i < len(n) - 1:
    j = i + 1
    while j < len(n):
      if n[i] + n[j] == x:
        pairs.append((n[i], n[j]))
      j += 1
    i += 1
  return pairs


n = [1, 6, 0, 2, 5, 4, 7, 9]
x = 9

print(find_pairs(n, x))