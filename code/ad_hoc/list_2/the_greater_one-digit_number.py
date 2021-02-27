'''
  Input
  There will be several test cases . Each test case begins with two integers N and M ( 0 ≤ N ≤ 10100, 0 ≤ M ≤ 10100 ), indicating the two numbers to be compared. The last test case is given when N = M = 0 , and this case will not be processed.

  Output
  For each test case , print a line containing an integer, indicating 1 if the first number is the largest of a number , 2 if the second number is the largest of a number or 0 if both numbers have the same value of a number.

  Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1867
'''
def get_one_digit(number):
  if len(str(number)) == 1:
    return number
  else:
    new_num = 0
    nums = [int(x) for x in str(number)]
    for n in nums:
      new_num += n
    return(get_one_digit(new_num))

while True:
  n, m = [int(x) for x in input().split(" ")]

  if n == 0 and m == 0:
    break
  
  if get_one_digit(n) > get_one_digit(m):
    print(1)

  elif get_one_digit(n) == get_one_digit(m):
    print(0)

  else:
    print(2)


