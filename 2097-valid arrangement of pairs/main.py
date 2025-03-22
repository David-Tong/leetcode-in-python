class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        # pre-process
        from collections import defaultdict
        ingress, outgress = defaultdict(int), defaultdict(int)
        paths = defaultdict(list)
        for pair in pairs:
            start, end = pair
            ingress[end] += 1
            outgress[start] += 1
            paths[start].append(end)
        # print(paths)

        # euler path or euler circuit
        # if we only one node with in degree just one more than out degree
        #   and only one node with out degree only one more than in degree
        # and all other nodes with equal in degree and out degree
        # it is an euler path
        # if all nodes with equal in degree and out degree, it is euler circuit
        start = paths.keys()[0]
        for node in paths:
            if outgress[node] - ingress[node] == 1:
                start = node

        # process
        # dfs
        def dfs(node, path):
            print(node, path)
            # the path to the end node will be explored first, if it exist
            while paths[node]:
                nnode = paths[node].pop()
                dfs(nnode, path)
            path.append(node)

        path = list()
        dfs(start, path)
        path = path[::-1]

        # post process
        ans = list()
        for x in range(len(path) - 1):
            ans.append([path[x], path[x + 1]])
        return ans


pairs = [[5,1],[4,5],[11,9],[9,4]]
pairs = [[1,3],[3,2],[2,1]]
pairs = [[1,2],[1,3],[2,1]]
pairs = [[1,2]]
pairs = [[8,1],[1,3],[3,1],[1,6],[6,7],[7,1],[1,2],[2,4],[4,2],[2,9]]
pairs = [[8,1],[1,2],[1,3],[3,1],[1,6],[6,7],[7,1],[2,4],[4,2],[2,9]]

solution = Solution()
print(solution.validArrangement(pairs))
