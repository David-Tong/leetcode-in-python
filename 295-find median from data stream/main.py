class MedianFinder(object):

    def __init__(self):
        from heapq import heapify
        # left - max hep, right - min heap
        self.left = []
        self.right = []
        heapify(self.left)
        heapify(self.right)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        from heapq import heappop, heappush
        if not self.left or num < -1 * self.left[0]:
            heappush(self.left, -1 * num)
        else:
            heappush(self.right, num)

        # re-balance
        if len(self.left) < len(self.right):
            heappush(self.left, -1 * heappop(self.right))
        elif len(self.left) - len(self.right) > 1:
            heappush(self.right, -1 * heappop(self.left))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) / 2.0
        else:
            return -1 * self.left[0]


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
