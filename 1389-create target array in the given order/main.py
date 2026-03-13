class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        # process
        ans = list()
        for x, idx in enumerate(index):
            ans.insert(idx, nums[x])
        return ans


nums = [0,1,2,3,4]
index = [0,1,2,2,1]

nums = [1,2,3,4,0]
index = [0,1,2,3,0]

nums = [1]
index = [0]

solution = Solution()
print(solution.createTargetArray(nums, index))
