class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        from collections import defaultdict
        out_degrees = defaultdict(int)

        for path in paths:
            out_degrees[path[0]] += 1
            out_degrees[path[1]] += 0

        for city in out_degrees:
            if out_degrees[city] == 0:
                return city


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths = [["B","C"],["D","B"],["C","A"]]
paths = [["A","Z"]]

solution = Solution()
print(solution.destCity(paths))
