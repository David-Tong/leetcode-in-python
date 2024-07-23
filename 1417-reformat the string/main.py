import string


class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        # pre-process
        numbers = ""
        letters = ""
        for ch in s:
            if ch in string.ascii_lowercase:
                letters += ch
            else:
                numbers += ch

        if abs(len(numbers) - len(letters)) > 1:
            return ""

        if len(numbers) >= len(letters):
            first = numbers
            second = letters
        else:
            first = letters
            second = numbers

        # process
        ans = ""
        for x in range(len(second)):
            ans += first[x] + second[x]
        if len(numbers) != len(letters):
            ans += first[-1]
        return ans


s = "a0b1c2"
s = "leetcode"
s = "1229857369"
s = "abcc123"
s = "1234sdt"

solution = Solution()
print(solution.reformat(s))
