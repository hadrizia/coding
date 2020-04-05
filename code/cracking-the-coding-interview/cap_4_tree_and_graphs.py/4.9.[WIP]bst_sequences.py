'''
  Resume: Given a bst with distinct elements, 
    print all possible arrays that couldhave led to this tree.
'''
from code.data_structures.tree.node import Node
from code.data_structures.linkedlist.singly_linkedlist import LinkedList

def combine_lists(first, second, results, prefix):
  if not first.size() or not second.size():
    result = prefix.copy()
    result.addAll(first)
    result.addAll(second)
    results.append(result)
    return
  
  h_first = first.deleteHead()
  prefix.insert(h_first.data.value)
  combine_lists(first, second, results, prefix)
  prefix.delete(h_first.data.value)
  first.insertToHead(h_first)

  h_second = second.deleteHead()
  prefix.insert(h_second.data.value)
  combine_lists(first, second, results, prefix)
  prefix.delete(h_second.data.value)
  second.insertToHead(h_second)

def bst_sequences(root):
  results = []
  if not root:
    return results
  
  prefix = LinkedList()
  prefix.insert(root.value)

  left_sequence = bst_sequences(root.left)
  right_sequence = bst_sequences(root.right)

  for left in left_sequence:
    for right in right_sequence:
      res = []
      combine_lists(left, right, res, prefix)
      results.extend(res)
  return results


def tests():
  root = Node(
    value=2,
    left=Node(
      value=1
    ),
    right=Node(
      value=3
    )
  )

  print(bst_sequences(root))
  

if __name__ == "__main__":
  tests()


