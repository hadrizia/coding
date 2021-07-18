class Node(object):
  def __init__(self, data=None):
    self.right = None
    self.left = None
    self.data = data
    self.left_length = 0

def insert(root, x):
  if not root:
    return Node(x)

  if x <= root.data:
    root.left = insert(root.left, x)
    root.left_length += 1

  else:
    root.right = insert(root.right, x)
  return root

def getRankOf(root, x):
  if root.data == x:
    return root.left_length
  
  if root.data > x:
    if root.left:
      return getRankOf(root.left, x)
    else:
      return -1
  else:
    if not root.right:
      return -1
    
    right_rank = getRankOf(root.right, x)
    if right_rank == -1:
      return -1
    else:
      return root.left_length + 1 + right_rank

def track(arr):
  root = None
  for elem in arr:
    root = insert(root, elem)
  return root


arr  = [5, 1, 4, 4, 5, 9, 7, 13, 3]
root = track(arr)
assert getRankOf(root, 1) == 0
assert getRankOf(root, 3) == 1
assert getRankOf(root, 4) == 3
assert getRankOf(root, 7) == 6
