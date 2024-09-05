class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        # pre-process
        seats = list()
        for idx, crd in enumerate(corridor):
            if crd == "S":
                seats.append(idx)

        L = len(seats)
        if L == 0 or L % 2 == 1:
            return 0

        ways = list()
        for x in range(1, L, 2):
            if x + 1 < L:
                ways.append(seats[x + 1] - seats[x])

        # process
        ans = 1
        for way in ways:
            ans *= way
        ans = ans % MODULO
        return ans


corridor = "SSPPSPS"
corridor = "SSPPSPSPPP"
corridor = "PPSPSP"
corridor = "S"
corridor = "SSPPPPSPPSPSPSPSPSPSPSPSPSPPPPPSSSSPPSS"

solution = Solution()
print(solution.numberOfWays(corridor))
