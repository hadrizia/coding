'''
  Link: https://codeforces.com/problemset/problem/681/C
'''

import heapq

def print_operations(ops):
  print(len(ops))
  for o in ops:
    print(o)


def heap_operations(num_op):
  heap = []
  ops = []

  for _ in range(num_op):
    op = input()
    if op == "removeMin": # O(logN)
      if heap:
        heapq.heappop(heap)
      else:
        ops.append("insert 0")
      ops.append(op)
        
    else:
      op, n = op.split(" ")
      n = int(n)

      if op == "insert": # O(logN)
        heapq.heappush(heap, n)
        ops.append(op + " " + str(n))

      elif op == "getMin": 
        if not heap: # O(logN)
          heapq.heappush(heap, n)
          ops.append("insert " + str(n))

        elif heap[0] == n:
          pass

        else:
          while heap and heap[0] < n: # O(N * logN)
            heapq.heappop(heap) 
            ops.append("removeMin")

          if not heap or heap[0] < n: # O(logN)
            heapq.heappush(heap, n)
            ops.append("insert " + str(n))
        ops.append(op + " " + str(n))

  print_operations(ops)

    
def main():
  while True:
    try:
      num = int(input())
      heap_operations(num)
    except EOFError: 
      break


if __name__ == "__main__":
  main()