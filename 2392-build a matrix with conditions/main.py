class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """
        def topologicalSort(conditions):
            ingrees = [0] * (k + 1)
            from collections import defaultdict
            dependencies = defaultdict(list)

            for condition in conditions:
                ingrees[condition[1]] += 1
                dependencies[condition[0]].append(condition[1])

            from collections import deque
            queue = deque()
            for x in range(k):
                if ingrees[x + 1] == 0:
                    queue.append(x + 1)

            idx = 0
            ans = defaultdict(list)
            while queue:
                size = len(queue)
                for x in range(size):
                    dependee = queue.popleft()
                    ans[dependee] = [_ for _ in range(idx, idx + size)]
                    for dependent in dependencies[dependee]:
                        ingrees[dependent] -= 1
                        if ingrees[dependent] == 0:
                            queue.append(dependent)
                idx += size

            return ans

        def place(x, rows, cols):
            for row in rows:
                for col in cols:
                    if grid[row][col] == 0:
                        grid[row][col] = x
                        return True
            return False


        rowOpts = topologicalSort(rowConditions)
        colOpts = topologicalSort(colConditions)

        grid = [[0] * k for _ in range(k)]
        for x in range(k):
            rows = rowOpts[x + 1]
            cols = colOpts[x + 1]
            if not place(x + 1, rows, cols):
                return list()
        return grid


k = 3
rowConditions = [[1,2],[3,2]]
colConditions = [[2,1],[3,2]]

k = 3
rowConditions = [[1,2],[2,3],[3,1],[2,3]]
colConditions = [[2,1]]

solution = Solution()
print(solution.buildMatrix(k, rowConditions, colConditions))
