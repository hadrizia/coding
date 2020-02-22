from code.data_structures.linkedlist.singly_linkedlist import LinkedList
from code.data_structures.linkedlist.node import Node

def fill(list, diff):
  for _ in range(abs(diff)):
    list.insertToHead(0)

def cal_sum_list(node1, node2, node_res):
  if not node1 or not node2:
    return 0
  else:
    node_res.next = Node()
    res = node1.data + node2.data + cal_sum_list(node1.next, node2.next, node_res.next)
    node_res.data = res % 10
    return int(res / 10)

def sum_lists(list1, list2):
  size_list1 = list1.size()
  size_list2 = list2.size()
  diff = size_list1 - size_list2

  if diff > 0:
    fill(list2, diff)

  elif diff < 0:
    fill(list1, diff)
  
  list1.insertToHead(0)
  list2.insertToHead(0)
  
  result = LinkedList()
  result.insert(0)

  node1 = list1.head
  node2 = list2.head
  node_res = result.head
  
  cal_sum_list(node1, node2, node_res)

  if result.head.data == 0:
    result.head = result.head.next

  return result

def tests():
  l1 = LinkedList()
  l1.insert(6)
  l1.insert(1)
  l1.insert(7)

  l2 = LinkedList()
  l2.insert(2)
  l2.insert(9)
  l2.insert(5)

  l3 = sum_lists(l1, l2)
  print(l3.prettify())

if __name__ == "__main__":
  tests()
