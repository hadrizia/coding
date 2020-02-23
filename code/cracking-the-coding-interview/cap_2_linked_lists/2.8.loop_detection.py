from code.data_structures.linkedlist.singly_linkedlist import LinkedList
from code.data_structures.linkedlist.node import Node

def loop_detection(l):
  fast = l.head
  slow = l.head

  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

    if slow == fast:
      break
  
  if fast and fast.next:
    slow = l.head
    while slow != fast:
      fast = fast.next
      slow = slow.next 
    return fast
                                                                                                                                                      
  else:
    return Node()

def tests():
  l1 = LinkedList()
  l1.insert('A')
  l1.insert('B')
  l1.insert('C')
  l1.insert('D')
  l1.insertNode(Node('E', l1.head.next.next))

  assert loop_detection(l1).data == 'C'


if __name__ == "__main__":
  tests()