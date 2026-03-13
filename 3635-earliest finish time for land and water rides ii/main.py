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
        left, right = 0, 10 ** 6
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


from random import randint
landStartTime = [randint(1, 10 ** 5) for _ in range(5 * 10 ** 4)]
landDuration = [randint(1, 10 ** 5) for _ in range(5 * 10 ** 4)]
waterStartTime = [randint(1, 10 ** 5) for _ in range(5 * 10 ** 4)]
waterDuration = [randint(1, 10 ** 5) for _ in range(5 * 10 ** 4)]

print(landStartTime)
print(landDuration)
print(waterStartTime)
print(waterDuration)

solution = Solution()
print(solution.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
