from code.data_structures.linkedlist.singly_linkedlist import LinkedList

'''
  Given that N = linked_list.size(),
  Time efficiency: O(N)
'''
def removeDups(linked_list):
  node = linked_list.head
  buffer = []
  buffer.append(node)

  while node:
    if node.data not in buffer:
      buffer.append(node.data)
    else:
      linked_list.delete(node.data)
    node = node.next

  return linked_list

def removeDupsWithoutBuffer(linked_list):
  node = linked_list.head

  if(linked_list.countOccurences(node.data) > 1):
    linked_list.deleteByIndex(None, node)
  
  while node.next:
    count = linked_list.countOccurences(node.next.data)    
    if count > 1:
      linked_list.deleteByIndex(node, node.next)
    node = node.next

  return linked_list

c