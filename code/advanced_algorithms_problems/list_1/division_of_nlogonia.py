def division(k):
  divisor_x, divisor_y = input().split()
  divisor_x = int(divisor_x)
  divisor_y = int(divisor_y)

  for _ in range(k):

    x, y = input().split()
    x = int(x)
    y = int(y)

    if x == divisor_x or y == divisor_y:
      print('divisa')
      
    else:
      res = []
      if y > divisor_y:
        res.append('N')
      else:
        res.append('S')

      if x > divisor_x:
        res.append('E')
      else:
        res.append('O')

      print(''.join(res))
    

division(4)
