def addWordsToDict(arr):
  availableDict = {}
  for word in arr:
  
    if word not in availableDict:
      availableDict[word] = 1

    else:
      availableDict[word] = availableDict[word] + 1
  
  return availableDict

'''
  Given that
    o = number of different words in note array
  Time efficiency: O(m + n + o)
'''
def checkMagazine(magazine, note):
  answer = 'Yes'
  availableDictInMagazine = addWordsToDict(magazine)
  noteDict = addWordsToDict(note)

  for word in noteDict:
    
    if word not in availableDictInMagazine or availableDictInMagazine[word] < noteDict[word]:
      answer = 'No'
      break
  
  print answer
    


#magazine = ["give", "me", "one", "grand", "today", "night"]
#note = ["give", "one", "grand", "today"]

magazine = ["avtq", "ekpvq", "z", "rdvzf", "m", "zu", "bof", "pfkzl", "ekpvq", "pfkzl", "bof", "zu", "ekpvq", "ekpvq", "ekpvq", "ekpvq", "z"]
note = ["m", "z", "z", "avtq", "zu", "bof", "pfkzl", "pfkzl", "pfkzl", "rdvzf", "rdvzf", "avtq", "ekpvq", "rdvzf", "avtq"]

checkMagazine(magazine, note)

