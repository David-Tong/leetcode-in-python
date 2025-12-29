class Solution(object):
    def maximumProduct(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # pre-process
        L = len(nums)
        maxis, minis = [0] * L, [0] * L

        idx = L - 1
        while idx >= 0:
            if idx == L - 1:
                maxis[idx] = nums[idx]
                minis[idx] = nums[idx]
            else:
                maxis[idx] = max(maxis[idx + 1], nums[idx])
                minis[idx] = min(minis[idx + 1], nums[idx])
            idx -= 1
        # print(maxis)
        # print(minis)

        # process
        ans = float("-inf")
        idx = 0
        while idx < L - m + 1:
            ans = max(ans, nums[idx] * maxis[idx + m - 1])
            ans = max(ans, nums[idx] * minis[idx + m - 1])
            idx += 1
        return ans


nums = [-1,-9,2,3,-2,-3,1]
m = 1

nums = [1,3,-5,5,6,-4]
m = 3

nums = [2,-1,2,-6,5,2,-5,7]
m = 2

from random import randint
nums = [randint(-1 * 10 ** 5, 10 ** 5) for _ in range(10 ** 5)]
m = 10
print(nums)

solution = Solution()
print(solution.maximumProduct(nums, m))
