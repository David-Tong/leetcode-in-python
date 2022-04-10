class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        index = 1

        while index < len(nums):
            if nums[index] == majority:
                count += 1
            else:
                count -= 1

            if count == 0:
                if index < len(nums) - 1:
                    index += 1
                    count += 1
                    majority = nums[index]

            index += 1

        return majority


solution = Solution()
nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]
#nums = [6, 5, 5]
print(solution.majorityElement(nums))
