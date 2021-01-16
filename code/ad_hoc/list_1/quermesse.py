test_num = 0
k = int(input())

while k > 0:
  test_num += 1
  
  array_input = input()
  array = [int(x) for x in array_input.split()]
	
  for i in range(len(array)):
    if array[i] == i + 1:
      print('Teste %d' % test_num)
      print(array[i])
    

  k = int(input())