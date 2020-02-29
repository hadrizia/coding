from code.data_structures.linkedlist.node import Node
from code.data_structures.stack.stack import Stack

class MinStack(object):
  def __init__(self, top = None):
    self.top = top
  
  def push(self, value):
    if self.is_empty():
      new_node = Node(value)
    else:  
      if self.top.data >= value:
        new_node = Node(value)
      else:
        new_node = self.top
      new_node.next = self.top
    self.top = new_node

  def pop(self):
    if not self.is_empty():
      deleted_node = self.top
      self.top = self.top.next
      return deleted_node
  
  def min(self):
    if not self.is_empty():
      return self.top
  
  def is_empty(self):
    return self.top == None

def push(stack, min_stack, value):
  stack.push(value)
  min_stack.push(value)

def pop(stack, min_stack):
  min_stack.pop()
  return stack.pop()

def min(min_stack):
  return min_stack.min()


def tests():
  stack = Stack()
  min_stack = MinStack()

  push(stack, min_stack, 5)
  assert min(min_stack).data == 5

  push(stack, min_stack, 6)
  assert min(min_stack).data == 5

  push(stack, min_stack, 3)
  assert min(min_stack).data == 3

  pop(stack, min_stack)
  assert min(min_stack).data == 5


if __name__ == "__main__":
  tests()