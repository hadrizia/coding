'''
  Input
  The input contains several test cases. Each test case is composed by two lines. The first line of a test case contains two integers A and C, separated by a blank space, indicating, respectively, the height (1 ≤ A ≤ 104) and the length (1 ≤ C ≤ 104) of the block to be sculpted, in milimeters. The second line contains C integers Xi, each one indicating the final height, in milimeters of the block between the positions i and i + 1 through the length (0 ≤ Xi ≤ A, for 0 ≤ i ≤ C - 1). Consider that on each step, a layer of width 1 mm is removed on the parts of the block where the laser is turned on.

  The end of the input is indicated by a line that contains only two zeros, separated by a blank space.

  Output
  For each test case, your program must print a single line, containing an integer, indicating the number of times that the laser must be turned on to sculpt the block in the indicated format.
  
  Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1107
'''

def laser_sculpture():
  raw_input = input()
  while raw_input != "0 0":
    h = int(raw_input.split(" ")[0])
    l = int(raw_input.split(" ")[1])

    last_block = h
    moves = 0

    blocks = [int(x) for x in input().split(" ")]

    for b in blocks:
      if last_block > b:
        moves += (h - b) - (h - last_block)
      last_block = b

    print(moves)
    raw_input = input()

laser_sculpture()