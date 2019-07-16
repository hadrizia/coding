from code.data_structures.linkedlist.singly_linkedlist import LinkedList
'''
  Given that N = len(linkedlist) and k = a random index:
    N for get the index of last element + N for search the (index_last_element - k)th node
    O(2 * N) = O(N)
'''
def returnKthToLast(linkedlist, k):
  kth_to_last = linkedlist
  return kth_to_last.getKthToLast(k)

def tests():
  ll = LinkedList()
  ll.insert(4)
  ll.insert(3)
  ll.insert(2)
  ll.insert(5)
  ll.insert(2)
  ll.insert(4)
  assert ll.prettify() == [(4, 3), (3, 2), (2, 5), (5, 2), (2, 4), (4, None)]
  assert returnKthToLast(ll, 0).data == 4
  assert returnKthToLast(ll, 2).data == 5
  assert returnKthToLast(ll, 5).data == 4

if __name__ == "__main__":
  tests()

