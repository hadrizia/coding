'''
  You are given  queries. Each query is of the form two integers described below:
-  : Insert x in your data structure.
-  : Delete one occurence of y from your data structure, if present.
-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element

Link: https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''
from collections import defaultdict

def freqQuery(queries):
  d = defaultdict(int)
  ans = []
  f = defaultdict(int)
  
  for q in queries:
    op = q[0]
    n = q[1]

    if op == 1:
      if d[n] >= 1:
        f[d[n]] -= 1
      d[n] += 1
      f[d[n]] += 1
    
    elif op == 2 and n in d:
      f[d[n]] -= 1
      d[n] -= 1
      if d[n] >= 1:
        f[d[n]] += 1
      if d[n] == 0:
        del d[n]
        
    elif op == 3:
      flag = False
      if d:
          if n in f and f[n] >= 1:
            flag = True
      if flag:
          ans.append(1)
      else:
          ans.append(0)
  return ans

q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

freqQuery(queries)