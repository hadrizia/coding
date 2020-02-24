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

  def prettify(self):
    node = self.top
    array = []

    while node.next:
      print(node.next.data)
      array.append((node.data, node.next.data))
      node = node.next
    array.append((node.data, node.next))
    return array