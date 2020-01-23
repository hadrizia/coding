from code.data_structures.linkedlist.singly_linkedlist import LinkedList

def sum_rev_list(linked_list1, linked_list2):
  sum_list = LinkedList()
  node1 = linked_list1.head
  node2 = linked_list2.head

  while node1 != None and node2 != None:
  