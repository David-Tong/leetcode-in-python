class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        L = len(s)
        questions = list()
        start = -1
        for idx, ch in enumerate(s):
            if ch == "?":
                if start == -1:
                    start = idx
            else:
                if start != -1:
                    outs = list()
                    if start > 0:
                        outs.append(s[start - 1])
                    outs.append(s[idx])
                    questions.append((start, idx, outs))
                    start = -1
        if start != -1:
            outs = list()
            if start > 0:
                outs.append(s[start - 1])
            questions.append((start, L, outs))

        # process
        ans = list(s)
        for question in questions:
            start, end, outs = question[0], question[1], question[2]
            idx = 0
            for x in range(start, end):
                ch = chr(ord('a') + idx)
                while ch in outs:
                    ch = chr(ord('a') + idx)
                    idx += 1
                ans[x] = ch
                idx = (idx + 1) % 26
        return "".join(ans)


s = "?zs"
s = "ubv?w"
s = "a??????????a"
s = "a????????????????????????????????????????????????????????????????????????????????????????a"
s = "?????"
s = "????a???b???c"
s = "?????a????"
s = "a?"

solution = Solution()
print(solution.modifyString(s))