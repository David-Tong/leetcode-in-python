class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        idx = -1
        maxi = max(nums)
        for x in range(L):
            if nums[x] == maxi:
                idx = x
                break

        # process
        nums = sorted(nums)
        if nums[-2] == 0:
            return idx
        else:
            if (nums[-1] * 1.0) / nums[-2] >= 2:
                return idx
            else:
                return -1


nums = [3,6,1,0]
nums = [1,2,3,4]

solution = Solution()
print(solution.dominantIndex(nums))
