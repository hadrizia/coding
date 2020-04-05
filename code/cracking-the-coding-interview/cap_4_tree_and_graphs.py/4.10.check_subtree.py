'''
  Resume: Determine if T2 is a subtree of T1
'''

from code.data_structures.tree.node import Node

def check_subtree(tree1, tree2):
  return True if not tree2 else search_node(tree1, tree2)

def search_node(root1, root2):
  if not root1:
    return False
  
  if root1.value == root2.value and compare_trees(root1, root2):
    return True
  
  return search_node(root1.left, root2) or search_node(root1.right, root2)


def compare_trees(root1, root2):
  if not root1 and not root2:
    return True
  
  if not root1 or not root2 or root1.value != root2.value:
    return False
  
  return compare_trees(root1.left, root2.left) and compare_trees(root1.right, root2.right)


def tests():
  tree1 = Node(
    value=5,
    left=Node(
      value=3),
    right=Node(
      value=8
    )
  )
  tree2 = Node(value = 1)

  assert not check_subtree(tree1, tree2)
  assert check_subtree(tree1, Node(value=3))

if __name__ == "__main__":
  tests()