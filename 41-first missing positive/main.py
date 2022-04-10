class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        while x < len(nums):
           if nums[x] > 0 and nums[x] <= len(nums):
               if nums[x] != x + 1:
                   tmp = nums[x]
                   if nums[tmp-1] != nums[x]:
                       nums[x] = nums[tmp-1]
                       nums[tmp-1] = tmp
                   else:
                       x += 1
               else:
                   x += 1
           else:
               x += 1

        for x in range(len(nums)):
            if nums[x] != x + 1:
                return x + 1

        return len(nums) + 1


nums = [1, 2, 0]
#nums = [3, 4, -1, 1]
#nums = [7, 8, 9, 11, 12]
#nums = [1, 1]
#nums = [0, 2, 2, 1, 1]

solution = Solution()
print(solution.firstMissingPositive(nums))
