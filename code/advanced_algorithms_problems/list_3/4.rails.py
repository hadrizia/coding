'''
  Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1062
'''
# [5, 4, 3, 2, 1]
# [1 3 2 5 4 6]
# 2 3 1 5 4

# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def rails(seq, train):
  station = []
  A = []
  B = []
  target = train
  for i in seq:
    A.append(i)
  
  while A:
    coach = A.pop()
    if coach == target:
      B.insert(0, coach)
      target -= 1
      if station:
        while station:
          if station[-1] == target:
            B.insert(0, station.pop())
            target -= 1
          else:
            break
    else:
      if station:
        while station:
          if station[-1] == target:
            B.insert(0, station.pop())
            target -= 1
          else:
            station.append(coach)
            break
      else:
        station.append(coach)
  
  exp_output = [i for i in range(1, train + 1)]

  return B == exp_output

def main():
  n = int(input())
  while n != 0:
      try:
        coaches = [int(x) for x in input().split(" ")]
        if len(coaches) > 1 and coaches[0] != 0:
          if rails(coaches, n):
            print("Yes")
          else:
            print("No")
        if coaches == [0]:
          print("")
          n = int(input())
      except EOFError:
        break

main()
