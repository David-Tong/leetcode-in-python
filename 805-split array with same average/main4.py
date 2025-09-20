class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre-process
        L = len(nums)
        M = 2 ** (L) - 1

        from collections import defaultdict
        dicts = defaultdict(set)
        dicts[0] = [0]

        for x in range(L):
            for key in sorted(dicts.keys(), reverse=True):
                for mask in dicts[key]:
                    dicts[key + nums[x]].add(mask | 1 << x)
        # print(dicts)

        # helper function
        def getOnes(mask):
            res = 0
            while mask:
                if mask & 1:
                    res += 1
                mask >>= 1
            return res

        averages = defaultdict(list)
        for key in dicts:
            for mask in dicts[key]:
                ones = getOnes(mask)
                if ones > 0:
                    average = key * 1.0 / ones
                    averages[average].append(mask)
        # print(averages)

        # process
        for average in averages:
            for x in range(len(averages[average])):
                mask = averages[average][x]
                for y in range(x + 1, len(averages[average])):
                    mask2 = averages[average][y]
                    if mask ^ mask2 == M:
                        # print(bin(mask), bin(mask2))
                        return True
        return False


nums = [1,2,3,4,5,6,7,8]
nums = [3,1]

from random import randint
nums = [randint(0, 10 ** 4) for _ in range(25)]
print(nums)

solution = Solution()
print(solution.splitArraySameAverage(nums))
