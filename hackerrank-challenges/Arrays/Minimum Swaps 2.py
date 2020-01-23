#!/bin/python

import math
import os
import random
import re
import sys

swaps = 0

def countSwaps():
  global swaps
  swaps += 1


def partition(arr, low, high): 
    i = (low - 1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
      if   arr[j] <= pivot: 
        i = i + 1 
        arr[i], arr[j] = arr[j], arr[i]
        countSwaps() 
        
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
      
    return i + 1 
 
def quickSort(arr, low, high): 
    if low < high: 
      pi = partition(arr, low, high)
      quickSort(arr, low, pi - 1) 
      quickSort(arr, pi + 1, high)

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
  quickSort(arr, 0, len(arr) - 1)
  print swaps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    # fptr.write(str(res) + '\n')

    # fptr.close()
