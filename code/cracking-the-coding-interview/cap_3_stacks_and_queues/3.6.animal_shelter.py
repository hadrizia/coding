from code.data_structures.linkedlist.singly_linkedlist import LinkedList

class AnimalShelter(object):
  def __init__(self, cats_queue = LinkedList(), dogs_queue = LinkedList(), last_order = 0):
    self.cats_queue = cats_queue
    self.dogs_queue = dogs_queue
    self.last_order = last_order

  def oldest_cat(self):
    return self.cats_queue.head
  
  def oldest_dog(self):
    return self.dogs_queue.head

  def enqueue(self, animal):
    self.last_order += 1
    if animal == 'cat':
      self.cats_queue.insert(self.last_order)
    else:
      self.dogs_queue.insert(self.last_order)

  def dequeue_cat(self):
    return self.cats_queue.deleteHead()

  def dequeue_dog(self):
    return self.dogs_queue.deleteHead()

  def dequeue_any(self):
    if self.cats_queue.is_empty():
      return self.dequeue_dog()

    elif self.dogs_queue.is_empty():
      return self.dequeue_cat()
    
    else:
      if self.oldest_dog().data < self.oldest_cat().data:
        return self.dequeue_dog()

      else:
        return self.dequeue_cat()


def tests():

  animal_shelter = AnimalShelter()
  animal_shelter.enqueue('dog')
  animal_shelter.enqueue('cat')
  animal_shelter.enqueue('dog')
  animal_shelter.enqueue('cat')
  animal_shelter.enqueue('cat')
  animal_shelter.enqueue('cat')
  animal_shelter.enqueue('dog')

  assert animal_shelter.cats_queue.size() == 4
  assert animal_shelter.dogs_queue.size() == 3

  assert animal_shelter.oldest_cat().data == 2
  animal_shelter.dequeue_cat()
  assert animal_shelter.oldest_cat().data == 4

  assert animal_shelter.oldest_dog().data == 1
  animal_shelter.dequeue_dog()
  assert animal_shelter.oldest_dog().data == 3

  assert animal_shelter.dequeue_any().data == 3



if __name__ == "__main__":
  tests()