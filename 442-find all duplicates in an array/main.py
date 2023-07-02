class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = list()
        for num in nums:
            num = abs(num)
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
            else:
                ans.append(num)
        return ans


nums = [4,3,2,7,8,2,3,1]
nums = [1,1,2]
nums = [1]
nums = [2,2]
nums = [1,2,2,1]

solution = Solution()
print(solution.findDuplicates(nums))
