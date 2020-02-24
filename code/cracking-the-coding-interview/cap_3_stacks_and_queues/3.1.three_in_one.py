class StackInArray(object):

  def __init__(self, array, number_of_stacks = 3):
    self.array = array
    self.number_of_stacks = number_of_stacks
    self.stacks_size = int(len(self.array) / self.number_of_stacks)
  
  def push(self, stack_num, data):
    if not self.is_full(stack_num):
      last_index_stack = stack_num * self.stacks_size - 1
      index_top = self.index_of_top(stack_num)
      if self.size(stack_num) > 0:
        for i in range(last_index_stack, index_top, -1):
          self.array[i] = self.array[i - 1]
      self.array[self.index_of_top(stack_num)] = data
  
  def pop(self, stack_num):
    if not self.is_empty(stack_num):
      deleted_value = self.array[self.index_of_top(stack_num)]
      index = self.index_of_top(stack_num)
      size = self.size(stack_num)
      for i in range(index, index + size):
        self.array[i] = self.array[i + 1]
      return deleted_value      
  
  def index_of_top(self, stack_num):
    last_index_stack = stack_num * self.stacks_size
    first_index_stack = last_index_stack - self.stacks_size
    return first_index_stack

  def top(self, stack_num):
    return self.array[self.index_of_top(stack_num)]

  def is_empty(self, stack_num):
    return self.array[self.index_of_top(stack_num)] == None

  def is_full(self, stack_num):
    last_index_stack = stack_num * self.stacks_size - 1
    return self.array[last_index_stack] != None
  
  def size(self, stack_num):
    index_top = self.index_of_top(stack_num)
    end_index = index_top + self.number_of_stacks
    size = 0
    i = index_top
    while self.array[i] != None and i < end_index:
      i += 1
      size += 1
    return size


def tests():
  array = [None for _ in range(15)]
  
  stacks_in_array = StackInArray(array, 3)

  assert stacks_in_array.is_empty(1) == True
  assert stacks_in_array.is_empty(2) == True
  assert stacks_in_array.is_empty(3) == True
  
  stacks_in_array.push(1, 1)
  stacks_in_array.push(2, 1)
  stacks_in_array.push(3, 1)
  assert stacks_in_array.top(1) == 1
  assert stacks_in_array.top(2) == 1
  assert stacks_in_array.top(3) == 1
  assert stacks_in_array.index_of_top(1) == 0
  assert stacks_in_array.index_of_top(2) == 5
  assert stacks_in_array.index_of_top(3) == 10

  stacks_in_array.push(1, 2)
  stacks_in_array.push(2, 5)
  stacks_in_array.push(3, 2)

  assert stacks_in_array.top(1) == 2
  assert stacks_in_array.top(2) == 5
  assert stacks_in_array.top(3) == 2


  stacks_in_array.push(1, 3)
  
  assert stacks_in_array.pop(1) == 3
  assert stacks_in_array.pop(2) == 5

  assert stacks_in_array.top(1) == 2
  assert stacks_in_array.top(2) == 1

if __name__ == "__main__":
  tests()
