def awaysOfInsertionOrRemove(string1, string2):
  away = 0
  i = 0
  j = 0
  while i <= len(string1) - 1 and j <= len(string2) - 1 and away <= 1:
    if string1[i] == string2[j]:
      j += 1
    else:
      away += 1
    i += 1
  return away

def awaysOfReplace(string1, string2):
  away = 0
  for i in xrange(len(string1)):
    if string1[i] != string2[i]:
      away += 1

    if away > 1:
      break
  return away
    
'''
  Assuming that M = min(len(string1), len(string2)):
    Time efficiecy: O(M)
    Memory efficiecy: O(M)
'''
def checkAway(string1, string2):
  away = 0
  len_string1 = len(string1)
  len_string2 = len(string2)

  if len_string1 - len_string2 == 1:
    away = awaysOfInsertionOrRemove(string1, string2)
  
  elif len_string2 - len_string1 == 1:  
    away = awaysOfInsertionOrRemove(string2, string1)
  
  elif len_string1 == len_string2:
    away = awaysOfReplace(string1, string2)
  
  else:
    return False

  if away <= 1:
    return True

  return False

def tests():
  assert checkAway('pale', 'ple') == True
  assert checkAway('pale', 'pales') == True
  assert checkAway('pale', 'bale') == True
  assert checkAway('pale', 'bake') == False

tests()