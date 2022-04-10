class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]


solution = Solution()
numbers = [2, 7, 11, 15]
target = 9
numbers = [2, 3, 4]
target = 6
numbers = [-1, 0]
target = -1
numbers = [2, 2]
target = 4
print(solution.twoSum(numbers, target))
