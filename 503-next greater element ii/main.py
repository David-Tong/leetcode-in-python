class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        nums = nums * 2
        stack = list()
        ans = [-1] * 2 * N
        for idx, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                index, _ = stack.pop()
                ans[index] = num
            stack.append((idx, num))
        return ans[:N]


nums = [1,2,1]
nums = [1,2,3,4,3]
nums = [5,4,3,2,1]

solution = Solution()
print(solution.nextGreaterElements(nums))
