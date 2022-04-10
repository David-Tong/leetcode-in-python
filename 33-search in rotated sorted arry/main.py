class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            if nums[left] < nums[middle]:
                if nums[left] < target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target < nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1


#nums = [4, 5, 6, 7, 0, 1, 2]
#target = 0

#nums = [4, 5, 1, 2, 3]
#target = 3

#nums = [0, 1, 2, 3, 4]
#target = 0

#nums = [5, 4, 3, 2, 1]
#target = 1

#nums = [1]
#target = 1

#nums = [4, 5, 6, 7, 0, 1, 2]
#target = 1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

#nums = [1]
#target = 0

#nums = [3, 5, 1]
#target = 3

#nums = [5, 1, 3]
#target = 3

#nums = [5, 1, 2, 3, 4]
#target = 1

solution = Solution()
print(solution.search(nums, target))
