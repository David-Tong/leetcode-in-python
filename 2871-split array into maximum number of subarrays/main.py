class Solution(object):
    def maxSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        ans = 0
        score = nums[0]
        for x in range(L):
            score &= nums[x]
            if score == 0:
                ans += 1
                if x < L - 1:
                    score = nums[x + 1]
        return ans if ans > 0 else 1


nums = [1,0,2,0,1,2]
nums = [5,7,1,3]
nums = [4,5,6,7,1,2,1,4]

solution = Solution()
print(solution.maxSubarrays(nums))