'''
  An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 
  and his friend's house is located at point x(x > 0) of the coordinate line. 
  In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. 
  Determine, what is the minimum number of steps he need to make in order to get to his friend's house.
  Link: http://codeforces.com/problemset/problem/617/A
'''

def minimum_steps(local):
  possible_steps = [1, 2, 3, 4, 5]
  possible_steps.sort(reverse=True)
  steps = 0

  for p in possible_steps:
    while local >= p and local > 0:    
      steps += local // p
      local = local % p       
      
  return steps
