class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # pre-process
        L = len(blocks)
        recolors = 0
        for x in range(k):
            if blocks[x] == "W":
                recolors += 1

        # process
        ans = recolors
        for x in range(k, L):
            if blocks[x] == "W" and blocks[x - k] == "B":
                recolors += 1
            elif blocks[x] == "B" and blocks[x - k] == "W":
                recolors -= 1
            ans = min(ans, recolors)
        return ans


blocks = "WBBWWBBWBW"
k = 7

blocks = "WBWBBBW"
k = 2

blocks = "WWWWWWWWWWWW"
k = 5

solution = Solution()
print(solution.minimumRecolors(blocks, k))
