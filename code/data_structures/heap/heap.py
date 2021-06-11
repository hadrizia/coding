class Heap(object):
  def __init__(self, heap=[]):
    self.heap = heap

  def heapify(self, i, n):
    biggest = i
    left = i * 2 + 1
    right = i * 2 + 2
    
    if left < n and self.heap[left] > self.heap[i]:
      biggest = left
    
    if right < n and self.heap[right] > self.heap[biggest]:
      biggest = right

    if biggest != i:
      self.heap[biggest], self.heap[i] = self.heap[i], self.heap[biggest]
      self.heapify(biggest, n)

    else:
      return

  def build_heap(self):
    n = len(self.heap)
    for i in range(len(h.heap) // 2 - 1, -1, -1):
      h.heapify(i, n)

  def heapsort(self):
    self.build_heap()
    n = len(self.heap)

    for i in range(n - 1, 0, -1):
      self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
      self.heapify(0, i)

h = Heap([4, 6, 2, 3, 1, 9])
h.build_heap()
h.heapsort()

assert h.heap == [1, 2, 3, 4, 6, 9]

