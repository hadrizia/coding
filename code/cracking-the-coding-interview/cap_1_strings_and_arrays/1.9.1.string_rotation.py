def is_substring(s1, s2):
  return True if s1 in s2 else False

'''
  Time efficiency: O(1)
  Memory efficiency: (O(len(string1)))
'''
def string_rotation(str1, str2):
  if len(str1) != len(str2):
    return False

  string = str1 + str1
  return is_substring(str2, string)

def tests():
  assert string_rotation('sapato', 'tosapa') == True
  assert string_rotation('sapato', 'satopa') == False
  assert string_rotation('waterbottle', 'erbottlewat') == True
  assert string_rotation('waterbottle', 'botterlewar') == False

if __name__ == "__main__":
  tests()