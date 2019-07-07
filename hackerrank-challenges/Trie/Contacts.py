def mergeTwoFiles(file1, file2):
  return file1 + file2



def minimumTime(numOfSubFiles, files):
  orderedFiles = sorted(files)
  timeToMerge = [[0 for i in xrange(len(orderedFiles))] for i in xrange(len(orderedFiles))]
  timeToMerge[0] = orderedFiles[0]
  totalTime = 0
  for i in xrange(1, len(orderedFiles)):
    timeToMerge[i] = mergeTwoFiles(orderedFiles[i], timeToMerge[i-1])
    totalTime += timeToMerge[i]
  return totalTime
        


n = 4
files = [8, 4, 6, 12]

print minimumTime(n, files)