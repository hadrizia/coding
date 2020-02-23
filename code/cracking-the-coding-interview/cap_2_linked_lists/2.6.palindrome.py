from code.data_structures.linkedlist.singly_linkedlist import LinkedList

def create_inverted_list(node):
  list = LinkedList()
  while node:
    list.insertToHead(node)
    node = node.next
  return list

def is_palindrome(l):
  middle = l.size() / 2
  count = 0
  node = l.head
  inverted_list = LinkedList()

  while node:
    count += 1
    if count == middle:
      inverted_list = create_inverted_list(node)
    node = node.next
  
  node1 = l.head
  node2 = inverted_list.head
  while node1 and node2:
    if node1.data != node2.data:
      return False
    node1 = node1.next
    node2 = node2.next
  
  return True

def is_palindrome_2(l):
  l_size = l.size()
  middle = l_size / 2
  is_odd = True if l_size % 2 != 0 else False
  
  stack = []
  node = l.head
  indice = 0

  while node:
    indice += 1
    if indice < middle:
      stack.append(node.data)
    elif indice == middle and not is_odd:
      stack.append(node.data)
    elif indice > middle:
      if stack[-1] == node.data:
        stack.pop()
    node = node.next
  
  return len(stack) == 0


def tests():
  l1 = LinkedList()
  l1.insert('A')
  l1.insert('N')
  l1.insert('A')

  l2 = LinkedList()
  l2.insert('A')
  l2.insert('N')
  l2.insert('T')
  l2.insert('A')

  assert is_palindrome_2(l1) == True
  assert is_palindrome(l2) == False

if __name__ == "__main__":
  tests()
