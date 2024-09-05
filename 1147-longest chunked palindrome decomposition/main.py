class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        def doDecomposition(text, count):
            L = len(text)
            middle = L / 2 + 1
            for x in range(1, middle):
                #print("text - {}, text2 - {}".format(text[:x], text[L - x:]))
                if text[:x] == text[L - x:]:
                    doDecomposition(text[x:L - x], count + 2)
                    return
            if L == 0:
                self.ans = count
            else:
                self.ans = count + 1

        doDecomposition(text, 0)
        return self.ans


text = "ghiabcdefhelloadamhelloabcdefghi"
#text = "merchant"
#text = "antaprezatepzapreanta"
#text = "aaa"
text = "elvtoelvto"

solution = Solution()
print(solution.longestDecomposition(text))
