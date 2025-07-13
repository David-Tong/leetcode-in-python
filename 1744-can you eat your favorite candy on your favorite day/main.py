class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # pre-process
        presum = [0]
        for candy in candiesCount:
            presum.append(presum[-1] + candy)

        # process
        ans = list()
        from bisect import bisect_left, bisect_right
        for query in queries:
            type, day, cap = query
            mini, maxi = day + 1, (day + 1) * cap
            idx_mini = bisect_left(presum, mini)
            idx_maxi = bisect_left(presum, maxi)
            if idx_mini <= type + 1 <= idx_maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans


candiesCount = [7,4,5,3,8]
queries = [[0,2,2],[1,2,2],[0,8,3],[1,3,2],[4,2,4],[2,13,1000000000]]

candiesCount = [8,4,5,3,8]
queries = [[1,3,2],[0,9,2]]

"""
candiesCount = [5,2,6,4,1]
queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
"""

solution = Solution()
print(solution.canEat(candiesCount, queries))
