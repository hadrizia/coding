from code.data_structures.tree.node import Node

def check_balanced(root, is_balanced = True):
  if not root:
    return (0, True)
    
  if not is_balanced:
    return(0, is_balanced)

  left = check_balanced(root.left)
  right = check_balanced(root.right)

  diff = left[0] - right[0]
  is_balanced = left[1] and right[1]

  if(abs(diff) > 1):
    is_balanced = False
    
  return (1 + max(left[0], right[0]), is_balanced)

def tests():
  root = Node(
    value=5,
    left=Node(
      value=3,
      left=Node(
        value=2,
        left=Node(
          value=1)),
      right=Node(4)),
    right=Node(
      value=8, 
      left=Node(
        value=7, 
        left=Node(6)), 
        right=Node(9)
        )
  )

  root2 = Node(
    value=5,
    right=Node(
      value=8, 
      left=Node(
        value=7, 
        left=Node(6)), 
        right=Node(9)
        )
  )

  assert check_balanced(root)[1] == True
  assert check_balanced(root2)[1] == False

if __name__ == "__main__":
  tests()
