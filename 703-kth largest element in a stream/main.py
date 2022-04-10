class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        from bisect import bisect_left
        idx = bisect_left(self.nums, val)
        self.nums = self.nums[0:idx] + [val] + self.nums[idx:]
        return self.nums[len(self.nums) - self.k]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(11))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
