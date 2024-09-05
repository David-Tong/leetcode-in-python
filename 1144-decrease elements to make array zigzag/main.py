class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L <= 2:
            return 0

        # case 1 : A[0] > A[1] < A[2]
        # reduce nums in odd indexes
        idx = 1
        ans = 0
        while idx < L:
            mini = float("inf")
            if idx - 1 >= 0:
                mini = nums[idx - 1]
            if idx + 1 < L:
                mini = min(mini, nums[idx + 1])
            ans += max(0, nums[idx] - (mini - 1))
            idx += 2

        # case 2 : A[0] < A[1] > A[2]
        # reduce nums in even indexes
        idx = 0
        ans2 = 0
        while idx < L:
            mini = float("inf")
            if idx - 1 >= 0:
                mini = nums[idx - 1]
            if idx + 1 < L:
                mini = min(mini, nums[idx + 1])
            ans2 += max(0, nums[idx] - (mini - 1))
            idx += 2
        print(ans, ans2)
        return min(ans, ans2)


nums = [1,2,3]
nums = [9,6,1,6,2]
nums = [1]
nums = [2,3]
nums = [1,2,4,1,2,3,1,4,5,6,1,8]
nums = [4,3,1,5,6,11,2,3,4,568,14,1,13,4,6,7,8,12,22]
nums = [7,4,8,9,7,7,5]

solution = Solution()
print(solution.movesToMakeZigzag(nums))
