'''
  Iahub wants to destroy as many balls as possible. You are given the description of the row of balls, and the color of Iahub's ball. Help Iahub train for the IOI by telling him the maximum number of balls from the row he can destroy.

  Input
  The first line of input contains three integers: n (1 ≤ n ≤ 100), k (1 ≤ k ≤ 100) and x (1 ≤ x ≤ k). The next line contains n space-separated integers c1, c2, ..., cn (1 ≤ ci ≤ k). Number ci means that the i-th ball in the row has color ci.

  It is guaranteed that the initial row of balls will never contain three or more contiguous balls of the same color.

  Output
  Print a single integer — the maximum number of balls Iahub can destroy.

  Link: https://codeforces.com/problemset/problem/430/B
'''

def balls_game():
  n, k, x = input().split(" ")
  n = int(n)
  balls = [int(x) for x in input().split(" ")]
  ans = 0

  for k in range(len(balls)):
    i = k
    j = i + 1
    cnt = 1
    cur = int(x)
    while True:
      pre_i = i
      pre_j = j

      while i >= 0 and balls[i] == cur:
        i -=1
        cnt += 1

      while j < n and balls[j] == cur:
        j += 1
        cnt += 1

      if cnt <= 2:
        i = pre_i
        j = pre_j
        break
      
      else:
        cur = balls[i]
        cnt = 0
      ans = max(ans, j - i - 1)
  return(ans)

print(balls_game())