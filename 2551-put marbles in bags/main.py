class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        L = len(weights)

        # short-cut
        if k == L or k == 1:
            return 0

        from heapq import heapify, heappush, heappop
        minis = list()
        maxis = list()
        heapify(minis)
        heapify(maxis)

        idx = 1
        while idx < L:
            heappush(minis, weights[idx - 1] + weights[idx])
            heappush(maxis, (weights[idx - 1] + weights[idx]) * - 1)
            idx += 1

        mini_score = 0
        maxi_score = 0
        for _ in range(k - 1):
            mini_score += heappop(minis)
            maxi_score -= heappop(maxis)

        ans = maxi_score - mini_score
        return ans


weights = [1,3,5,1]
k = 2

weights = [1, 3]
k = 2

weights = [1,2,5,6,74,3,12,11,2,34,5,6,7]
k = 5

weights = [1,2,5,6,74]
k = 3

solution = Solution()
print(solution.putMarbles(weights, k))