class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # process
        nums = set(nums)
        idx = 1
        while idx <= L:
            target = k * idx
            if target not in nums:
                ans = target
                return ans
            else:
                idx += 1
        ans = k * idx
        return ans


nums = [8,2,3,4,6]
k = 2

nums = [1,4,7,10,15]
k = 5

nums = [8,2,10,4,6]
k = 2

solution = Solution()
print(solution.missingMultiple(nums, k))
