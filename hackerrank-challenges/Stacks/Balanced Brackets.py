#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
# Complete the isBalanced function below.
def isBalanced(s):
  stack = []
  opening = ['{', '[', '(']
  closing = ['}', ']', ')']

  for char in s:
      if char in opening:
        stack.append(char)
      elif len(stack) > 0 and char in closing:
        index = closing.index(char)
        if opening[index] == stack[len(stack) - 1]:
            stack.pop()
        else:
          return 'NO'
          break
      elif char in closing:
        return 'NO'
        break

  if len(stack) == 0:
    return 'YES'
   

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        print result

    #fptr.close()
