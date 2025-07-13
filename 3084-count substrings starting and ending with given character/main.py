class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        # pre-process
        count = 0
        for ch in s:
            if ch == c:
                count += 1

        # process
        if count >= 2:
            ans = count + count * (count - 1) // 2
        else:
            ans = count
        return ans


s = "abada"
c = "a"

s = "zzz"
c = "z"

s = "ab"
c = "a"

s = "a"
c = "b"

solution = Solution()
print(solution.countSubstrings(s, c))
