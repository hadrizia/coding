import heapq

class PriorityQueue(object):
  def __init__(self, queue = []):
    self.queue = []

  def push(self, new_el):
    heapq.heappush(self.queue, new_el)
  
  def peek(self):
    return self.queue[0]
  
  def pop(self):
    return heapq.heappop(self.queue)
  

q = PriorityQueue()
q.push(6)
q.push(4)
q.push(2)
q.push(3)

assert q.peek() == 2
assert q.pop() == 2
assert q.peek() == 3
q.pop()
q.push(1)
assert q.peek() == 1

