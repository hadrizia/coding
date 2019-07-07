'''
  Given that:
    N = len(string),
  Time efficiency: O(n)
  Memory efficiency: O(n)
'''
def stringCompression(string):
  occurrences = 0
  compressedString = ''
  for i in xrange(len(string)):
    occurrences += 1
    if (i + 1 >= len(string)) or string[i] != string[i + 1]:
      compressedString += string[i] + str(occurrences)
      occurrences = 0

  return compressedString if len(compressedString) < len(string) else string


def tests():
  assert stringCompression('aaaabbbbcccc') == 'a4b4c4'
  assert stringCompression('abcde') == 'abcde'
  assert stringCompression('aaaabbbbccccAA') == 'a4b4c4A2'