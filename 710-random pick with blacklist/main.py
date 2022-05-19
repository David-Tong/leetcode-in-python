class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.blacklist = sorted(blacklist)
        # how many number before the blacklist[x]
        self.nums = [num - idx for idx, num in enumerate(self.blacklist)]
        self.L = n - len(blacklist)

    def pick(self):
        """
        :rtype: int
        """
        import random
        rand = random.randint(0, self.L - 1)
        from bisect import bisect_right
        idx = bisect_right(self.nums, rand)
        if idx > 0:
            return rand - self.nums[idx - 1] + 1 + self.blacklist[idx - 1]
        else:
            return rand 


solution = Solution(7, [2, 3, 5])
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
