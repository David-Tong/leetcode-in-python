class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        # process
        ans = list()
        for word in words:
            ws = word.split(separator)
            for w in ws:
                if w != "":
                    ans.append(w)
        return ans


words = ["one.two.three","four.five","six"]
separator = "."

words = ["$easy$","$problem$"]
separator = "$"

words = ["|||"]
separator = "|"

solution = Solution()
print(solution.splitWordsBySeparator(words, separator))
