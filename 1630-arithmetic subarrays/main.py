class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        M = len(l)
        anses = [False] * M

        def checkArithmetic(nums, left, right):
            nums = sorted(nums[left:right + 1])
            L = len(nums)
            if len(nums) < 2:
                return False
            elif len(nums) == 2:
                return True
            else:
                gap = nums[1] - nums[0]

            for x in range(2, L):
                if nums[x] - nums[x - 1] != gap:
                    return False
            return True

        for x in range(M):
            anses[x] = checkArithmetic(nums, l[x], r[x])

        return anses


nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]

solution = Solution()
print(solution.checkArithmeticSubarrays(nums, l, r))
