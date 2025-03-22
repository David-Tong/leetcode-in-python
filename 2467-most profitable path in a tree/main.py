class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(dict)
        for edge in edges:
            dicts[edge[0]][edge[1]] = True
            dicts[edge[1]][edge[0]] = True
        # print(dicts)

        # process bob
        self.path = list()
        visited = defaultdict(bool)
        visited[0] = True
        paths = [0]
        def search_bob(node):
            if node == bob:
                self.path = paths
                return True

            for nxt in dicts[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    paths.append(nxt)
                    if search_bob(nxt):
                        return True
                    paths.pop()

            return False

        search_bob(0)
        bob_path = defaultdict(int)
        for idx, path in enumerate(self.path[::-1]):
            bob_path[path] = idx
        # print(bob_path)

        # process alice
        self.ans = float("-inf")
        visited = defaultdict(bool)

        def process_alice(node, step, income):
            if node in bob_path:
                if step < bob_path[node]:
                    income += amount[node]
                elif step == bob_path[node]:
                    income += amount[node] // 2
            else:
                income += amount[node]

            explore = False
            for nxt in dicts[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    explore = True
                    process_alice(nxt, step + 1, income)

            if not explore:
                self.ans = max(self.ans, income)

        visited[0] = True
        process_alice(0, 0, 0)
        return self.ans


edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]

edges = [[0,1]]
bob = 1
amount = [-7280,2350]

edges = [[0,4],[4,2],[4,3],[3,1]]
bob = 3
amount = [-2,4,2,-4,6]

solution = Solution()
print(solution.mostProfitablePath(edges, bob, amount))
