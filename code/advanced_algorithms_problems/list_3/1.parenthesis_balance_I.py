'''
  Considering an expression with parenthesis, print a message informing if the among of parenthesis is correct or incorrect, without considering the rest of the expression.

  Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1068
'''

def parenthesis_balance(exp):
  stack = []

  for e in exp:
    if e == "(":
      stack.append("(")
    elif e == ")":
      if not stack:
        return 'incorrect'
      else:
        stack.pop()
  
  return 'correct' if not stack else 'incorrect'

def main():
  while True:
    try:
      exp = input()
      exp = [x for x in exp if x in [")", "("]]
      print(parenthesis_balance(exp))
    except EOFError: 
      break

main()