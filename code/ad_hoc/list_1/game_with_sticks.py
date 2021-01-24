'''
  The rules of the game are very simple. 
  The players move in turns. Akshat won gold, so he makes the first move.
  During his/her move, a player must choose any remaining intersection point and 
  remove from the grid all sticks which pass through this point. 
  A player will lose the game if he/she cannot make a move 
  (i.e. there are no intersection points remaining on the grid at his/her move).

Assume that both players play optimally. Who will win the game?
  Link: https://codeforces.com/problemset/problem/451/A
'''

def game_with_sticks(n, m):
  round_num = 0
  while n >= 1 and m >= 1:
    n -= 1
    m -= 1
    round_num += 1

  return "Akshat" if round_num % 2 != 0 else "Malvika"
