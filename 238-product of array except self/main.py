class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        product = 1
        zeros = 0
        for i in range(N):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros += 1

        ans = [0] * N
        if zeros == 1:
            for i in range(N):
                if nums[i] == 0:
                    ans[i] = product
        elif zeros == 0:
            for i in range(N):
                ans[i] = product // nums[i]
        return ans


nums = [1, 2, 3, 4]
nums = [0, 0]

solution = Solution()
print(solution.productExceptSelf(nums))
