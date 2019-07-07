from singly_linkedlist import LinkedList

'''
  Given that N = linked_list.size(),
  Time efficiency: O(N)
'''
def removeDups(linked_list):
  if linked_list.size() == 0:
    return -1
  
  node = linked_list.head
  buffer = []
  buffer.append(node)

  while node.next:
    if node.next.data not in buffer:
      buffer.append(node.next.data)
    else:
      linked_list.delete(node.data)    
    node = node.next

  return linked_list

def tests():
  ll = LinkedList()
  ll.insert_tail(4)
  ll.insert_tail(3)
  ll.insert_tail(2)
  ll.insert_tail(5)
  ll.insert_tail(2)
  ll.insert_tail(4)
  assert ll.prettify() == [(4, 3), (3, 2), (2, 5), (5, 2), (2, 4), (4, None)]
  ll = removeDups(ll)
  assert ll.prettify() == [(3, 5), (5, 2), (2, 4), (4, None)]