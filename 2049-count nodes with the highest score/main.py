class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        # pre-process
        N = len(parents)
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, parent in enumerate(parents):
            if parent != -1:
                dicts[parent].append(idx)

        # process
        self.values = defaultdict(int)

        # dfs
        def dfs(node):
            children = dicts[node]
            values = list()
            for child in children:
                values.append(dfs(child))
            res = sum(values) + 1
            if node != 0:
                values.append(N - sum(values) - 1)
            self.values[node] = 1
            for value in values:
                self.values[node] *= value
            return res

        dfs(0)
        maxi = max(self.values.values())
        ans = 0
        for node in self.values:
            if self.values[node] == maxi:
                ans += 1
        return ans


parents = [-1,2,0,2,0]
parents = [-1,2,0]

solution = Solution()
print(solution.countHighestScoreNodes(parents))
