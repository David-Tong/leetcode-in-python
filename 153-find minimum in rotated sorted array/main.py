class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            # if x < y and arr[x] < arr[y], then the rotated point is not there
            if nums[left] < nums[middle]:
                if nums[middle] > nums[right]:
                    left = middle
                else:
                    return nums[left]
            elif nums[left] > nums[middle]:
                if nums[middle] < nums[right]:
                    right = middle
                else:
                    return nums[right]

        ans = min(nums[left], nums[right])
        if left > 0:
            ans = min(ans, nums[left - 1])
        if right < len(nums) - 1:
            ans = min(ans, nums[right + 1])
        return ans


nums = [3,4,5,1,2]
#nums = [4,5,6,7,0,1,2]
#nums = [11,13,15,17]
#nums = [5,4,3,2,1]
#nums = [5,1,2,3,4]
#nums = [2,3,4,5,1]
#nums = [1,2]

solution = Solution()
print(solution.findMin(nums))
