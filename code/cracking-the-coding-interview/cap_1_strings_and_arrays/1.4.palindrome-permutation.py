'''
  Given that N = len(string):
    Time efficiency: O(2 * n) = O(n)
    Memory efficiency: O(2 * n) = O(n) 
'''
def palindromePermutation(string):
  dictionary = {}
  for letter in string.lower():
    if letter not in dictionary:
      dictionary[letter] = 1
    else:
      dictionary[letter] += 1
  
  center_letter = 0
  for key in dictionary:
    if key != ' ' and dictionary[key] % 2 != 0:
      center_letter += 1
      if center_letter > 1:
        return False
  
  return True


def tests():
  assert palindromePermutation("Taco cat") == True
  assert palindromePermutation("Tact Caa") == True
  assert palindromePermutation("Tact hCoa") == False
  assert palindromePermutation("Hadrizia") == False

if __name__ == "__main__":
  tests()