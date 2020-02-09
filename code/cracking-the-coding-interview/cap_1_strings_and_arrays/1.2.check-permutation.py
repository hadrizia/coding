def countLettersOccurences(string):
  dictionary = {}
  for letter in  string:
    if letter in dictionary:
      dictionary[letter] += 1
    else:
      dictionary[letter] = 1
  return dictionary

'''
  Assuming that N = len(string1) and M = len(string2):
    Time efficiency: O(N + M)
    Memory efficiency: O(N + M)
'''
def checkPermutation(string1, string2):
  dict_string1 = countLettersOccurences(string1)
  dict_string2 = countLettersOccurences(string2)
  return dict_string1 == dict_string2


def tests():
  assert checkPermutation("god", "dog") == True
  assert checkPermutation("god  ", "dog") == False
  assert checkPermutation("God", "dog") == False
  assert checkPermutation("hadri", "hidra") == True
  assert checkPermutation("juma", "umaj") == True
  assert checkPermutation("gOd", "dOg") == True
  assert checkPermutation("hadrizia", "hadrielle") == False
  assert checkPermutation("gOD", "dOG") == False
  assert checkPermutation("gOd", "dOgg") == False

if __name__ == "__main__":
  tests()
  
