class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)

        ans = list()
        for idx in range(0, N, 2):
            freq, val = nums[idx], nums[idx + 1]
            ans.extend([val] * freq)
        return ans


nums = [1,2,3,4]
nums = [1,1,2,3]

solution = Solution()
print(solution.decompressRLElist(nums))
