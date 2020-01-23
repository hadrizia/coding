#!/bin/python

import math
import os
import random
import re
import sys

def countDeletions(dict_a, dict_b):
  deletions = 0

  for letter in dict_a:
    if letter not in dict_b:
      deletions += dict_a[letter]
  
    elif letter in dict_a and letter in dict_b:
      deletions += abs(dict_a[letter] - dict_b[letter])
  
  for letter in dict_b:
    if letter not in dict_a:
      deletions += dict_b[letter]

  return deletions

def countLettersFrequency(string):
  d = {}
  for letter in string:
    if letter not in d:
      d[letter] = 1
    else:
      d[letter] += 1
  
  return d

# Complete the makeAnagram function below.
def makeAnagram(a, b):
  deletions = 0

  dict_a = countLettersFrequency(a)
  dict_b = countLettersFrequency(b)

  deletions = countDeletions(dict_a, dict_b)

  return deletions

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    # fptr.write(str(res) + '\n')

    # fptr.close()
