class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # process
        c = 0
        ans = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                ans = max(ans, c)
                c = 0
        ans = max(ans, c)
        return ans


nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]

solution = Solution()
print(solution.findMaxConsecutiveOnes(nums))
