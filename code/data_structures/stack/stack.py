from code.data_structures.linkedlist.node import Node

class Stack(object):
  def __init__(self, top = None):
    self.top = top
  
  def push(self, data):
    new_top = Node(data)
    new_top.next = self.top
    self.top = new_top

  def pop(self):
    if not self.is_empty():
      deleted_node = self.top
      self.top = self.top.next
      return deleted_node

  def peek(self):
    return self.top
  
  def is_empty(self):
    return self.top == None
  
  def size(self):
    node = self.top
    count = 0
    while node:
      count += 1
      node = node.next
    return count

  def remove_bottom(self):
    if not self.is_empty():
      aux_stack = Stack()
      while not self.is_empty():
        aux_stack.push(self.pop().data)
      
      bottom = aux_stack.pop()
      
      while not aux_stack.is_empty():
        self.push(aux_stack.pop().data)
      
      return bottom
      

  def prettify(self):
    node = self.top
    array = []
    
    while node:
      array.append(node.data)
      node = node.next
    return array