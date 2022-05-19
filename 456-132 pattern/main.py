class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        three = float("-inf")
        for num in nums[::-1]:
            if num < three:
                return True
            while stack and stack[-1] < num:
                three = max(three, stack.pop())
            stack.append(num)
        return False


nums = [1,2,3,4]
nums = [3,1,4,2]
#nums = [-1,3,2,0]
#nums = [2,2,2,2]
#nums = [2,3,2,2]
#nums = [3,4,2,2]
#nums = [1,3,2,4,5,6,7,8,9,10]

solution = Solution()
print(solution.find132pattern(nums))
