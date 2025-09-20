class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        # pre-process
        M = 10
        N = 3
        placements = [[0] * N for _ in range(M)]

        # helper function
        def colorize(color):
            if color == "R":
                return 0
            elif color == "G":
                return 1
            elif color == "B":
                return 2
            else:
                raise ValueError

        L = len(rings)
        for x in range(0, L, 2):
            color, rod = rings[x], int(rings[x + 1])
            placements[rod][colorize(color)] |= 1

        # print(placements)

        # process
        ans = 0
        for x in range(M):
            if sum(placements[x]) == 3:
                ans += 1
        return ans


rings = "B0B6G0R6R0R6G9"
rings = "B0R0G0R9R0B0G0"
rings = "G4"

solution = Solution()
print(solution.countPoints(rings))

