'''
  Valera is afraid of getting lost on the resort. So he wants you to come up with a path he would walk along. The path must consist of objects v1, v2, ..., vk (k ≥ 1) and meet the following conditions:

  Objects with numbers v1, v2, ..., vk - 1 are mountains and the object with number vk is the hotel.
  For any integer i (1 ≤ i < k), there is exactly one ski track leading from object vi. This track goes to object vi + 1.
  The path contains as many objects as possible (k is maximal).
  Help Valera. Find such path that meets all the criteria of our hero!

  Link: http://codeforces.com/problemset/problem/350/B
'''

def create_graph():
  n = int(input())
  input_types = input().split(" ")
  types = [int(i) for i in input_types]

  input_vertex = input().split(" ")
  prev = [0 for i in range(n)]
  cntFrom =[0 for i in range(n)]

  for i in range(n):
    prev[i] = int(input_vertex[i])
    prev[i] -= 1
    if (prev[i] != -1):
      cntFrom[prev[i]] += 1

  ans = []
  for i in range(n):
    if types[i] == 1:
      curV = i
      cur = []
      
      while prev[curV] != -1 and cntFrom[prev[curV]] <= 1:
        cur.append(curV)
        curV = prev[curV]
      
      cur.append(curV)
      
      if len(ans) < len(cur):
        ans = cur

  ans_alt = [str(i + 1) for i in ans[::-1]]
  
  print(len(ans_alt))
  return(' '.join(ans_alt))


print(create_graph())

  