class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        from bisect import bisect_left, bisect_right
        negative_idx = bisect_left(nums, 0)
        positive_idx = bisect_right(nums, 0)

        negatives = negative_idx
        positives = L - positive_idx
        ans = max(negatives, positives)
        return ans


nums = [-2,-1,-1,1,2,3]
nums = [-3,-2,-1,0,0,1,2]
nums = [5,20,66,1314]
nums = [-3,-2]
nums = [0,0,0]

solution = Solution()
print(solution.maximumCount(nums))
