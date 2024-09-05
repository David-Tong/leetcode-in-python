class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        L = len(nums)

        idx = 0
        total = sum(nums[:idx + k])
        ans = total * 1.0 / k
        while idx + k < L:
            idx += 1
            total -= nums[idx - 1]
            total += nums[idx + k - 1]
            ans = max(ans, total * 1.0 / k)

        return ans


nums = [1,12,-5,-6,50,3]
k = 4

nums = [5]
k = 1

solution = Solution()
print(solution.findMaxAverage(nums, k))
