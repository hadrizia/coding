def search_in_rotated_array(arr, k):
  return search(arr, k, 0, len(arr) - 1)

def search(arr, k, l, r):
  if l > r:
    return -1

  mid = (l + r) // 2
  if arr[mid] == k: # Found!
    return mid
  
  else:
    if arr[l] < arr[mid]: # Normally ordered, just do the regular binary search
      if arr[mid] > k and arr[l] <= k: # Check if should search in left side
        return search(arr, k, l, mid - 1)
      else:
        return search(arr, k, mid + 1, r)

    elif arr[l] > arr[mid]: # Was rotated, do the inverse binary search
      if arr[mid] < k and arr[r] >= k: # Check if should search in right side
        return search(arr, k, mid + 1, r)
      else:
        return search(arr, k, l, mid - 1)

    else: 
      if arr[mid] != arr[r]: # All left side is the same, search in the right side
        return search(arr, k, mid + 1, r)
    
      else: # We need to check in both sides
        res = search(arr, k, mid + 1, r) # Search in left side
        if  res == -1: # Search in right side
          return search(arr, k, mid + 1, r)
        else:
          return res

def tests():
  arr1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
  arr2 = [3, 4, 2, 2, 2]
  arr3 = [2, 3, 4, 2, 2, 2]
  
  assert search_in_rotated_array(arr1, 5) == 8
  assert search_in_rotated_array(arr2, 4) == 1
  assert search_in_rotated_array(arr3, 4) == 2

if __name__== "__main__":
  tests()