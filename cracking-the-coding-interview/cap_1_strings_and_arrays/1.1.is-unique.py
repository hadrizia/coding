'''
  Assuming that N = len(string)
    Time efficiency: O(N)
    Memory efficiency: O(N)
'''
def isUnique(string):
  dictionary = {}
  for letter in string:
    if letter not in dictionary:
      dictionary[letter] = 1
    else:
      return False
  return True


def tests():
  assert isUnique('Hadrizia') == False
  assert isUnique('HadrizIA') == True
  assert isUnique('HadRzi') == True
  assert isUnique('HAdrizIa') == True
  assert isUnique('Hadrize') == True
  assert isUnique('Gabriely') == True
  assert isUnique('ANA') == False
  assert isUnique('IsUnique') == True
  assert isUnique('IsUnqe') == True
  assert isUnique('Marie Jul') == True

tests()

