from code.data_structures.stack.stack import Stack

class MyQueue(object):
  def __init__(self, stack = Stack(), aux = Stack(), top = None, tail = None):
    self.stack = stack
    self.aux = aux
    self.top = top
    self.tail = tail
  
  def enqueue(self, value):
    if self.is_empty():
      self.stack.push(value)
      self.top = self.stack.top
    else:
      self.stack.push(value)
    self.tail = self.stack.top
  
  def dequeue(self):
    while not self.stack.is_empty():
      self.aux.push(self.stack.pop().data)

    deletednode = self.aux.pop()
    self.top = self.aux.peek()

    while not self.aux.is_empty():
      self.stack.push(self.aux.pop())
    
    return deletednode

  def is_empty(self):
    return self.stack.is_empty()

  def size(self):
    return self.stack.size()


def tests():
  queue = MyQueue()
  queue.enqueue(1)
  assert queue.top.data == 1
  assert queue.tail.data == 1

  queue.enqueue(2)
  assert queue.top.data == 1
  assert queue.tail.data == 2

  queue.enqueue(3)
  assert queue.size() == 3

  queue.dequeue()

  assert queue.top.data == 2
  assert queue.tail.data == 3

  assert queue.size() == 2

if __name__ == "__main__":
  tests()

  
    
