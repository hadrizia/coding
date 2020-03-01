from code.data_structures.stack.stack import Stack
from code.data_structures.linkedlist.node import Node

class SetOfStacks(object):
  def __init__(self, stacks = [], capacity_of_stacks = 0):
    self.stacks = stacks
    self.capacity_of_stacks = capacity_of_stacks
  
  def is_empty(self):
    return len(self.stacks) == 0

  def add_new_stack_to_set(self, value):
    stack = Stack()
    stack.push(value)
    self.stacks.append(stack)

  def push(self, value):
    if self.is_empty():
      self.add_new_stack_to_set(value)
    else:
      last_stack = self.stacks[-1]
      if last_stack.size() < self.capacity_of_stacks:
        last_stack.push(value)
      else:
        self.add_new_stack_to_set(value)

  def pop(self):
    if not self.is_empty():
      last_stack = self.stacks[-1]
      deleted_node = last_stack.pop()
      if last_stack.is_empty():
        self.stacks.remove(last_stack)
      return deleted_node
  
  def pop_at(self, index):
    indexed_stack = self.stacks[index]
    if indexed_stack != None:
      deleted_node = indexed_stack.pop()
      if indexed_stack.size() == self.capacity_of_stacks - 1: 
        for i in range(index, len(self.stacks) - 1):
          self.stacks[i].push(self.stacks[i + 1].remove_bottom())
          if self.stacks[i + 1].is_empty():
            self.stacks.remove(self.stacks[i + 1])
            break


      return deleted_node

def tests():
  set_of_stacks = SetOfStacks(capacity_of_stacks = 2)
  set_of_stacks.push(1)
  set_of_stacks.push(2)
  set_of_stacks.push(3)
  assert len(set_of_stacks.stacks) == 2

  set_of_stacks.pop()
  assert len(set_of_stacks.stacks) == 1

  set_of_stacks.push(3)
  set_of_stacks.push(4)
  set_of_stacks.push(5)
  assert len(set_of_stacks.stacks) == 3
  set_of_stacks.pop_at(0)
  assert len(set_of_stacks.stacks) == 2


if __name__ == "__main__":
  tests()