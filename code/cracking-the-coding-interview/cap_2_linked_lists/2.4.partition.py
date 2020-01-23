from code.data_structures.linkedlist.singly_linkedlist import LinkedList

def partition(linkedlist, partition):
  partitioned_linked_list = LinkedList()
  node = linkedlist.head

  while node != None:
    if node.data < partition:
      partitioned_linked_list.insertToHead(node.data)
    else:
      partitioned_linked_list.insert(node.data)
  
    node = node.next

  
  return partitioned_linked_list

def tests():
  linked_list = LinkedList()
  linked_list.insert(3)
  linked_list.insert(5)
  linked_list.insert(8)
  linked_list.insert(5)
  linked_list.insert(10)
  linked_list.insert(2)
  linked_list.insert(1)

  expected_output = LinkedList()
  expected_output.insert(1)
  expected_output.insert(2)
  expected_output.insert(3)
  expected_output.insert(5)
  expected_output.insert(8)
  expected_output.insert(5)
  expected_output.insert(10)

  assert expected_output.prettify() == partition(linked_list, 5).prettify()

if __name__ == "__main__":
  tests()  

