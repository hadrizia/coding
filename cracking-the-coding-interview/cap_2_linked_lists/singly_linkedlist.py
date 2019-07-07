from node import Node 

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
      set_head(node.next)
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
          deleted_node = node.next
          node.next = deleted_node.next
          return deleted_node
        node = node.next
      raise ValueError("Data not in list")
  
  def prettify(self):
    node = self.head
    array = []
    
    while node.next:
      array.append((node.data, node.next.data))
      node = node.next
    array.append((node.data, node.next))
    return array
  
  def insert_ordered(self, data):
    new_node = Node(data)
    node = self.head

    if self.size() == 0:
      self.head = new_node
    
    elif node.data > new_node.data:
      new_node.next = node
      self.head = new_node
    
    else:
      while node.next and node.next.data <= new_node.data:
        node = node.next

      if node.next and node.next.data > new_node.data:
        new_node.next = node.next
        node.next = new_node

      else:
        node.next = new_node
