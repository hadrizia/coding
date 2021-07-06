"""
  What is an anagram?
    When we have two or more words that have the same numbers of each letter so one can be
    made just by arranging the letters of other.

  - Brute force solution:
    - Sort each string so we can have the anagrams together
      - this is bad cause we want to keep the original string
      - we can store in a hashmap!
"""

from collections import defaultdict

def sort_string(hashmap, string):
  sorted_string = ''.join(sorted(string))
  hashmap[sorted_string].append(string)

def group_anagrams(strings):
  hashmap = defaultdict(list)
  for string in strings:
    sort_string(hashmap, string)

  result = []
  for _, value in hashmap.items():
    result.extend(value)
  
  return result

def tests():
  assert group_anagrams(['cat', 'dog', 'book', 'god', 'tac']) == ['cat', 'tac', 'dog', 'god', 'book']

tests()