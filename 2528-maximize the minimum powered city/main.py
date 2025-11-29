class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(stations)
        diff = [0] * (L + 1)
        for x in range(L):
            left, right = max(0, x - r), min(L, x + r + 1)
            diff[left] += stations[x]
            diff[right] -= stations[x]
        # print(diff)

        # helper function
        from copy import deepcopy
        def can(target):
            increases = k
            new_diff = deepcopy(diff)
            power = 0
            for x in range(L):
                power += new_diff[x]
                if power < target:
                    increase = target - power
                    if increase <= increases:
                        increases -= increase
                        idx = min(L, x + 2 * r + 1)
                        new_diff[idx] -= increase
                        power += increase
                    else:
                        return False
            return True

        # process
        # binary search
        left, right = 0, 10 ** 12
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                left = middle
            else:
                right = middle - 1

        if can(right):
            return right
        else:
            return left


stations = [1,2,4,5,0]
r = 1
k = 2

stations = [4,4,4,4]
r = 0
k = 3

"""
from random import randint
stations = [randint(0, 10 ** 5) for _ in range(10 ** 5)]
print(stations)
r = 1000
k = 10 ** 9
"""

stations = [100000] * (10 ** 5)
stations[-1] = 0
r = 0
k = 100000

stations = [1] * 75000 + [0] * 100000
print(stations)
r = 25000
k = 55000

solution = Solution()
print(solution.maxPower(stations, r, k))
