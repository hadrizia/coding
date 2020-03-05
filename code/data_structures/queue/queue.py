from code.data_structures.linkedlist.node import Node

class Queue(object):
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def enqueue(self, value):
    node = Node(value)
    if self.is_empty():
      self.head = node
      self.tail = node
    else:
      n = self.head
      while n.next:
        n = n.next
      n.next = node
      self.tail = node
  
  def dequeue(self):
    if not self.is_empty():
      n = self.head
      self.head = self.head.next
      return n

  def is_empty(self):
    return self.head == None