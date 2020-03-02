from code.data_structures.stack.stack import Stack

def tests():
  stack = Stack()
  stack.push_in_order(4)
  assert stack.prettify() == [4]

  stack.push_in_order(3) 
  assert stack.prettify() == [3, 4]

  stack.push_in_order(1)
  assert stack.prettify() == [1, 3, 4]

  stack.push_in_order(2)
  assert stack.prettify() == [1, 2, 3, 4]


if __name__ == "__main__":
  tests()