def getMedianIndex(d):
  if d % 2 == 0:
    median_index = ((d - 1/ 2) + (d / 2)) / 2.0 
  else:
    median_index = d / 2
  return median_index


def calculateMedian(arr, start, end, median_index):
  sorted_array = sorted(arr[start:end])
  return sorted_array[median_index]

'''
  Time efficiency: O(d * (n * log n))
'''
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
  notifications = 0
  median_index = getMedianIndex(d)
  if len(expenditure) > 0 and d > 0 and d < len(expenditure):
    for i in xrange(len(expenditure) - d):
      median = calculateMedian(expenditure, i, i + d, median_index)
      if expenditure[i + d] >= 2 * median:
        notifications += 1
  return notifications


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
#expenditure = [1, 2, 3, 4, 4]
d = 5
#d = 4

print activityNotifications(expenditure, d)
