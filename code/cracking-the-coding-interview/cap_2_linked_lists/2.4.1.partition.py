from code.data_structures.linkedlist.singly_linkedlist import LinkedList

def partition(ll, p):
  head = ll.head
  node = head
  tail = head
  
  while node:
    next_node = node.next
    if node.data < p:
      node.next = head
      head = node
    else:
      tail.next = node
      tail = node
    node = next_node
  tail.next = node
  return head

def tests():
  ll = LinkedList()
  ll.insert(3)
  ll.insert(5)
  ll.insert(8)
  ll.insert(5)
  ll.insert(10)
  ll.insert(2)
  ll.insert(1)
  ll.head = partition(ll, 5) 
  assert ll.prettify() == [(1, 2), (2, 3), (3, 5), (5, 8), (8, 5), (5, 10), (10, None)]

if __name__ == "__main__":
  tests()