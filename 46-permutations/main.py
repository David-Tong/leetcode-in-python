class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def doPermute(selections, permutation):
            if not selections:
                self.ans.append(permutation[:])
            else:
                for selection in selections:
                    permutation.append(selection)
                    next_selections = selections.copy()
                    next_selections.remove(selection)
                    doPermute(next_selections, permutation)
                    permutation.pop(-1)
        self.ans = []
        selections = set(nums)
        permutation = []
        doPermute(selections, permutation)
        return self.ans


nums = [1, 2, 3]
nums = [0, 1]
nums = [-1, 1]
nums = [1]
solution = Solution()

print(solution.permute(nums))
