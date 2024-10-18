class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        presums = list()
        presums.append(arr[0])
        for num in arr[1:]:
            presums.append(presums[-1] ^ num)

        # process
        anses = list()
        for query in queries:
            start, end = query
            presum = None
            if start != 0:
                presum = presums[start - 1]
            ans = presums[end]
            if presum:
                ans ^= presum
            anses.append(ans)
        return anses


arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]

solution = Solution()
print(solution.xorQueries(arr, queries))
