class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        nums = sorted(nums)

        # process
        maxis = sum(nums[-k:])
        minis = sum(nums[:k])
        ans = maxis - minis
        return ans


nums = [5,2,2,4]
k = 2

nums = [100]
k = 1

solution = Solution()
print(solution.absDifference(nums, k))
