class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        import string

        def getSubstrings(ss):
            L = len(ss)

            from collections import defaultdict
            substrings = defaultdict(int)
            for x in range(L):
                for y in range(L - x):
                    substrings[ss[x: x + y + 1]] += 1
            return substrings

        sources = getSubstrings(s)
        targets = getSubstrings(t)

        ans = 0
        for source in sources:
            for x in range(len(source)):
                for y in string.ascii_lowercase:
                    if source[x] != y:
                        target = source[:x] + y + source[x+1:]
                        if target in targets:
                            ans += sources[source] * targets[target]
        return ans


s = "aba"
t = "baba"

s = "ab"
t = "bb"

s = "abdiyewjwefjewojfiwejfiwijdijdiewjedijewiwejdiwjiwesalllpppsdwqoopjqidnsdyewuuuwefhuewfuewfhewfuhewu"
t = "fijwfewiwefjfwihiwefhweppwpqpqpqppqpdpdwqdkwejfiwejdiwejidwjdjdwidjiwjjadqwyqwdgtwcwddwdqqqqqwudhuwq"

solution = Solution()
print(solution.countSubstrings(s, t))
