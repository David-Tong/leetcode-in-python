class Solution(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        # helper function
        from collections import defaultdict
        cache = defaultdict(int)
        def dfs(node, num):
            key = "{}-{}".format(node, num)
            if key in cache:
                return cache[key]

            res = node ^ num
            if parents[node] != -1:
                res = max(res, dfs(parents[node], num))

            cache[key] = res
            return res

        # process
        ans = list()
        for query in queries:
            ans.append(dfs(query[0], query[1]))
        return ans


parents = [-1,0,1,1]
queries = [[0,2],[3,2],[2,5]]

parents = [3,7,-1,2,0,7,0,2]
queries = [[4,6],[1,15],[0,5]]

solution = Solution()
print(solution.maxGeneticDifference(parents, queries))
