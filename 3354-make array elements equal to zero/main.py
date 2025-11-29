class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        total = sum(nums)
        presum = 0

        # process
        ans = 0
        for num in nums:
            presum += num
            if num == 0:
                if presum == total - presum:
                    ans += 2
                elif abs(total - presum * 2) == 1:
                    ans += 1
        return ans


nums = [1,0,2,0,3]
nums = [2,3,4,0,4,1,0]
nums = [2,3,4,0,9,0,0,18]

solution = Solution()
print(solution.countValidSelections(nums))
