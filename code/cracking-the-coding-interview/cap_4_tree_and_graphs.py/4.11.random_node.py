import random

class TreeNode(object):
  def __init__(self, value='', left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    self.size = 1

  def insert_in_order(self, value):

    if value < self.value:
      if not self.left:
        self.left = TreeNode(value=value)
      else:
        self.left.insert_in_order(value)
    
    else:
      if not self.right:
        self.right = TreeNode(value=value)
      
      else:
        self.right.insert_in_order(value)
  
    self.size += 1


  def get_random_node(self, index = None):
    if not self:
      return
    
    if not index:
      index = random.randint(1, self.size)

    left_size = self.left.size if self.left else 0

    if index == left_size:
      return self
    
    elif index < left_size:
      return self.left.get_random_node(index=index)
    
    elif self.right:
      return self.right.get_random_node(index=index - (left_size + 1))


  def find(self, value):
    if not self:
      return 

    if value == self.value:
      return self

    elif value < self.value:
      return self.left.find(value)
    
    else: 
      return self.right.find(value)

     
def tests():
  root = TreeNode(5)
  root.insert_in_order(3)
  root.insert_in_order(2)
  root.insert_in_order(7)
  root.insert_in_order(6)

  arr = [5, 3, 2, 7, 6]
  assert root.get_random_node().value in arr

if __name__ == "__main__":
  tests()