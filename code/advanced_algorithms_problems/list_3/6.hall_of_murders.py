'''
  Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1861
'''

def murderes():
  hall = {}
  killed = set()
  while True:
    try:
      m, v = input().split(" ")
      killed.add(v)

      if v in hall:
        del hall[v]

      if m not in killed:
        if m in hall:
          hall[m] += 1
        else:
          hall[m] = 1
    except:
      print("HALL OF MURDERERS")
      for k in sorted(hall):
        print(k, hall[k])
      break

murderes()
