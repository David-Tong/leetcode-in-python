class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        ans = 0
        from bisect import bisect_right
        for idx, num in enumerate(nums):
            target = num + 2 * k
            idx_right = bisect_right(nums, target)
            ans = max(ans, idx_right - idx)
            if L - idx < ans:
                break
        return ans


nums = [4,6,1,2]
k = 2

nums = [1,1,1,1]
k = 10

nums = [2,3,4,5,6,2,3,2,4,11,13,16,14,55,4,3,2,6,7,9]
k = 5

solution = Solution()
print(solution.maximumBeauty(nums, k))
