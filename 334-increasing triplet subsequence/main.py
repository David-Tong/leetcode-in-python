class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mini = float("inf")
        stack = []
        for num in nums:
            mini = min(mini, num)
            if num > mini:
                while len(stack) > 0 and stack[-1] >= num:
                    stack.pop()
                stack.append(num)
                if len(stack) > 1:
                    return True
        return False


nums = [1, 2, 3, 4, 5]
#nums = [5, 4, 3, 2, 1]
#nums = [3, 1, 4, 2, 5]
#nums = [3, 1, 4, 2, 2]
#nums = [1, 2]
#nums = [1, 1, -2, 6]
#nums = [1, 5, 0, 4, 1, 3]

solution = Solution()
print(solution.increasingTriplet(nums))
