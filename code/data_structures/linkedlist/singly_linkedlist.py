from code.data_structures.linkedlist.node import Node 

class LinkedList(object):
  def __init__(self, head = None):
    self.head = head

  def insert_tail(self, data):
    new_node = Node(data)
    node = self.head

    if self.size() == 0:
      self.head = new_node
    
    else:
      while node.next:
        node = node.next
      
      node.next = new_node

  def search(self, data):
    head = self.head
    node = head

    if node.data == data:
      self.head = node.next
      return head
    
    else:
      while node.next:
        if node.next.data == data:
          deleted_node = node.next
          node.next = deleted_node.next
          return deleted_node

        node = node.next
      raise ValueError("Data not in list")

  def size(self):
    node = self.head
    count = 0
    while node:
        count += 1
        node = node.next
    return count

  def delete(self, data):
    head = self.head
    node = head

    if node.data == data:
      self.head = node.next
      return head
    
    else:
      while node:
        if node.data == data:
          previous = node
          next = node.next
          deleted_node = node
          self.deleteByIndex(previous, next)
          return deleted_node
        node = node.next
      raise ValueError("Data is not in list")

  def deleteByIndex(self, previous, node):
    previous.next = node.next

  def countOccurences(self, data):
    head = self.head
    node = head
    occurences = 0

    while node:
      if node.data == data:
        occurences += 1
      node = node.next
    
    return occurences

  def prettify(self):
  node = self.head
  array = []
  
  while node.next:
    array.append((node.data, node.next.data))
    node = node.next
  array.append((node.data, node.next))
  return array
    