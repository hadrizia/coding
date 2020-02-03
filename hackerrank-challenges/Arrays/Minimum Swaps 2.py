#!/bin/python

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
  numSwaps = 0
  i = 0
  while(i < len(arr) - 1):
    if arr[i] != i + 1:
      tmp = arr[i]
      arr[i], arr[tmp - 1] = arr[tmp - 1], arr[i]
      print arr
      numSwaps += 1
    else:
      i += 1
  return numSwaps


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)
    print res

    # fptr.write(str(res) + '\n')

    # fptr.close()
