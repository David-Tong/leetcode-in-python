class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        L = len(nums)
        target = sum(nums) - x
        left = 0
        right = 0
        total = 0
        ans = -1
        while right < L:
            total += nums[right]
            right += 1

            while left < L and total > target:
                total -= nums[left]
                left += 1

            if total == target:
                ans = max(ans, right - left)

        if ans == -1:
            return ans
        else:
            return L - ans


nums = [1,1,4,2,3]
x = 5

#nums = [5,6,7,8,9]
#x = 4

#nums = [3,2,20,1,1,3]
#x = 10

nums = [1,1]
x = 3

solution = Solution()
print(solution.minOperations(nums, x))
