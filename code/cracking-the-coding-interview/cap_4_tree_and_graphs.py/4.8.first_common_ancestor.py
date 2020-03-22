'''
  Resume: Find the first common ancestor of two nodes in a binary tree.
'''

from collections import namedtuple
from code.data_structures.tree.node import Node

Ancestor = namedtuple('Ancestor', ['node', 'is_ancestor'])

def common_ancestor(root, node1, node2):
  if not root:
    return Ancestor(None, False)
  
  if root == node1 and root == node2:
    return Ancestor(root, True)

  left_search = common_ancestor(root.left, node1, node2)
  if left_search.is_ancestor: # Ancestor is in the left subtree
    return left_search
  
  right_search = common_ancestor(root.right, node1, node2)
  if right_search.is_ancestor: # Ancestor is in the right subtree
    return right_search
  
  if left_search.node and right_search.node: # Found the ancestor in both subtrees -> return the parent node
    return Ancestor(root, True)
  
  elif root == node1 or root == node2:
    is_founded = True if left_search.node or right_search else False
    return Ancestor(root, False)
  
  else:
    node = left_search.node if left_search.node else right_search.node
    return Ancestor(node, False)


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

  node1 = root.left.left.left
  node3 = root.left
  node8 = root.right

  assert common_ancestor(root, root, node3).node.value == 5
  assert common_ancestor(root, node1, node8).node.value == 5
  assert common_ancestor(root, node1, node3).node.value == 3

if __name__ == '__main__':
  tests()