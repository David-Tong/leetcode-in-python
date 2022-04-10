class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.anses = []
        def doRestore(s, selected):
            if len(selected) > 4:
                return

            if len(s) == 0:
                if len(selected) == 4:
                    self.anses.append(".".join(selected))
                return

            doRestore(s[1:], selected + [s[0]])
            if len(s) > 1:
                if s[0] != "0":
                    doRestore(s[2:], selected + [s[0:2]])
            if len(s) > 2:
                if s[0] != "0" and int(s[0:3]) <= 255:
                    doRestore(s[3:], selected + [s[0:3]])

        doRestore(s, [])
        return self.anses


s = "25525511135"
s = "0000"
s = "101023"

solution = Solution()
print(solution.restoreIpAddresses(s))
