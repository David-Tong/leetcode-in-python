class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        from collections import defaultdict
        colored = defaultdict(int)
        colors = defaultdict(int)

        # process
        ans = list()
        for query in queries:
            ball, color = query
            if ball in colored:
                old_color = colored[ball]
                colors[old_color] -= 1
                if colors[old_color] == 0:
                    del colors[old_color]
            colored[ball] = color
            colors[color] += 1
            ans.append(len(colors))
        return ans


limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]

limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

solution = Solution()
print(solution.queryResults(limit, queries))
