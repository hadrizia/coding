from code.data_structures.linkedlist.singly_linkedlist import LinkedList
from code.data_structures.linkedlist.node import Node

def sum_with_one_list(node, node_res):
  while node:
    res = node.data + node_res.data
    carry_in = res % 10
    carry_out = int(res / 10)
    node_res.data = carry_in
    new_node = Node(carry_out)
    node_res.next = new_node
    node = node.next

def remove_last_zero(head):
  node = head
  while node.next:
    if node.next.data == 0 and not node.next.next:
      node.next = node.next.next
    else:
      node = node.next
  return head


def sum_lists(head1, head2):
  node1 = head1
  node2 = head2

  result = LinkedList()
  result.insert(0)
  node_res = result.head

  while node1 and node2 and node_res:
    res = node1.data + node2.data + node_res.data
    carry_in = res % 10
    carry_out = int(res / 10)
    node_res.data = carry_in
    new_node = Node(carry_out)
    node_res.next = new_node
    node1 = node1.next
    node2 = node2.next
    node_res = node_res.next

  if node1:
    sum_with_one_list(node1, node_res)
  
  elif node2:
    sum_with_one_list(node2, node_res)

  return remove_last_zero(result.head)

def tests():
  l1 = LinkedList()
  l1.insert(7)
  l1.insert(1)
  l1.insert(6)

  l2 = LinkedList()
  l2.insert(5)
  l2.insert(9)
  l2.insert(2)

  l3 = LinkedList()
  l3.head = sum_lists(l1.head, l2.head)
  assert l3.prettify() == [(2, 1), (1, 9), (9, None)]

if __name__ == "__main__":
  tests()
