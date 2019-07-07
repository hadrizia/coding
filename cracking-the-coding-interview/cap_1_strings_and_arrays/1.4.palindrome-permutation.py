'''
  Given that N = len(string):
    Time efficiency: O(2 * n) = O(n)
    Memory efficiency: O(2 * n) = O(n) 
'''
def palindromePermutation(string):
  string = string.lower().replace(' ', '')
  dictionary = {}
  for letter in string:
    if letter in dictionary:
      dictionary[letter] = dictionary[letter] + 1
  
    else:
      dictionary[letter] = 1
  
  center_letter = 0
  for count in dictionary:
    if count == 1:
      center_letter += 1
  
  return center_letter <= 1


def tests():
  assert palindromePermutation("Taco cat") == True
  assert palindromePermutation("Tact Coa") == True
  assert palindromePermutation("Tact hCoa") == False
  assert palindromePermutation("Hadrizia") == False