class Solution(object):
    def checkArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        diffs = [0] * L

        # process
        idx = 0
        decs = 0
        while idx < L:
            decs += diffs[idx]
            if nums[idx] - decs < 0:
                return False

            if nums[idx] - decs > 0:
                diff = nums[idx] - decs
                if idx + k > L:
                    return False
                decs += diff
                if idx + k < L:
                    diffs[idx + k] -= diff
            idx += 1
        return True


nums = [2,2,3,1,1,0]
k = 3

nums = [1,3,1,1]
k = 2

nums = [10,9,8,7,6,5,4,3,2,1]
k = 2

nums = [1,2,3,4,5,6,7,8,9,10]
k = 2

nums = [1,0,1,0,1]
k = 2

solution = Solution()
print(solution.checkArray(nums, k))
