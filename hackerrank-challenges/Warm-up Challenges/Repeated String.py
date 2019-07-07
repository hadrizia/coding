def countOccurrencesOfA(s):
  count = 0
  for letter in s:
    if letter == 'a':
      count += 1
  return count

# Complete the repeatedString function below.
'''
  Time efficiency: O(1)
'''
def repeatedString(s, n):
  count = 0
  if n > 0:
    count = countOccurrencesOfA(s)
    fullTimes = n / len(s)
    remainderTimes = n % len(s)
    count = count * fullTimes + countOccurrencesOfA (s[:remainderTimes])
  return count

s = "aba"
n = 10
print repeatedString(s, n)