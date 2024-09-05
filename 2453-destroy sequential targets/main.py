class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        from collections import defaultdict
        dicts = defaultdict(tuple)

        nums = sorted(nums)
        for num in nums[::-1]:
            mod = num % space
            if mod not in dicts:
                dicts[mod] = (num, 1)
            else:
                dicts[mod] = (num, dicts[mod][1] + 1)

        print(dicts)

        maxi = 0
        mods = list()
        for key in dicts:
            if maxi <= dicts[key][1]:
                if maxi < dicts[key][1]:
                    mods = list()
                mods.append(dicts[key][0])
                maxi = dicts[key][1]

        ans = min(mods)
        return ans


nums = [3,7,8,1,1,5]
space = 2

"""
nums = [1,3,5,2,4,6]
space = 2

nums = [6,2,5]
space = 100

nums = [101,102,33,4,99,22,77,13,45,123,87,113411,45678,124321]
space = 712

nums = [2,3,4,1,4,5,3,4,5,2]
space = 10000
"""

solution = Solution()
print(solution.destroyTargets(nums, space))
