class NodeWithParent(object):
  def __init__(self, value = None, left = None, right = None, parent = None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

def get_left_most_node(node):
  if not node:
    return None
  while node.left:
    node = node.left
  return node

def sucessor(root):
  if root.right:
    return get_left_most_node(root.right)

  node = root
  parent = node.parent
  while parent and parent.left != node:
    node = parent
    parent = parent.parent

  return parent

def tests():
  #  Creating the nodes
  root = NodeWithParent(
    value=5
  )

  node_3 = NodeWithParent(
    value = 3
  )

  node_2 = NodeWithParent(
    value = 2
  )

  node_6 = NodeWithParent(
    value = 6
  )

  node_7 = NodeWithParent(
    value = 7
  )

  node_8 = NodeWithParent(
    value = 8
  )

  node_9 = NodeWithParent(
    value = 9
  )

  # Setting the relations
  root.left = node_3
  root.right = node_8
  node_3.parent = root
  node_8.parent = root

  node_3.left = node_2
  node_2.parent = node_3

  node_8.left = node_7
  node_8.right = node_9
  node_7.parent = node_8
  node_9.parent = node_8

  node_7.left = node_6
  node_6.parent = node_7

  # Testing the sucessor
  assert sucessor(node_3) == root
  assert sucessor(root) == node_6
  assert sucessor(node_8) == node_9
  assert sucessor(node_9) == None  

if __name__ == "__main__":
  tests()
