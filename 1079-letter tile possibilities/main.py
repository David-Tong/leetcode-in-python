class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        # pre-process
        L = len(tiles)

        # process
        dotiles = set()
        # recursion function
        def doTile(selections, tile, n):
            if n == 0:
                if tile:
                    dotiles.add(tile)
            else:
                doTile(selections, tile, n - 1)
                for x in range(L):
                    if selections >> x & 1 == 0:
                        doTile(selections | 1 << x, tile + tiles[x], n - 1)
        doTile(0, "", L)

        # post-process
        ans = len(dotiles)
        return ans


tiles = "AAB"
tiles = "AAABBC"
tiles = "V"

solution = Solution()
print(solution.numTilePossibilities(tiles))
