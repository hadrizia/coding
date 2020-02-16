from code.data_structures.linkedlist.singly_linkedlist import LinkedList

'''
  Given that N = len(linked_list),
  Time efficiency: O(N^2)
  Memory efficiency: O(1)
'''
def delete_dups(linked_list, data):
  node = linked_list.head
  count = 0

  if node.data == data:
    count += 1

  while node and node.next:
    if node.next.data == data:
      count += 1
      if count > 1:
        node.next = node.next.next
    node = node.next
  
def remove_dups(linked_list):
  node = linked_list.head
  while node:
    delete_dups(linked_list, node.data)
    node = node.next
  
def tests():
  ll = LinkedList()
  ll.insert(4)
  ll.insert(3)
  ll.insert(2)
  ll.insert(5)
  ll.insert(2)
  ll.insert(4)
  assert ll.prettify() == [(4, 3), (3, 2), (2, 5), (5, 2), (2, 4), (4, None)]
  remove_dups(ll)
  assert ll.prettify() == [(4, 3), (3, 2), (2, 5), (5, None)]

if __name__ == "__main__":
  tests()