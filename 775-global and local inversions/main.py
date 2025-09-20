class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)

        # process
        idx = 0
        while idx < L - 1:
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                idx += 1
            idx += 1
        sorts = sorted(nums)

        for x in range(L):
            if nums[x] != sorts[x]:
                return False
        return True


nums = [1,0,2]
nums = [1,2,0]
nums = [0, 3, 1, 2, 4]

solution = Solution()
print(solution.isIdealPermutation(nums))

from itertools import permutations
for nums in list(permutations(range(0, 3))):
    nums = list(nums)
    print(nums)
    print(solution.isIdealPermutation(nums))