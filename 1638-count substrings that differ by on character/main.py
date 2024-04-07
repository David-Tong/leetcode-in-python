class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        import string

        M = len(s)
        sources = list()
        for x in range(M):
            for y in range(M - x):
                sources.append(s[x: x + y + 1])

        ans = 0
        for source in sources:
            print(source)
            for x in range(len(source)):
                for y in string.ascii_lowercase:
                    if y != source[x]:
                        target = source[:x] + y + source[x + 1:]
                        if target in t:
                            ans += 1
        return ans


s = "aba"
t = "baba"

solution = Solution()
print(solution.countSubstrings(s, t))
