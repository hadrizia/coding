def isSubstring(str1, str2):
  if str2 in str1:
    return True
  return False

'''
  Time efficiency: O(len(string2))
  Memory efficiency: (O(1)))
'''
def stringRotation(str1, str2):
  if len(str1) != len(str2):
    return False

  for i in xrange(len(str2)):
    if isSubstring(str1, str2[i:]) and isSubstring(str1, str2[:i]):
      return True
  return False

def tests():
  assert stringRotation('sapato', 'tosapa') == True
  assert stringRotation('sapato', 'satopa') == False
  assert stringRotation('waterbottle', 'erbottlewat') == True
  assert stringRotation('waterbottle', 'botterlewar') == False

if __name__ == "__main__":
  tests()