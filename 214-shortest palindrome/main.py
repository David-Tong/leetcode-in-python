class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)
        length = L
        middle = length / 2
        borrow = 0

        rstart = length - middle
        lstart = middle - 1 - borrow
        range = lstart + 1

        while lstart >= 0:
            if s[:lstart + 1][::-1] == s[rstart: rstart + range]:
                return s[rstart + range:][::-1] + s

            length += 1
            borrow += 1
            middle = length / 2

            rstart = L - middle
            lstart = middle - 1 - borrow
            range = lstart + 1

        return s[1:][::-1] + s


s = "aacecaaa"
s = "abcd"
s = "axxd"
s = "dxxxa"

solution = Solution()
print(solution.shortestPalindrome(s))
