class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        L = len(books)

        # dp init
        # dp[x] - the minimal possible height after placing books[:x+1]
        dp = [float("inf")] * L
        dp[0] = books[0][1]

        # dp transfer
        for x in range(1, L):
            width = 0
            height = 0
            for y in range(x, -1, -1):
                if width + books[y][0] <= shelfWidth:
                    width += books[y][0]
                    height = max(height, books[y][1])
                    if y - 1 >= 0:
                        dp[x] = min(dp[x], height + dp[y - 1])
                    else:
                        dp[x] = min(dp[x], height)
                else:
                    break
        return dp[L - 1]


books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4

books = [[1,3],[2,4],[3,2]]
shelfWidth = 6

solution = Solution()
print(solution.minHeightShelves(books, shelfWidth))
