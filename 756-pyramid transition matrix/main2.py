class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # pre-process
        L = len(bottom)
        pyramid = [[''] * L for _ in range(L)]
        for y in range(L):
            pyramid[0][y] = bottom[y]
        # print(pyramid)

        from collections import defaultdict
        dicts = defaultdict(list)
        for allow in allowed:
            dicts[allow[:2]].append(allow[2])
        # print(dicts)

        # process
        def dfs(row, col, pyramid):
            if row == L:
                return True
            elif col == L - row:
                return dfs(row + 1, 0, pyramid)
            else:
                key = "{}{}".format(pyramid[row - 1][col], pyramid[row - 1][col + 1])
                for value in dicts[key]:
                    pyramid[row][col] = value
                    if dfs(row, col + 1, pyramid):
                        return True
                return False

        return dfs(1, 0, pyramid)


bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]

bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]

bottom = "ABBBBA"
allowed = ["ACA","ACF","ACE","ACD","ABA","ABF","ABE","ABD","FCA","FCF","FCE","FCD","FBA","FBF","FBE","FBD","ECA","ECF","ECE","ECD","EBA","EBF","EBE","EBD","DCA","DCF","DCE","DCD","DBA","DBF","DBE","DBD","CAA","CAF","CAE","CAD","CFA","CFF","CFE","CFD","CEA","CEF","CEE","CED","CDA","CDF","CDE","CDD","BAA","BAF","BAE","BAD","BFA","BFF","BFE","BFD","BEA","BEF","BEE","BED","BDA","BDF","BDE","BDD","CCA","CCF","CCE","CCD","CBA","CBF","CBE","CBD","BCA","BCF","BCE","BCD","BBA","BBF","BBE","BBD","CCC","CCB","CBC","CBB","BCC","BCB","BBC","BBB"]

solution = Solution()
print(solution.pyramidTransition(bottom, allowed))
