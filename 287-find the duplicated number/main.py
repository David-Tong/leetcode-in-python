class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countLessThanX(nums, x):
            count = 0
            for num in nums:
                if num < x:
                    count += 1
            return count

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if countLessThanX(nums, middle) >= middle:
                right = middle - 1
            else:
                left = middle

        if countLessThanX(nums, right) >= right:
            return left
        else:
            return right


nums = [1, 3, 4, 2, 2]
#nums = [3, 1, 3, 4, 2]
#nums = [2, 2, 2, 2, 2]
nums = [1, 1]
nums = [3, 1, 3, 4, 2]
nums = [4, 1, 3, 4, 2]

solution = Solution()
print(solution.findDuplicate(nums))
