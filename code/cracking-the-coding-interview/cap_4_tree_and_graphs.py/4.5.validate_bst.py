from code.data_structures.tree.node import Node

def validate_bst(root):
  return check_bst(root, None, None)

def check_bst(root, min, max):
  if not root:
    return True

  if min and root.value <= min or max and root.value > max:
    return False
  
  if not check_bst(root.left, min, root.value) or not check_bst(root.right, root.value, max):
    return False
  
  return True  

def tests():
  root = Node(
  value=5,
  right=Node(
    value=8, 
    left=Node(
      value=7, 
      left=Node(6)), 
    right=Node(9)
    ),
    left=Node(
      value=6
    )
  )

  root2 = Node(
    value=5,
    left=Node(
      value=3),
    right=Node(
      value=8
    )
  )

  assert validate_bst(root) == False
  assert validate_bst(root2) == True
  
if __name__ == "__main__":
  tests()