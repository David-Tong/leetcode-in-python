class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # pre-process
        L = len(stones)
        presum = [0]
        for stone in stones:
            presum.append(presum[-1] + stone)

        def stoneSum(x, y):
            return presum[y + 1] - presum[x]

        # dfs
        def game(x, y):
            if x >= y:
                return 0

            key = str(x) + "-" + str(y)
            if key not in self.cache:
                self.cache[key] = max(stoneSum(x + 1, y) - game(x + 1, y), stoneSum(x, y - 1) - game(x, y - 1))
            return self.cache[key]

        # cache
        from collections import defaultdict
        self.cache = defaultdict(int)

        return game(0, L - 1)


stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]

solution = Solution()
print(solution.stoneGameVII(stones))
