# Complete the maximumToys function below.
'''
  Time efficiency: O(n * log n + len(prices))
'''
def maximumToys(prices, k):
  count = 0
  if k > 0 and len(prices) > 0:
    prices.sort()
    while k > 0 and len(prices) > 0:
      if k >= prices[0]:
        count += 1
        k -= prices[0]
        prices.remove(prices[0])
      else:
        break
  return count


arr = [1, 12, 5, 111, 200, 1000, 10]
k = 50
print maximumToys(arr, k)