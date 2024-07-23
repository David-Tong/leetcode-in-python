class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        k = 3
        if L <= k + 1:
            return 0

        nums = sorted(nums)

        # process
        left = 0
        right = L - 1 - k
        ans = float("inf")
        while right < L:
            ans = min(ans, nums[right] - nums[left])
            left += 1
            right += 1
        return ans


nums = [5,3,2,4]
nums = [1,5,0,10,14]
nums = [3,100,20]
nums = [1,5,10,1000,1001]
nums = [0,3,8,10000,10002]

solution = Solution()
print(solution.minDifference(nums))
