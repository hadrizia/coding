'''
  Assuming that S is the aditional space required to replace a space by '%20' and N is the number of spaces in string[:real_len]:
    Time efficiency: O(2 * real_len) = O(real_len)
    Memory efficiency: O(real_len + S * N)
'''
def urlify(string, real_len):
  string = string[:real_len]
  # Constant that represents the aditional space required to replace a space by '%20'
  ADITIONAL_SPACE = 2
  for i in xrange(real_len):
    if string[i] == ' ':
      real_len = real_len + ADITIONAL_SPACE

  for i in xrange(real_len):
    if string[i] == ' ':
      string = string[:i] + '%20' + string[i+1:]
  return string

def tests():
  assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
  assert urlify("Mr John Smith    ", 14) == "Mr%20John%20Smith%20"
  assert urlify("MrJohnSmith", 11) == "MrJohnSmith"

tests()