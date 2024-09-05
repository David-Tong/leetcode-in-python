class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        N = len(piles)

        def take(idx, M, step):
            key = str(idx) + "-" + str(M) + "-" + str(step)
            if key in self.cache:
                return self.cache[key]

            if idx >= N:
                return 0, 0

            alice_max_stones = 0
            bob_max_stones = 0
            for x in range(1, 2 * M + 1):
                alice_stones, bob_stones = take(idx + x, min(N // 2 + 1, max(M, x)), step + 1)
                if step % 2 == 0:
                    if alice_stones + sum(piles[idx: idx + x]) > alice_max_stones:
                        alice_max_stones = alice_stones + sum(piles[idx: idx + x])
                        bob_max_stones = bob_stones
                else:
                    if bob_stones + sum(piles[idx: idx + x]) > bob_max_stones:
                        alice_max_stones = alice_stones
                        bob_max_stones = bob_stones + sum(piles[idx: idx + x])
            self.cache[key] = (alice_max_stones, bob_max_stones)
            return alice_max_stones, bob_max_stones

        from collections import defaultdict
        self.cache = defaultdict(tuple)
        return take(0, 1, 0)[0]


piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]
piles = [1]
piles = [10,22,56,12,3,4,6,18,109,21,56]
piles = [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063,8023,7729,7084,8407]
piles = [806,6146,3503,3024,226,682,3500,4560,3346,5981,9508,2658,4984,9713,8485,1646,5321,4418,1940,7445,3769,7310,4776,9134,6821,6334,9889,312,8722,5894,9118,1911,8106,3068,6070,1117,5172,2852,2637,7477,8197,5091,3898,5198,707,8886,8312,4673,4884,8665,9476,433,1816,3462,756,1934,1506,314,6032,710,695,1958,6015,8588,7402,6375,390,5033,7510,6761,5549,5364,4206,7365,6484,6783,3151,9141,8986,9309,476,5697,7932,2165,655,7598,79]

solution = Solution()
print(solution.stoneGameII(piles))
