class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        MAGIC = 5000

        def serve(n1, n2):
            key = str(n1) + "-" + str(n2)
            if key in self.cache:
                return self.cache[key]

            if n1 <= 0 and n2 > 0:
                return 1, 0, 0
            elif n1 > 0 and n2 <= 0:
                return 0, 1, 0
            elif n1 <= 0 and n2 <= 0:
                return 0, 0, 1

            case1 = serve(n1 - 100, n2)
            case2 = serve(n1 - 75, n2 - 25)
            case3 = serve(n1 - 50, n2 - 50)
            case4 = serve(n1 - 25, n2 - 75)

            A_win = 0.25 * (case1[0] + case2[0] + case3[0] + case4[0])
            B_win = 0.25 * (case1[1] + case2[1] + case3[1] + case4[1])
            draw = 0.25 * (case1[2] + case2[2] + case3[2] + case4[2])

            self.cache[key] = (A_win, B_win, draw)
            return A_win, B_win, draw

        from collections import  defaultdict
        self.cache = defaultdict(tuple)

        if n > MAGIC:
            return 1.0

        A_win, B_win, draw = serve(n, n)
        return A_win + 0.5 * draw


n = 50
n = 100

solution = Solution()
print(solution.soupServings(n))

