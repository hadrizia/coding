'''
  Input
    The first line contains integer q (1 ≤ q ≤ 1000), the number of handle change requests.
    Next q lines contain the descriptions of the requests, one per line.
    Each query consists of two non-empty strings old and new, separated by a space. The strings consist of lowercase and uppercase Latin letters and digits. Strings old and new are distinct. The lengths of the strings do not exceed 20.
    The requests are given chronologically. In other words, by the moment of a query there is a single person with handle old, and handle new is not used and has not been used by anyone.

  Output
    In the first line output the integer n — the number of users that changed their handles at least once.
    In the next n lines print the mapping between the old and the new handles of the users. Each of them must contain two strings, old and new, separated by a space, meaning that before the user had handle old, and after all the requests are completed, his handle is new. You may output lines in any order.
    Each user who changes the handle must occur exactly once in this description.

    Link: http://codeforces.com/problemset/problem/501/B
'''

def changing_handles(n):
  handles = {}
  for _ in range(n):
    old, new = input().split(" ")

    if old not in handles:
      handles[new] = old
    else:
      handles[new] = handles[old]
      del handles[old]
  return handles

def main():
  m = int(input())
  h = changing_handles(m)

  print(len(h))
  for k, v in h.items():
    print(v, " ", k)

main()