import collections
from collections import deque
import json

def maxProfit(prices):
    left = 0  # Buy
    right = 1  # Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left]  # our current Profit
        if prices[left] < prices[right]:
            max_profit = max(currentProfit, max_profit)
        else:
            left = right
        right += 1
    return max_profit


class Solution:
    def floodFill(self, image, sr, sc, color):
        self.islands(image, sr, sc, color, image[sr][sc])
        return image

    def islands(self, grid, i, j, c, prev):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != prev:
            return
        current = grid[i][j]

        if grid[i][j] == prev:
            grid[i][j] = c

        self.islands(grid, i + 1, j, c, current)
        self.islands(grid, i - 1, j, c, current)
        self.islands(grid, i, j + 1, c, current)
        self.islands(grid, i, j - 1, c, current)

def insert(intervals, new_interval):
  merged = []
  start, end = 0, 1
  for i in range(len(intervals)):
    if intervals[i][end] < new_interval[start]:
      merged.append(intervals[i])
    elif intervals[i][start] <= new_interval[end]:
      new_interval[start] = min(intervals[i][start], new_interval[start])
      new_interval[end] = max(intervals[i][end], new_interval[end])
      merged.append(new_interval)
    elif intervals[i][start] > new_interval[end]:
      merged.append(intervals[i])
  # TODO: Write your code here
  return merged

def minWindow(s, t):
    # get char counts in t
    # tCharCount = {}
    # for char in t:
    #     tCharCount[char] = tCharCount.get(char, 0) + 1
    tCharCount = collections.Counter(t)

    # left and right pointers
    l = r = 0
    # num chars we need in substring
    need = len(t)
    # num we have
    have = 0
    # length of our answer
    minLen = len(s) + 1
    ans = ''

    for r in range(len(s)):
        # if char is in tChar hash and the count of of that char is > 0, then we have gained a char
        if s[r] in tCharCount:
            if tCharCount[s[r]] > 0:
                have += 1
            tCharCount[s[r]] -= 1

        # while we have more than or equal to we need, check length and update accordingly
        # then update left pointer and the char it points to if in tCharHash
        # if the count of that char is in the hash and its count rises above 0, we have lost a char
        while have >= need:
            if (r - l) + 1 < minLen:
                ans = s[l:r + 1]
                minLen = (r - l) + 1

            if s[l] in tCharCount:
                tCharCount[s[l]] += 1
                if tCharCount[s[l]] > 0:
                    have -= 1
            l += 1

    return ans

def findAnagrams(s, p):

    myDictP = collections.Counter(p)
    myDictS = collections.Counter(s[:len(p)])

    output = []
    i = 0
    j = len(p)

    while j <= len(s):
        if myDictS == myDictP:

            output.append(i)

        myDictS[s[i]] -= 1
        if myDictS[s[i]] <= 0:
            myDictS.pop(s[i])

        if j < len(s):
            myDictS[s[j]] += 1
        j += 1
        i += 1

    return output

def trap(bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right:
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume



class MaxProfit:
    def jobScheduling(self, startTime, endTime, profit):
        # O(nlog(n))
        lst = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dpEndTime = [0]
        dpProfit = [0]

        for start, end, pro in lst:
            # find rightMost idx to insert this start time
            # idx is where this new start needs to be inserted
            # idx - 1 is the one that doesn't overlap

            # We use this binary search in order to go through our dpEndTimes
            # If we've seen an end time that produces a profit that we can add
            # to the current profit we return that index. ELSE we return 1 for
            # start times that overlap with our current MAX end time
            idx = self.bSearch(dpEndTime, start)

            lastProfit = dpProfit[-1]

            # idx - 1 will not overlap with the current start time
            currProfit = dpProfit[idx - 1] + pro  # they don't overlap

            # whener we find currProfit greater than last, we update
            if currProfit > lastProfit:
                dpEndTime.append(end)
                dpProfit.append(currProfit)

        return dpProfit[-1]

    def bSearch(self, dp, target):
        left, right = 0, len(dp)

        while left < right:
            mid = (left + right) // 2

            if dp[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

from itertools import accumulate


def getServedBuildings(buildingCount, routerLocation, routerRange):
    served_buildings = 0

    difference_array = [0]*(len(buildingCount)+1)

    for router in range(len(routerLocation)):
        lo = routerLocation[router] - 1 - routerRange[router]
        hi = routerLocation[router] - 1 + routerRange[router]

        if lo < 0:
            lo = 0

        if hi >= len(difference_array):
            hi = len(difference_array)-1

        difference_array[lo] += 1
        difference_array[hi] -= 1

    for i in range(1,len(difference_array)):
        difference_array[i] = difference_array[i] + difference_array[i-1]

    for building in range(len(buildingCount)):
        if difference_array[building] >= buildingCount[building]:
            served_buildings += 1

    return served_buildings


def knapsack_0_1(W, n, weights, values):
    dp = [[0 for x in range(n + 1)] for x in range(W + 1)]
    for x in range(1, W + 1):
        for i in range(1, n + 1):
            dp[x][i] = dp[x][i - 1]
            wi = weights[i - 1]
            vi = values[i - 1]
            if x >= wi:
                dp[x][i] = max(dp[x][i], dp[x - wi][i - 1] + vi)
    for i,v in enumerate(dp):
        print("row",i,":",v)
    return dp[W][n]


def topological_sort(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
    return sortedOrder

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
  graph = {i: [] for i in range(vertices)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder

def isValid(stale, latest, otjson):
    # Start our cursor
    i = 0

    # Transform json to array
    otjson = json.loads(otjson)

    # Loop through commands
    for dict in otjson:

        # Inserting strings
        if dict["op"] == "insert":
            stale = stale[:i] + dict["chars"] + stale[i:]
            # Cannot splice from index 0
            # if i == 0:
            #     stale = dict["chars"] + stale
            # else:
            #     part_1 = stale[:i]
            #     part_2 = stale[i:]
            #     stale = stale[:i] + dict["chars"] + stale[i:]

        # We are adding to our cursor to move to new index
        if dict["op"] == "skip":
            i += dict["count"]
            if i > len(stale):
                return False

        # Deleting all char after delete count
        if dict["op"] == "delete":
            if dict["count"] > len(stale):
                return False
            stale = stale[0:i]

    if stale[-1] not in ".?!":
        stale += "."
    return stale == latest

def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[end] >= target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

class cut:
    def ways(self, grid, k):
        n, m = len(grid), len(grid[0])
        N, M = n + 1, m + 1
        sum_grid = [[0] * M for _ in range(N)]
        for i in range(1, N):
            for j in range(1, M):
                sum_grid[i][j] = sum_grid[i-1][j] + sum_grid[i][j-1] - sum_grid[i-1][j-1] + int(grid[i-1][j-1] == 'A')

        dp = {}

        #[[0, 0, 0, 0],
        # [0, 0, 1, 1],
        # [0, 1, 2, 3],
        # [0, 1, 2, 3]]

        def count(a, b, c, d):
            return sum_grid[c][d] - sum_grid[a][d]\
                 - sum_grid[c][b] + sum_grid[a][b]
        def dfs(a, b, k):
            if (a, b, k) in dp: return dp[(a, b, k)]
            if k == 1 and count(a, b, n, m) >= 1: return 1

            ret = 0
            for i in range(a + 1, n):
                if count(a, b, i, m) >= 1:
                    ret = (ret + dfs(i, b, k - 1))
            for j in range(b + 1, m):
                if count(a, b, n, j) >= 1:
                    ret = (ret + dfs(a, j, k - 1))
            dp[(a, b, k)] = ret
            return ret
        var = dfs(0, 0, k)
        return var

class Queens:
    def solveNQueens(self, n):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res

    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            print(nums)
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in range(n):
            # First check verifies diag members
            # Second check verifies if they are in the same row
            if abs(nums[i]-nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

if __name__ == '__main__':
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    #print(minWindow("ADOBECDEEBANC","ABC"))
    # s = "carcbaebabacd"
    # p = "abc"
    # print(findAnagrams(s,p))
    # print(subsets("23"))
    # trap([0,1,0,2,1,0,1,3,2,1,2,1])
    #print(Queens().solveNQueens(4))
    # MaxProfit().jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70])
    # print(getServedBuildings([1,2,1,2,2],[3,1,3],[1,2,3]))
    #print(knapsack_0_1(10, 5, [4, 9, 3, 5, 7], [10, 25, 13, 20, 8]))
    # print("Topological sort: " +
    #       str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    # nums = [4,5,6,7,0,1,2]
    # target = 0
    # print(search(nums,target))
    # var = cut()
    # print(var.ways([".A.","A.A","..."],3))
    Queens().solveNQueens(4)