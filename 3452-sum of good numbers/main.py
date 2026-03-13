class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        ans = 0
        for x in range(L):
            if x - k >= 0:
                if nums[x - k] >= nums[x]:
                    continue
            if x + k < L:
                if nums[x + k] >= nums[x]:
                    continue
            ans += nums[x]
        return ans


nums = [1,3,2,1,5,4]
k = 2

nums = [2,1]
k = 1

solution = Solution()
print(solution.sumOfGoodNumbers(nums, k))
