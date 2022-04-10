class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == val:
                return 0

        left = 0
        right = len(nums) - 1

        count = 0
        while left < right:
            if nums[left] == val:
                while right >= 0 and nums[right] == val:
                    right -= 1
                if left < right:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                    left += 1
                    right -= 1
                else:
                    break
            else:
                left += 1

        if right < 0:
            return 0

        if nums[left] == val:
            return left
        else:
            return left + 1


nums = [3, 2, 2, 3]
val = 3

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

nums = [4, 5]
val = 5

solution = Solution()
print(solution.removeElement(nums, val))
