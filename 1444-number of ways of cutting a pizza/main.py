class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        M = len(pizza)
        N = len(pizza[0])

        # setup cache
        from collections import defaultdict
        cache = defaultdict(int)

        def findStart(x, y, vertical):
            if vertical:
                for start_y in range(y, N):
                    for start_x in range(x, M):
                        if pizza[start_x][start_y] == 'A':
                            return start_y
            else:
                for start_x in range(x, M):
                    for start_y in range(y, N):
                        if pizza[start_x][start_y] == 'A':
                            return start_x

        def hasApple(x, y):
            for next_x in range(x, M):
                for next_y in range(y, N):
                    if pizza[next_x][next_y] == 'A':
                        return True
            return False

        # x - the row index
        # y - the column index
        # n - the number of pieces
        def doWays(x, y, n):
            if n == k:
                if hasApple(x, y):
                    return 1
                else:
                    return 0

            key = str(x) + "_" + str(y) + "_" + str(n)
            if key in cache:
                return cache[key]

            ways = 0
            # do vertical cuts
            start_y = findStart(x, y, True)
            if start_y is not None:
                for next_y in range(start_y + 1, N):
                    ways += doWays(x, next_y, n + 1)

            # do horizontal cuts
            start_x = findStart(x, y, False)
            if start_x is not None:
                for next_x in range(start_x + 1, M):
                    ways += doWays(next_x, y, n + 1)

            cache[key] = ways
            return ways

        ans = doWays(0, 0, 1) % MODULO
        return ans


pizza = ["A..","AAA","..."]
k = 3

pizza = ["A..","AA.","..."]
k = 3

pizza = ["A..","A..","..."]
k = 1

pizza = [".A.","...","AAA"]
k = 3


pizza = [".A..A","A.A..","A.AA.","AAAA.","A.AA."]
k = 5

pizza = [
  "..A.A.AAA...AAAAAA.AA..A..A.A......A.AAA.AAAAAA.AA",
  "A.AA.A.....AA..AA.AA.A....AAA.A........AAAAA.A.AA.",
  "A..AA.AAA..AAAAAAAA..AA...A..A...A..AAA...AAAA..AA",
  "....A.A.AA.AA.AA...A.AA.AAA...A....AA.......A..AA.",
  "AAA....AA.A.A.AAA...A..A....A..AAAA...A.A.A.AAAA..",
  "....AA..A.AA..A.A...A.A..AAAA..AAAA.A.AA..AAA...AA",
  "A..A.AA.AA.A.A.AA..A.A..A.A.AAA....AAAAA.A.AA..A.A",
  ".AA.A...AAAAA.A..A....A...A.AAAA.AA..A.AA.AAAA.AA.",
  "A.AA.AAAA.....AA..AAA..AAAAAAA...AA.A..A.AAAAA.A..",
  "A.A...A.A...A..A...A.AAAA.A..A....A..AA.AAA.AA.AA.",
  ".A.A.A....AAA..AAA...A.AA..AAAAAAA.....AA....A....",
  "..AAAAAA..A..A...AA.A..A.AA......A.AA....A.A.AAAA.",
  "...A.AA.AAA.AA....A..AAAA...A..AAA.AAAA.A.....AA.A",
  "A.AAAAA..A...AAAAAAAA.AAA.....A.AAA.AA.A..A.A.A...",
  "A.A.AA...A.A.AA...A.AA.AA....AA...AA.A..A.AA....AA",
  "AA.A..A.AA..AAAAA...A..AAAAA.AA..AA.AA.A..AAAAA..A",
  "...AA....AAAA.A...AA....AAAAA.A.AAAA.A.AA..AA..AAA",
  "..AAAA..AA..A.AA.A.A.AA...A...AAAAAAA..A.AAA..AA.A",
  "AA....AA....AA.A......AAA...A...A.AA.A.AA.A.A.AA.A",
  "A.AAAA..AA..A..AAA.AAA.A....AAA.....A..A.AA.A.A...",
  "..AA...AAAAA.A.A......AA...A..AAA.AA..A.A.A.AA..A.",
  ".......AA..AA.AAA.A....A...A.AA..A.A..AAAAAAA.AA.A",
  ".A.AAA.AA..A.A.A.A.A.AA...AAAA.A.A.AA..A...A.AAA..",
  "A..AAAAA.A..A..A.A..AA..A...AAA.AA.A.A.AAA..A.AA..",
  "A.AAA.A.AAAAA....AA..A.AAA.A..AA...AA..A.A.A.AA.AA",
  ".A..AAAA.A.A.A.A.......AAAA.AA...AA..AAA..A...A.AA",
  "A.A.A.A..A...AA..A.AAA..AAAAA.AA.A.A.A..AA.A.A....",
  "A..A..A.A.AA.A....A...A......A.AA.AAA..A.AA...AA..",
  ".....A..A...A.A...A..A.AA.A...AA..AAA...AA..A.AAA.",
  "A...AA..A..AA.A.A.AAA..AA..AAA...AAA..AAA.AAAAA...",
  "AA...AAA.AAA...AAAA..A...A..A...AA...A..AA.A...A..",
  "A.AA..AAAA.AA.AAA.A.AA.A..AAAAA.A...A.A...A.AA....",
  "A.......AA....AA..AAA.AAAAAAA.A.AA..A.A.AA....AA..",
  ".A.A...AA..AA...AA.AAAA.....A..A..A.AA.A.AA...A.AA",
  "..AA.AA.AA..A...AA.AA.AAAAAA.....A.AA..AA......A..",
  "AAA..AA...A....A....AA.AA.AA.A.A.A..AA.AA..AAA.AAA",
  "..AAA.AAA.A.AA.....AAA.A.AA.AAAAA..AA..AA.........",
  ".AA..A......A.A.AAA.AAAA...A.AAAA...AAA.AAAA.....A",
  "AAAAAAA.AA..A....AAAA.A..AA.A....AA.A...A.A....A..",
  ".A.A.AA..A.AA.....A.A...A.A..A...AAA..A..AA..A.AAA",
  "AAAA....A...A.AA..AAA..A.AAA..AA.........AA.AAA.A.",
  "......AAAA..A.AAA.A..AAA...AAAAA...A.AA..A.A.AA.A.",
  "AA......A.AAAAAAAA..A.AAA...A.A....A.AAA.AA.A.AAA.",
  ".A.A....A.AAA..A..AA........A.AAAA.AAA.AA....A..AA",
  ".AA.A...AA.AAA.A....A.A...A........A.AAA......A...",
  "..AAA....A.A...A.AA..AAA.AAAAA....AAAAA..AA.AAAA..",
  "..A.AAA.AA..A.AA.A...A.AA....AAA.A.....AAA...A...A",
  ".AA.AA...A....A.AA.A..A..AAA.A.A.AA.......A.A...A.",
  "...A...A.AA.A..AAAAA...AA..A.A..AAA.AA...AA...A.A.",
  "..AAA..A.A..A..A..AA..AA...A..AA.AAAAA.A....A..A.A"
]
k = 8

solution = Solution()
print(solution.ways(pizza, k))
