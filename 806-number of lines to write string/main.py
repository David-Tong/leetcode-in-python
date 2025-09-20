class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        # process
        W = 100
        line = 0
        characters = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            width = widths[idx]
            if characters + width > 100:
                characters = 0
                line += 1
            characters += width
        line += 1
        ans = [line, characters]
        return ans


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"

solution = Solution()
print(solution.numberOfLines(widths, s))
