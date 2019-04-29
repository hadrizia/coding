def stringToDict(string):
  dict = {}
  
  for letter in string:
    dict[letter] = 1

  return dict


def checkSubstring(maxS, minS):
  ans = 'NO'
  hash_aux = stringToDict(minS)

  for letter in maxS:
    if letter in hash_aux:
      ans = 'YES'
      break

  return ans


'''
  Given that
    m = min(len(s1), len(s2))
    
  Time efficiency: O(len(s1) + len(s2) + m)
'''
def twoStrings(s1, s2):
 
  if len(s1) > len(s2):
    return checkSubstring(s1, s2)
  
  else:
    return checkSubstring(s2, s1)


s1 = "hi"
s2 = "world"

twoStrings(s1, s2)