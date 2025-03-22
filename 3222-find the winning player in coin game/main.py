class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        y = y // 4
        times = min(x, y)
        return "Alice" if times % 2 == 1 else "Bob"


x = 2
y = 7

x = 4
y = 11

solution = Solution()
print(solution.winningPlayer(x, y))
