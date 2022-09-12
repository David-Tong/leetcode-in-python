class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        spares = list()
        for idx in range(len(capacity)):
            spares.append(capacity[idx] - rocks[idx])
        heapify(spares)

        ans = 0
        while additionalRocks > 0 and len(spares) > 0:
            additionalRocks -= heappop(spares)
            if additionalRocks >= 0:
                ans += 1

        return ans


capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2

capacity = [10,2,2]
rocks = [2,2,0]
additionalRocks = 100

capacity = [91,54,63,99,24,45,78]
rocks = [35,32,45,98,6,1,25]
additionalRocks = 17

solution = Solution()
print(solution.maximumBags(capacity, rocks, additionalRocks))
