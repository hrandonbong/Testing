from heapq import *

class MedianOfAStream:
  def __init__(self):
    self.minHeap = []
    self.maxHeap = []

  def insert_num(self, num):
   # TODO: Write your code here
    if not self.maxHeap or -self.maxHeap[0] >= num:
      # Heaps store numbers in ascending order, so to keep [0] as the max we make all numbers
      # negative. So biggest number stays at [0] as a negative. Cuz negative is -bigger number is
      # the smaller number.
      heappush(self.maxHeap, -num)
    else:
      heappush(self.minHeap, num)

  def find_median(self):
    # TODO: Write your code here
    if len(self.maxHeap) == len(self.minHeap):
      # we have even number of elements, take the average of middle two elements
      return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

    # because max-heap will have one more element than the min-heap
    return -self.maxHeap[0] / 1.0


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
