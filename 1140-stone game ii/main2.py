class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        N = len(piles)

        def take(idx, M):
            key = str(idx) + "-" + str(M)
            if key in self.cache:
                return self.cache[key]

            if idx >= N:
                return 0

            if idx + 2 * M >= N:
                return sum(piles[idx:])

            min_max = float("-inf")
            curr = 0
            for x in range(0, 2 * M):
                if idx + x < N:
                    curr += piles[idx + x]
                    min_max = max(min_max, curr - take(idx + x + 1, max(M, x + 1)))

            self.cache[key] = min_max
            return min_max

        from collections import defaultdict
        self.cache = defaultdict(int)

        total = sum(piles)
        ans = (total + take(0, 1)) / 2

        return ans


piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]
piles = [1]
piles = [10,22,56,12,3,4,6,18,109,21,56]
piles = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063,8023,7729,7084,8407]
piles = [806,6146,3503,3024,226,682,3500,4560,3346,5981,9508,2658,4984,9713,8485,1646,5321,4418,1940,7445,3769,7310,4776,9134,6821,6334,9889,312,8722,5894,9118,1911,8106,3068,6070,1117,5172,2852,2637,7477,8197,5091,3898,5198,707,8886,8312,4673,4884,8665,9476,433,1816,3462,756,1934,1506,314,6032,710,695,1958,6015,8588,7402,6375,390,5033,7510,6761,5549,5364,4206,7365,6484,6783,3151,9141,8986,9309,476,5697,7932,2165,655,7598,79]

solution = Solution()
print(solution.stoneGameII(piles))
