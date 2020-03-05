from code.data_structures.tree.node import Node

def in_order_traversal(arr, root):
  if root.value != None:
    in_order_traversal(arr, root.left)
    arr.append(root.value)
    in_order_traversal(arr, root.right)
    return arr

def pre_order_traversal(arr, root):
  if root.value != None:
    arr.append(root.value)
    in_order_traversal(arr, root.left)
    in_order_traversal(arr, root.right)
    return arr

def post_order_traversal(arr, root):
  if root.value != None:
    in_order_traversal(arr, root.left)
    in_order_traversal(arr, root.right)
    arr.append(root.value)
    return arr

def minimal_tree(arr):
  if len(arr) == 0:
    return Node()  
  middle = int(len(arr) / 2)

  node = Node(arr[middle])
  node.left = minimal_tree(arr[:middle])
  node.right = minimal_tree(arr[middle + 1:])
  return node

def tests():
  array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  root = minimal_tree(array)

  in_order = in_order_traversal([], root)
  pre_order = pre_order_traversal([], root)
  post_order = post_order_traversal([], root)

  assert in_order == [1, 2, 3, 4, 5, 6, 7, 8, 9]
  assert pre_order == [5, 1, 2, 3, 4, 6, 7, 8, 9]
  assert post_order == [1, 2, 3, 4, 6, 7, 8, 9, 5]

if __name__ == "__main__":
  tests()