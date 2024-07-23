class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # pre-process
        L = len(piles) // 3
        piles = sorted(piles, reverse=True)

        # process
        idx = 1
        ans = 0
        for x in range(L):
            ans += piles[idx + 2 * x]
        return ans


piles = [2,4,1,2,7,8]
piles = [2,4,5]
piles = [9,8,7,6,5,1,2,3,4]

solution = Solution()
print(solution.maxCoins(piles))
