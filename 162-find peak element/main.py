class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            # peak between left and middle
            if nums[middle] < nums[left]:
                right = middle - 1
            # peak between middle and right
            elif nums[middle] < nums[right]:
                left = middle + 1
            # peak between left and right
            # nums[middle] >= left and nums[middle] >= right
            else:
                if nums[middle] < nums[middle - 1]:
                    right = middle - 1
                elif nums[middle] < nums[middle + 1]:
                    left = middle + 1
                else:
                    return middle

        if nums[right] > nums[left]:
            return right
        else:
            return left


nums = [1,2,3,1]
nums = [1,2,1,3,5,6,4]
nums = [1,2,4]
nums = [1]
nums = [4,1]

solution = Solution()
print(solution.findPeakElement(nums))
