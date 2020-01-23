#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
  arr.sort()
  minimum = abs(arr[0] - arr[1])
  
  for i in range(len(arr) - 1):
    minimum = min(minimum, abs(arr[i] - arr[i + 1]))

  return minimum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = minimumAbsoluteDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
