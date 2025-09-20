class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        # process
        # helper function
        def total(idx):
            end = idx + 1
            start = max(0, idx - nums[idx])
            return presum[end] - presum[start]

        ans = 0
        for x in range(L):
            ans += total(x)
        return ans


nums = [2,3,1]
nums = [3,1,1,2]

solution = Solution()
print(solution.subarraySum(nums))

