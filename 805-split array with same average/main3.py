class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        if L == 1:
            return False

        total = sum(nums)
        for x in range(L):
            nums[x] = nums[x] * L - total
        print(nums)

        # process
        # helper function
        # get total for the mask
        def maskSum(mask, nums):
            return sum(_ for idx, _ in enumerate(nums) if mask >>idx & 1)

        # search for the left part of nums[:M]
        # to see if we have sum for 0 for a sequence in it
        M = L // 2

        from collections import defaultdict
        lefts = defaultdict(int)
        for mask in range(1, 1 << M):
            left = maskSum(mask, nums[:M])
            if left == 0:
                return True
            lefts[left] = mask

        # search for the right part of nums[M:]
        # to see if we have sum for 0 for a sequence in it,
        # or we have a sequence with a sum of total, and we have a sequence with a sum of -total in lefts
        for mask in range(1, 1 << (L - M)):
            right = maskSum(mask, nums[M:])
            if total == 0:
                return True
            opposite = right * -1
            if opposite in lefts:
                # you can't put all in one array
                if mask == 2 ** (L - M) - 1 and lefts[opposite] == 2 ** M - 1:
                    pass
                else:
                    return True
        return False


nums = [1,2,3,4,5,6,7,8]
nums = [3,1]
"""
nums = [2509, 8789, 4362, 1142, 3509, 4016, 5771, 9001, 7348, 810, 6361, 6104, 2806, 2846, 2849]
nums = [9507, 9480, 4838, 7549, 6165, 3618, 718, 4792, 2683, 3525, 3759, 6509, 1262, 1674, 8490, 3656, 5125, 354, 5778, 9219]
nums = [8896, 8367, 8093, 2072, 5074, 8254, 8662, 9761, 4551, 9961, 8685, 9605, 4341, 9116, 2159, 4146, 2564, 8062, 1053, 173, 2696, 4589, 3166, 7863, 1884]
nums = [3915, 2495, 3563, 6954, 4106, 7787, 1599, 9000, 6362, 8191, 6928, 3768, 105, 9323, 8612, 4, 1815, 429, 3214, 7102, 6528, 4829, 6230, 1651, 7833, 3073, 463, 6175, 1123, 6885]
nums = [3,1,2]
"""

solution = Solution()
print(solution.splitArraySameAverage(nums))
