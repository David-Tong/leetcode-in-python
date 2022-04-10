class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        red = 0
        white = 0
        blue = 0

        for x in range(N):
            if nums[x] == 0:
                red += 1
            elif nums[x] == 1:
                white += 1
            elif nums[x] == 2:
                blue += 1

        for x in range(N):
            if x < red:
                nums[x] = 0
            elif x < red + white:
                nums[x] = 1
            else:
                nums[x] = 2


nums = [2, 0, 2, 1, 1, 0]
nums = [2, 0, 1]

solution = Solution()
solution.sortColors(nums)
print(nums)
