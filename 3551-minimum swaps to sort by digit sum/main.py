class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)

        # helper function
        def getDigitSum(num):
            res = 0
            for digit in str(num):
                res += int(digit)
            return res

        pairs = list(zip(list(map(getDigitSum, nums)), nums))
        pairs = sorted(pairs)
        # print(pairs)

        # map to dicts
        dicts = {val: idx for idx, (key, val) in enumerate(pairs)}

        # pre-process nums
        arr = list()
        dicts2 = dict()
        for idx, num in enumerate(nums):
            arr.append(dicts[num])
            dicts2[dicts[num]] = idx
        # print(arr)
        # print(dicts2)

        # process
        idx = 0
        ans = 0
        while idx < L:
            if arr[idx] != idx:
                idx2 = dicts2[idx]
                arr[idx], arr[idx2] = arr[idx2], arr[idx]
                dicts2[arr[idx]], dicts2[arr[idx2]] = idx, idx2
                ans += 1
            idx += 1
        return ans


nums = [37,100]
nums = [22,14,33,7]
nums = [18,43,34,16]

"""
from random import randint
nums = list(set([randint(1, 100) for _ in range(10)]))
print(nums)
"""

nums = [67,77,82,19,52,54,90,61]

solution = Solution()
print(solution.minSwaps(nums))
