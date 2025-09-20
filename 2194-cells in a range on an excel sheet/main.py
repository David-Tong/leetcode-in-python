class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # pre-process
        start, end = s.split(":")
        sc, sd = ord(start[0]) - ord('A'), int(start[1])
        ec, ed = ord(end[0]) -ord('A'), int(end[1])

        # process
        ans = list()
        for x in range(sc, ec + 1):
            for y in range(sd, ed + 1):
                ch = chr(ord('A') + x)
                ans.append("{}{}".format(ch, y))
        return ans


s = "K1:L2"
s = "A1:F1"

solution = Solution()
print(solution.cellsInRange(s))
