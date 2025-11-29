class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        ans = sum(nums) % k
        return ans


nums = [3,9,7]
k = 5

nums = [4,1,3]
k = 4

nums = [3,2]
k = 6

solution = Solution()
print(solution.minOperations(nums, k))
