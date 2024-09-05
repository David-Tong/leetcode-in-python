class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        last_min, last_max = -1, -1
        start = 0

        ans = 0
        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                start = idx
                last_min, last_max = -1, -1

            if num == minK:
                last_min = idx

            if num == maxK:
                last_max = idx

            ans += max(0, min(last_min, last_max) - start + 1)
        return ans


nums = [1,3,5,2,7,5]
minK = 1
maxK = 5

nums = [1,1,1,1]
minK = 1
maxK = 1

solution = Solution()
print(solution.countSubarrays(nums, minK, maxK))
