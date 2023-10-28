class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)

        ans = 0
        k = 1
        while k <= L:
            n = 1
            total = 0
            while k * n * n <= L:
                total += nums[k * n * n - 1]
                n += 1
            k += 1
            ans = max(ans, total)
        return ans


nums = [8,7,3,5,7,2,4,9]
nums = [5,10,3,10,1,13,7,9,4]
nums = [6,3,4,5,1,2,3,4,5,1,2,112,88,121,98,9,45]

solution = Solution()
print(solution.maximumSum(nums))
