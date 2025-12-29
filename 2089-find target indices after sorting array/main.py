class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        ans = list()
        for x in range(L):
            if nums[x] == target:
                ans.append(x)
        return ans


nums = [1,2,5,2,3]
target = 2

solution = Solution()
print(solution.targetIndices(nums, target))
