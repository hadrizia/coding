from code.data_structures.linkedlist.singly_linkedlist import LinkedList
from code.data_structures.linkedlist.node import Node

def point_forward(node, diff):
  i = -1
  while node:
    i += 1
    if i == diff:
      return node
    node = node.next

def intersection(l1, l2):
  intersec = Node()
  if l1.tail().data != l2.tail().data:
    return intersec
  
  node1 = l1.head
  node2 = l2.head

  diff = l1.size() - l2.size()

  if diff > 0:
    node1 = point_forward(node1, diff)
  elif diff < 0:
    node2 = point_forward(node2, abs(diff))

  while node1 and node2:
    if node1.data == node2.data:
      return node1
    node1 = node1.next
    node2 = node2.next
  return intersec

def tests():
  l1 = LinkedList()
  l1.insert(2)
  l1.insert(3)
  l1.insert(4)
  l1.insert(5)
  l1.insert(7)

  l2 = LinkedList()
  l2.insert(5)
  l2.insert(6)
  l2.insert(7)
  l2.insert(4)
  l2.insert(5)
  l2.insert(7)

  assert intersection(l1, l2).data == 4

if __name__ == "__main__":
  tests()
