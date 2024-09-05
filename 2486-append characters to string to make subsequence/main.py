class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # pre-process
        M = len(s)
        N = len(t)

        # process
        idx = 0
        idx2 = 0
        while idx < M and idx2 < N:
            if s[idx] == t[idx2]:
                idx += 1
                idx2 += 1
            else:
                idx += 1

        ans = N - idx2
        return ans


s = "coaching"
t = "coding"

s = "abcde"
t = "a"

s = "z"
t = "abcde"

solution = Solution()
print(solution.appendCharacters(s, t))
