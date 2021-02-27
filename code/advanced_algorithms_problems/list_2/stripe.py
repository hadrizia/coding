'''
  Once Bob took a paper stripe of n squares (the height of the stripe is 1 square). 
  In each square he wrote an integer number, possibly negative. 
  He became interested in how many ways exist to cut this stripe into two pieces 
  so that the sum of numbers from one piece is equal to the sum of numbers from the other piece, 
  and each piece contains positive integer amount of squares. 
  Would you help Bob solve this problem?

  Link: https://codeforces.com/problemset/problem/18/C
'''

def stripe(len_numbers, numbers):
  n = 0

  stripe_1 = numbers[0]
  stripe_2 = sum(numbers[1:])

  for i in range(1, len_numbers):
    if stripe_1 == stripe_2:
      n += 1
    stripe_1 += numbers[i]
    stripe_2 -= numbers[i]

  return n

