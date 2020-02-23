from code.data_structures.linkedlist.node import Node 

class LinkedList(object):
  def __init__(self, head = None):
    self.head = head

  def insert(self, data):
    new_node = Node(data)
    node = self.head

    if self.size() == 0:
      self.head = new_node
    
    else:
      while node.next:
        node = node.next
      node.next = new_node

  def insertNode(self, new_node):
    node = self.head

    if self.size() == 0:
      self.head = new_node
    
    else:
      while node.next:
        node = node.next
      node.next = new_node

  def insertToHead(self, data):
    new_node = Node(data)

    if self.size() == 0:
      self.head = new_node
    
    else:
      new_node.next = self.head
      self.head = new_node



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
      while node.next:
        if node.next.data == data:
          previous = node
          next = node.next
          deleted_node = node.next
          self.deleteByIndex(previous, next)
          return deleted_node
        node = node.next
      raise ValueError("Data is not in list")

  def deleteByIndex(self, previous, node):
    if node.data == self.head.data:
      self.head = node.next
    else:
      previous.next = node.next 

  # The next functions are related to questions from Cracking the Coding Interview   
  def countOccurences(self, data):
    node = self.head
    occurences = 0

    while node:
      if node.data == data:
        occurences += 1
      node = node.next
    return occurences

  def getKthToLast(self, k):
    node = self.head
    last = 0
    
    # Get the index of last element
    while node.next:
      node = node.next
      last += 1

    # Kth to last
    kth_to_last = last - k

    # Search for kth_to_last
    index = 0
    node = self.head
    while index != kth_to_last and node.next:
      node = node.next
      index += 1

    if index == kth_to_last:
      return node
    raise ValueError("The Kth number does not exists!") 

  def prettify(self):
    node = self.head
    array = []
    
    while node.next:
      array.append((node.data, node.next.data))
      node = node.next
    array.append((node.data, node.next))
    return array

  def tail(self):
    node = self.head
    while node.next:
      node = node.next
    return node