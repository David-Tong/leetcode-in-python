class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        boundary, minIdx, maxIdx = -1, -1, -1
        ans = 0
        # use the x to get the right of the array
        for x in range(L):
            if minK <= nums[x] <= maxK:
                if nums[x] == minK:
                    minIdx = x
                if nums[x] == maxK:
                    maxIdx = x
                ans += max(0, min(minIdx, maxIdx) - boundary)
            else:
                # use boundary to get the left of the array
                boundary = x
        return ans


nums = [1,3,5,2,7,5]
minK = 1
maxK = 5

solution = Solution()
print(solution.countSubarrays(nums, minK, maxK))
