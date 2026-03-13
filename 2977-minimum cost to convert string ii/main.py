class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        # pre-process
        M = len(source)
        N = len(original)

        from collections import defaultdict
        dicts = defaultdict(int)
        idx = 0
        for vertex in original:
            if vertex not in dicts:
                dicts[vertex] = idx
                idx += 1
        for vertex in changed:
            if vertex not in dicts:
                dicts[vertex] = idx
                idx += 1
        # print(dicts)

        # initialize distance matrix
        V = len(dicts)
        distances = [[float("inf")] * V for _ in range(V)]
        for z in range(V):
            distances[z][z] = 0
        for z in range(N):
            x = dicts[original[z]]
            y = dicts[changed[z]]
            distances[x][y] = min(distances[x][y], cost[z])

        # run floyd algorithm
        for z in range(V):
            for x in range(V):
                for y in range(V):
                    distances[x][y] = min(distances[x][y], distances[x][z] + distances[z][y])
        # print(distances)

        # process
        # dp init
        # dp[x] - the minimum cost to covert string source[:x] to string target[:x]
        dp = [float("inf")] * (M + 1)
        dp[0] = 0

        # dp transfer
        # case 1 : if source[x - 1] == target[x - 1]
        # dp[x] = dp[x - 1]
        # case 2 : if source[y:x] can be converted to target[y:x] with the cost
        # dp[x] - min(dp[x], dp[y] + cost)
        for x in range(1, M + 1):
            if source[x - 1] == target[x - 1]:
                dp[x] = dp[x - 1]
            for y in range(x):
                s = source[y: x]
                t = target[y: x]
                if s in dicts and t in dicts:
                    idx_s, idx_t = dicts[s], dicts[t]
                    if distances[idx_s][idx_t] != float("inf"):
                        cost = distances[idx_s][idx_t]
                        dp[x] = min(dp[x], dp[y] + cost)

        # post-process
        if dp[M] == float("inf"):
            ans = -1
        else:
            ans = dp[M]
        return ans


source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]

source = "abcdefgh"
target = "acdeeghh"
original = ["bcd","fgh","thh"]
changed = ["cde","thh","ghh"]
cost = [1,3,5]

source = "abcdefgh"
target = "addddddd"
original = ["bcd","defgh"]
changed = ["ddd","ddddd"]
cost = [100,1578]

solution = Solution()
print(solution.minimumCost(source, target, original, changed, cost))
