import sys

def mergeSort(formattedLists):
  first = formattedLists[0]
  second = formattedLists[1]

  # first and second are already sorted
  # need to perform merge sort and turn each item into an integer 
  
  # initialize counting variables and final list
  i = 0
  j = 0
  sorted = []

  # typical merge sort approach, look at each item starting at the front of each list
  # append the lower of the two list items first
  while i < len(first) and j < len(second):
    firstInt = int(first[i])
    secondInt = int(second[j])
    if firstInt < secondInt:
      sorted.append(firstInt)
      i += 1
    else:
      sorted.append(secondInt)
      j += 1

  # if second list has been totally added to final list, add all remaining
  # items from the first list
  while i < len(first):
    sorted.append(int(first[i]))
    i += 1
  
  # if first list has been totally added to final list, add all remaining
  # items from the second list
  while j < len(second):
    sorted.append(int(second[j]))
    j += 1

  # display final sorted list
  print(sorted)
  return sorted

def formLists(stringList):
  newList = ''.join(stringList).strip('[]').split('][')
  # want to keep with goal behind problem statement and merge two sorted lists
  # rather than sorting on long list of numbers
  first = newList[0].split(',')
  second = newList[1].split(',')
  return [first, second]

if __name__ == '__main__':
  # need to format incoming arguments
  formattedLists = formLists(sys.argv[1:])
  mergeSort(formattedLists)
