class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        # pre-process
        N = len(workerTimes)
        l = (mountainHeight // N + 1)
        L = l * (l + 1) * max(workerTimes)

        from math import sqrt
        M = int(sqrt(L // min(workerTimes))) + 1

        units = list()
        for x in range(M + 1):
            units.append(x * (x + 1) // 2)
        # print(units)

        # process
        # validate function
        from bisect import bisect_left
        def can(target):
            heights = 0
            for workerTime in workerTimes:
                unit = target // workerTime
                idx = bisect_left(units, unit)
                if idx >= len(units):
                    heights += len(units) - 1
                else:
                    if units[idx] == unit:
                        heights += idx
                    else:
                        heights += idx - 1
            return heights >= mountainHeight

        # binary search
        left = 1
        right = L
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                right = middle
            else:
                left = middle + 1

        if can(left):
            return left
        else:
            return right


mountainHeight = 4
workerTimes = [2,1,1]

mountainHeight = 10
workerTimes = [3,2,2,4]

mountainHeight = 5
workerTimes = [1]

mountainHeight = 100000
from random import randint
workerTimes = [randint(1, 1000) for _ in range(10000)]
print(workerTimes)

solution = Solution()
print(solution.minNumberOfSeconds(mountainHeight, workerTimes))
