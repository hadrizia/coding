class Listy(object):
  def __init__(self, listy = []):
    self.listy = listy
  
  def element_at(self, i):
    res = self.listy[i]
    return res if res else -1 
  
  def binary_search(self, x):
    if self.element_at(0) == -1:
      return -1

    left = 0
    right = left * 2 + 2
    middle = (right + left) // 2

    while self.element_at(right) != -1:
      if self.listy[right] <= x:
        left = right
        right *= 2

      else:
        break

    while left <= right:
      middle = (right + left) // 2
      if self.element_at(middle) != -1:
        if self.listy[middle] == x:
          return middle

        elif self.listy[middle] > x:
          right = middle - 1

        else:
          left = middle + 1
      else:
        return -1
        
      
l = Listy([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(l.binary_search(9))