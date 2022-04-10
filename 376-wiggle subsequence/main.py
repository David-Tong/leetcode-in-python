class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        stack.append(nums[0])
        ascending = None
        for idx, num in enumerate(nums[1:]):
            if num > nums[idx]:
                if ascending:
                    stack.pop(-1)
                else:
                    ascending = True
                stack.append(num)
            elif num < nums[idx]:
                if ascending is not None and not ascending:
                    stack.pop(-1)
                else:
                    ascending = False
                stack.append(num)
        return len(stack)


nums = [1, 7, 4, 9, 2, 5]
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [1, 5, 5, 5, 3, 3, 1, 2, 9, 10, -2, -6, -3]
nums = [1, 1, 1, 3, 5, 4]
nums = [3, 3, 3, 2, 5]


solution = Solution()
print(solution.wiggleMaxLength(nums))
