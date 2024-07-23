class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # pre-process
        L = 0
        for trip in trips:
            L = max(L, trip[2])
        diffs = [0] * L

        for trip in trips:
            num, start, end = trip
            diffs[start] += num
            if end < L:
                diffs[end] -= num

        # process
        passage = 0
        for idx in range(L):
            passage += diffs[idx]
            if passage > capacity:
                return False
        return True


trips = [[2,1,5],[3,3,7]]
capacity = 4

trips = [[2,1,5],[3,3,7]]
capacity = 5

trips = [[2,1,3],[2,4,5]]
capacity = 2

trips = [[2,1,4],[2,4,5]]
capacity = 2

solution = Solution()
print(solution.carPooling(trips, capacity))
