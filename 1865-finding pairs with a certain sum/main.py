class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        from collections import defaultdict
        self.dicts1, self.dicts2 = defaultdict(int), defaultdict(int)
        for num1 in nums1:
            self.dicts1[num1] += 1
        for num2 in nums2:
            self.dicts2[num2] += 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if val <= 0:
            raise ValueError

        num2 = self.nums2[index]
        self.nums2[index] += val

        if num2 not in self.dicts2 or self.dicts2[num2] <= 0:
            raise ValueError

        self.dicts2[num2] -= 1
        self.dicts2[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        ans = 0
        for num1 in self.dicts1:
            target = tot - num1
            if target in self.dicts2:
                ans += self.dicts1[num1] * self.dicts2[target]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

nums1, nums2 = [1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]
fsp = FindSumPairs(nums1, nums2)
print(fsp.count(7))
fsp.add(3, 2)
print(fsp.count(8))
print(fsp.count(4))
fsp.add(0, 1)
fsp.add(1, 1)
print(fsp.count(7))
