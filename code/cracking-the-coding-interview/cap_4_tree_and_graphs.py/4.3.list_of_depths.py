from code.data_structures.tree.node import Node
from code.data_structures.linkedlist.singly_linkedlist import LinkedList

def list_of_depths(root):
  array = []
  linked_list = LinkedList()
  if root.value:
    linked_list.insert(root) # Visiting the root

  while linked_list.size() > 0:
    array.append(linked_list) # Adding the level to the array of linkedLists
    parents = linked_list # Storing the previous level 
    linked_list = LinkedList() # Reseting the linkedList of current level
    parent = parents.head
    while parent:
      p = parent.data
      if p.left and p.left.value:
        linked_list.insert(p.left) 
      
      if p.right and p.right.value:
        linked_list.insert(p.right)
      parent = parent.next

  return array

def tests():
  root = Node(
    value=5,
    left=Node(
      value=3,
      left=Node(
        value=2,
        left=Node(1)),
      right=Node(4)),
    right=Node(
      value=8, 
      left=Node(
        value=7, 
        left=Node(6)), 
        right=Node(9)
        )
  )

  arr = list_of_depths(root)
  assert len(arr) == 4

if __name__ == "__main__":
  tests()
