class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        # pre-process
        L = len(bottom)

        # helper function
        def convert(ch):
            return str(ord(ch) - ord('A'))

        last = ""
        for y in range(L):
            last += convert(bottom[y])
        # print(last)

        from collections import defaultdict
        dicts = defaultdict(list)
        for allow in allowed:
            key = "{}{}".format(convert(allow[0]), convert(allow[1]))
            dicts[key].append(convert(allow[2]))
        # print(dicts)

        # process
        self.cache = defaultdict(bool)
        def dfs(row, col, last, current):
            cache_key = "{}-{}-{}-{}".format(row, col, last, current)
            if cache_key in self.cache:
                return self.cache[cache_key]

            if row == L:
                return True
            elif col == L - row:
                return dfs(row + 1, 0, current, "")
            else:
                key = last[col: col + 2]
                for value in dicts[key]:
                    if dfs(row, col + 1, last, current + value):
                        self.cache[cache_key] = True
                        return True
                self.cache[cache_key] = False
                return False

        return dfs(1, 0, last, "")


bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]

bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]

bottom = "ABBBBA"
allowed = ["ACA","ACF","ACE","ACD","ABA","ABF","ABE","ABD","FCA","FCF","FCE","FCD","FBA","FBF","FBE","FBD","ECA","ECF","ECE","ECD","EBA","EBF","EBE","EBD","DCA","DCF","DCE","DCD","DBA","DBF","DBE","DBD","CAA","CAF","CAE","CAD","CFA","CFF","CFE","CFD","CEA","CEF","CEE","CED","CDA","CDF","CDE","CDD","BAA","BAF","BAE","BAD","BFA","BFF","BFE","BFD","BEA","BEF","BEE","BED","BDA","BDF","BDE","BDD","CCA","CCF","CCE","CCD","CBA","CBF","CBE","CBD","BCA","BCF","BCE","BCD","BBA","BBF","BBE","BBD","CCC","CCB","CBC","CBB","BCC","BCB","BBC","BBB"]

solution = Solution()
print(solution.pyramidTransition(bottom, allowed))
