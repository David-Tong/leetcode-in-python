class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.L = len(w)
        self.presum = list()
        for idx, item in enumerate(w):
            if idx > 0:
                self.presum.append(item + self.presum[idx - 1])
            else:
                self.presum.append(item)
        self.total = self.presum[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        from random import randint
        target = randint(1, self.total)

        from bisect import bisect_left
        idx = bisect_left(self.presum, target)
        return idx


#solution = Solution([1])
#print(solution.pickIndex())

solution = Solution([1, 3])
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
print(solution.pickIndex())
