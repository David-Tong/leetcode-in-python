class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # pre-process
        L = len(nums)
        nums = sorted(nums)

        # process
        ans = list()
        idx = 0
        while idx < L - 1:
            num = nums[idx] + 1
            while num < nums[idx + 1]:
                ans.append(num)
                num += 1
            idx += 1
        return ans


nums = [1,4,2,5]
nums = [7,8,6,9]
nums = [5,1]

from random import randint
nums = list(set([randint(1,100) for _ in range(100)]))
print(nums)

solution = Solution()
print(solution.findMissingElements(nums))
