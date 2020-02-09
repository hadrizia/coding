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

'''
  Assuming that N = len(string)
    Time efficiency: O(N^2)
    Memory efficiency: O(1)
'''
def isUniqueWithoutDataStructure1(string):
  n = len(string)
  for i in range(n - 1):
    for j in range(i + 1, n):
      if string[i] == string[j]:
        return False
  return True

'''
Assuming that N = len(string)
  Time efficiency: O(N * log N + N) = O(N * logN)
  Memory efficiency: O(N)
'''
def isUniqueWithoutDataStructure2(string):
  string_sorted = sorted(string)
  for i in range(len(string_sorted) - 1):
    if string_sorted[i] == string_sorted[i + 1]:
      return False
  return True

def tests():
  assert isUnique('Hadrizia') == False
  assert isUniqueWithoutDataStructure1('HadrizIA') == True
  assert isUniqueWithoutDataStructure2('HadRzi') == True
  assert isUnique('HAdrizIa') == True
  assert isUniqueWithoutDataStructure1('Hadrize') == True
  assert isUniqueWithoutDataStructure2('Gabriely') == True
  assert isUnique('ANA') == False
  assert isUniqueWithoutDataStructure1('IsUnique') == True
  assert isUniqueWithoutDataStructure2('IsUnqe') == True
  assert isUnique('Marie Jul') == True

if __name__ == "__main__":
  tests()