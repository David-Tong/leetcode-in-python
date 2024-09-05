class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        ans = 0
        for stone in stones:
            if stone in jewels:
                ans += 1
        return ans


jewels = "aA"
stones = "aAAbbbb"

jewels = "z"
stones = "ZZ"

solution = Solution()
print(solution.numJewelsInStones(jewels, stones))
