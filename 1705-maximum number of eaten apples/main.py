class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        # pre-process
        L = len(apples)
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        # process
        ans = 0
        idx = 0
        while idx < L or heap:
            # remove rotten apples
            while heap and heap[0][0] <= idx:
                heappop(heap)
            # add new apples
            if idx < L and apples[idx] > 0:
                heappush(heap, (idx + days[idx], apples[idx]))
            # eat apple
            if heap:
                day, apple = heappop(heap)
                ans += 1
                if apple > 1:
                    heappush(heap, (day, apple - 1))
            idx += 1
        return ans


apples = [1,2,3,5,2]
days = [3,2,1,4,2]

apples = [3,0,0,0,0,2]
days = [3,0,0,0,0,2]

apples = [3,2,1,0,0,1]
days = [1,2,3,0,0,2]

apples = [5,0,0,0,2]
days = [5,0,0,0,2]

apples = [5,0,0,1,2,3,34,1,1,4]
days = [9,0,0,2,1,2,13,1,1,1]

apples = [5,2,3]
days = [6,9,10]

apples = [2,1,10]
days = [2,10,1]

solution = Solution()
print(solution.eatenApples(apples, days))
