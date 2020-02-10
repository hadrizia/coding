'''
  Assuming that M = min(len(string1), len(string2)):
    Time efficiecy: O(M)
    Memory efficiecy: O(M)
'''
def check_away(string1, string2):
  away = 0
  len_string1 = len(string1)
  len_string2 = len(string2)

  if len_string1 - len_string2 == 0:
    away = 0
    minor = string1
    major = string2
  
  elif len_string1 - len_string2 > 0:  
    away = 1
    minor = string2
    major = string1
  
  else:
    away = 1
    minor = string1
    major = string2
  
  for letter in minor:
    if letter not in major:
      away += 1
      if away > 1:
        return False

  return True

def tests():
  assert check_away('pale', 'ple') == True
  assert check_away('pale', 'pales') == True
  assert check_away('pale', 'bale') == True
  assert check_away('pale', 'bake') == False

if __name__ == "__main__":
  tests()