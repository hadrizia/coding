'''
  Input
  The input consists of several test cases. Each test case is composed of a line having an integer N, which is the nth number of the sequence to be calculated, with 0 <N <= 40.

  Output
  The output of each test case is a line containing only the nth number of the sequence.

  Link: https://www.urionlinejudge.com.br/judge/en/problems/view/2041
'''
from collections import defaultdict


def sequence(k, s = ["3"], i = 0):
  if i == k - 1:
    return s

  res = []
  count = 1

  if len(s) == 1:
    res.append(str(count))
    res.append(s[0])

  else:
    for n in range(len(s)):
      if n < len(s) - 1:
        if s[n] == s[n + 1]:
          count += 1
        else:
          res.append(str(count))
          res.append(s[n])
          count = 1
      elif n == len(s) - 1:
        res.append(str(count))
        res.append(s[n])
  i += 1
  return sequence(k, res, i)


def godelitos_sequence():
  try:
    n = int(input())
    while n:
      print(''.join(sequence(n)))
      n = int(input())
  except EOFError as e: 
    print(e)

godelitos_sequence()