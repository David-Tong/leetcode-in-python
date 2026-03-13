class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # pre-process
        M = len(landStartTime)
        N = len(waterStartTime)

        # helper function
        def can(target):
            # land first then water
            from heapq import heapify, heappush, heappop
            heap = list()
            heapify(heap)

            idx = 0
            while idx < N:
                if waterStartTime[idx] + waterDuration[idx] <= target:
                    heappush(heap, waterDuration[idx] - target)
                idx += 1

            if heap:
                water_start = -1 * heappop(heap)
                idx = 0
                while idx < M:
                    if landStartTime[idx] + landDuration[idx] <= water_start:
                        return True
                    idx += 1

            # water first then land
            heap = list()
            heapify(heap)

            idx = 0
            while idx < M:
                if landStartTime[idx] + landDuration[idx] <= target:
                    heappush(heap, landDuration[idx] - target)
                idx += 1

            if heap:
                land_start = -1 * heappop(heap)
                idx = 0
                while idx < N:
                    if waterStartTime[idx] + waterDuration[idx] <= land_start:
                        return True
                    idx += 1
                return False
            return False

        # process
        left, right = 0, 10 ** 4
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


landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]

landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]

"""
from random import randint
landStartTime = [randint(1, 1000) for _ in range(100)]
landDuration = [randint(1, 1000) for _ in range(100)]
waterStartTime = [randint(1, 1000) for _ in range(100)]
waterDuration = [randint(1, 1000) for _ in range(100)]

print(landStartTime)
print(landDuration)
print(waterStartTime)
print(waterDuration)
"""

landStartTime = [31,8]
landDuration = [47,64]
waterStartTime = [3,7]
waterDuration = [95,44]

solution = Solution()
print(solution.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
