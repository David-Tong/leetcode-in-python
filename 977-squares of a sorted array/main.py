class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        ans = []
        while left < right:
            if abs(nums[left]) > abs(nums[right]):
                ans.append(nums[left] ** 2)
                left += 1
            else:
                ans.append(nums[right] ** 2)
                right -= 1

        ans.append(nums[left] ** 2)
        return ans[::-1]


nums = [-4, -1, 0, 3, 10]
nums = [-7, -3, 2, 3, 11]
nums = [1]
solution = Solution()
print(solution.sortedSquares(nums))