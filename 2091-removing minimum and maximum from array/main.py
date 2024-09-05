class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        min_idx, min_val = -1, float("inf")
        max_idx, max_val = -1, float("-inf")

        for idx, num in enumerate(nums):
            if num < min_val:
                min_idx = idx
                min_val = num
            if num > max_val:
                max_idx = idx
                max_val = num

        # process
        maxi = max(min_idx, max_idx)
        mini = min(min_idx, max_idx)

        ans = min(mini + 1 + L - maxi, min(maxi + 1, L - mini))
        return ans


nums = [2,10,7,5,4,1,8,6]
nums = [0,-4,19,1,8,-2,-3,5]
nums = [101]

solution = Solution()
print(solution.minimumDeletions(nums))
