'''
  There is a bag-like data structure, supporting two operations:
    1 x
    Throw an element x into the bag.

    2
    Take out an element from the bag.
  Given a sequence of operations with return values, you're going to guess the data structure. It is a stack (Last-In, First-Out), a queue (First-In, First-Out), a priority-queue (Always take out larger elements first) or something else that you can hardly imagine!

  Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1340
'''

def guess(n):
  ds = []
  max_num = 0
  is_stack = True
  is_queue = True
  is_priority_queue = True

  for _ in range(n):
    op, x = input().split(" ")
    x = int(x)
    if op == "1":
      ds.append(x)
      if x > max_num:
        max_num = x
    elif op == "2":
      if x not in ds:
        return 'impossible'
      else:
        if len(ds) > 1:
          if x == ds[-1] and is_stack:
            is_stack = True
          else:
              is_stack = False
          if x == ds[0] and is_queue:
              is_queue = True
          else:
              is_queue = False
          if x == max_num and is_priority_queue:
              is_priority_queue = True
          else:
              is_priority_queue = False
      ds.remove(x)
      if is_priority_queue and ds:
        max_num = max(ds)
  
  if (
    (is_priority_queue and is_queue) or 
    (is_stack and is_queue) or 
    (is_priority_queue and is_stack)):
    return 'not sure'
  elif is_priority_queue:
    return 'priority queue'
  elif is_queue:
    return 'queue'
  elif is_stack:
    return 'stack'
  else:
    return 'impossible'


def main():
  while True:
    try:
      m = input().split(" ")
      if len(m) == 1:
          m = int(m[0])
          print(guess(m))
    except EOFError:
      break


main()