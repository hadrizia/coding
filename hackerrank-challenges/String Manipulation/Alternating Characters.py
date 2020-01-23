#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
  deletions = 0
  for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
      deletions += 1
  
  print deletions
  return deletions

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        # fptr.write(str(result) + '\n')

    # fptr.close()
