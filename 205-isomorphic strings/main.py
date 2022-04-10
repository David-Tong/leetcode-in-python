class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def doIsomorphic(s, t):
            from collections import defaultdict
            dicts = defaultdict(str)

            for x in range(len(s)):
                if s[x] in dicts:
                    if t[x] != dicts[s[x]]:
                        return False
                else:
                    dicts[s[x]] = t[x]
            return True

        return doIsomorphic(s, t) & doIsomorphic(t, s)


s = "egg"
t = "add"

s = "foo"
t = "bar"

s = "paper"
t = "title"

solution = Solution()
print(solution.isIsomorphic(s, t))
