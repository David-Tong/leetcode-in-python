class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        from collections import defaultdict
        self.dicts = defaultdict(list)
        for idx, num in enumerate(nums):
            self.dicts[num].append(idx)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target in self.dicts:
            if len(self.dicts[target]) == 1:
                return self.dicts[target][0]
            else:
                import random
                idx = random.randint(0, len(self.dicts[target]) - 1)
                return self.dicts[target][idx]


nums = [1, 2, 3, 3, 3]

solution = Solution(nums)
print(solution.pick(3))
print(solution.pick(1))
print(solution.pick(3))
