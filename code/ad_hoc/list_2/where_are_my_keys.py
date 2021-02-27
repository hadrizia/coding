'''
  Input
  The first line contains two integers Q(1 ≤ Q ≤ 1*103) and E(1 ≤ E ≤ Q) representing respectively the number of offices that he was in the last week and the number of offices that he was in the last two days.

  The second line contains E integers Si (1 ≤ Si ≤ 1000) containing the Identification number of each office that he was in the last two days.

  The next line contains Q integers Ci (1 ≤ Ci ≤ 1000) containing the identification number of each one of the offices that he was in the last week.

  Output
  For each office that he was in the last week your program should return “0” in case he has already visited that office while looking for the keys. Else your program should return “1” in case he hasn't visited that office yet while he was looking for the keys.
  
  Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1800
'''

def was_room_visited():
  total_offices = int(input().split(" ")[0])
  visited_offices = [int(x) for x in input().split(" ")]

  for _ in range(total_offices):
    office = int(input())
    if office not in visited_offices:
      print(1)
      visited_offices.append(office)
    else:
      print(0)

was_room_visited()