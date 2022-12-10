class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = len(s)

        count = 0
        half = L // 2
        for idx, ch in enumerate(s):
            if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                if idx < half:
                    count += 1
                else:
                    count -= 1
                    if count < 0:
                        return False

        return True if count == 0 else False


s = "book"
s = "textbook"
s = "maamii"
s = "ae"

solution = Solution()
print(solution.halvesAreAlike(s))
