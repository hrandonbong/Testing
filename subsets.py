from collections import deque

def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  subsets = []
  subsets.append([])
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
        # The last time we saw this repeated value was at the endIndex
        # of the previous run
      startIndex = endIndex + 1
    endIndex = len(subsets) - 1
    for j in range(startIndex, endIndex+1):
      # create a new subset from the existing subset and add the current element to it
      set1 = list(subsets[j])
      set1.append(nums[i])
      subsets.append(set1)
  return subsets


def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutations = deque()
  permutations.append([])
  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create new permutations
    n = len(permutations)
    for _ in range(n):
      oldPermutation = permutations.popleft()
      # create a new permutation by adding the current number at every position
      for j in range(len(oldPermutation)+1):
        newPermutation = list(oldPermutation)
        newPermutation.insert(j, currentNumber)
        if len(newPermutation) == numsLength:
          result.append(newPermutation)
        else:
          permutations.append(newPermutation)

  return result

def find_letter_case_string_permutations(str):
  permutations = []
  permutations.append(str)
  # process every character of the string one by one
  for i in range(len(str)):
    if str[i].isalpha():  # only process characters, skip digits
      # we will take all existing permutations and change the letter case appropriately
      n = len(permutations)
      for j in range(n):
        chs = list(permutations[j])
        # if the current character is in upper case, change it to lower case or vice versa
        chs[i] = chs[i].swapcase()
        permutations.append(''.join(chs))

  return permutations


class ParenthesesString:
  def __init__(self, str, openCount, closeCount):
    self.str = str
    self.openCount = openCount
    self.closeCount = closeCount


def generate_valid_parentheses(num):
  result = []
  queue = deque()
  queue.append(ParenthesesString("", 0, 0))
  while queue:
    ps = queue.popleft()
    value = ps.str
    # if we've reached the maximum number of open and close parentheses, add to the result
    if ps.openCount == num and ps.closeCount == num:
      result.append(ps.str)
    else:
      if ps.openCount < num:  # if we can add an open parentheses, add it
        queue.append(ParenthesesString(
          ps.str + "(", ps.openCount + 1, ps.closeCount))

      if ps.openCount > ps.closeCount:  # if we can add a close parentheses, add it
        queue.append(ParenthesesString(ps.str + ")",
                                       ps.openCount, ps.closeCount + 1))
  return result


def find_opp(arr):
  dict = {}
  result = []
  for i in arr:
    if i >= 0:
      if not dict.get(i):
        dict[i] = 0
      dict[i] += 1
    else:
      if dict.get(abs(i)):
        result.append(abs(i))
  return result


if __name__ == '__main__':
  # print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  # print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
  #
  # print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
  #
  # print("String permutations are: " +
  #       str(find_letter_case_string_permutations("ad52")))
  # print("String permutations are: " +
  #       str(find_letter_case_string_permutations("ab7c")))
  #
  # print("All combinations of balanced parentheses are: " +
  #       str(generate_valid_parentheses(2)))
  #
  # print(find_permutation('odicf', 'dc'))
  arr = [1,-1, 2, 3, 4, 5, 6, 7, 8, 9, -9]
  print(find_opp(arr))

  dict = 0
  if dict:
    print('zero')


