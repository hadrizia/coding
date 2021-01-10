'''
Given the initial configuration of the toy cubes in the box, find the amounts of cubes in each of the n columns after the gravity switch!

Input
The first line of input contains an integer n (1 ≤ n ≤ 100), the number of the columns in the box. The next line contains n space-separated integer numbers. The i-th number ai (1 ≤ ai ≤ 100) denotes the number of cubes in the i-th column.

Output
Output n integer numbers separated by spaces, where the i-th number is the amount of cubes in the i-th column after the gravity switch.

Link: https://codeforces.com/problemset/problem/405/A
'''
def mergesort(n, l, m, r):
  n1 = (m - l) + 1
  n2 = r - m
  

  left = [0] * n1
  right = [0] * n2

  for i in range(n1):
    left[i] = n[i + l]

  for j in range(n2):
    right[j] = n[m + 1 + j]

  i = 0
  j = 0
  k = l

  while i < len(left) and j < len(right):
    if left[i] >= right[j]:
      n[k] = right[j]
      j += 1
    else:
      n[k] = left[i]
      i += 1

    k += 1

  while i < n1:
    n[k] = left[i]
    i += 1
    k += 1
  
  while j < n2:
    n[k] = right[j]
    k += 1
    j += 1
  return n

def merge(n, l, r):
  if r <= l:
    return
 
  m = (l + r) // 2
 
  merge(n, l, m)
  merge(n, m + 1, r)

  mergesort(n, l, m, r)


def gravity_flip(n):
  return merge(n, 0, len(n) - 1)

n = [1,5, 6, 3, 1, 8, 4]
gravity_flip(n)
print(n)