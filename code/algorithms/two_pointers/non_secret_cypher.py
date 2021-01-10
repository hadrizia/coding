'''
Help Vasya, given an array of integers a and number k, find the number of subarrays of the array of numbers a, which has at least k equal numbers.

Subarray a[i... j] (1 ≤ i ≤ j ≤ n) of array a = (a1, a2, ..., an) is an array, made from its consecutive elements, starting from the i-th one and ending with the j-th one: a[i... j] = (ai, ai + 1, ..., aj).

Input
The first line contains two space-separated integers n, k (1 ≤ k ≤ n ≤ 4·105), showing how many numbers an array has and how many equal numbers the subarrays are required to have, correspondingly.

The second line contains n space-separated integers ai (1 ≤ ai ≤ 109) — elements of the array.

Output
Print the single number — the number of such subarrays of array a, that they have at least k equal integers.

Link: https://codeforces.com/contest/190/problem/D
'''

def get_count(a, i, j, k):
  count = {}
  for elem in range(i, j + 1):
    num = a[elem]
    if num in count:
      count[num] += 1
      if count[num] >= k:
        return True
    else:
      count[num] = 1
  return False
    
def decipher(a, k):
  i = 0
  res = 0

  while i < len(a):
    j = i
    while j < len(a):
      if get_count(a, i, j, k):
        res += 1
      j += 1
    i += 1
  return res


def tests():
  a = [1, 2, 1, 2]
  k = 2
  assert decipher(a, k) == 3

  a = [1, 2, 1, 1, 3]
  k = 3
  assert decipher(a, k) == 2

  a = [1, 1, 1]
  k = 1
  assert decipher(a, k) == 6