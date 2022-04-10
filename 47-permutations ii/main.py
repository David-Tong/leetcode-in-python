class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def doPermute(selections, candidates):
            if len(candidates) == 0:
                self.anses.append(selections)
            for idx, candidate in enumerate(candidates):
                if candidate not in candidates[:idx]:
                    selections.append(candidate)
                    doPermute(selections[:], candidates[:idx] + candidates[idx+1:])
                    selections.pop()

        self.anses = []
        doPermute([], nums)
        return self.anses


nums = [1, 1, 2]
nums = [1, 2, 3]
nums = [1, 1, 1, 1, 1, 1, 1, 1]
nums = [1]

solution = Solution()
print(solution.permuteUnique(nums))
