class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def do_subsets(nums, index, selected, ans):
            if index == len(nums):
                return ans.append(selected[:])
            selected.append(nums[index])
            do_subsets(nums, index + 1, selected, ans)
            selected.pop(-1)
            do_subsets(nums, index + 1, selected, ans)

        index = 0
        ans = []
        selected = []
        do_subsets(nums, index, selected, ans)
        return ans


nums = [1, 2, 3]
#nums = [1]
sol = Solution()
print(sol.subsets(nums))
