class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        width = 0
        space = []
        lines = []
        line = []
        # arrange words by line
        for word in words:
            if width + len(word) > maxWidth:
                space.append(maxWidth - width + len(line))
                width = 0
                lines.append(line[:])
                line = []
            width += len(word) + 1
            line.append(word)

        if len(line) > 0:
            space.append(maxWidth - width + len(line))
            lines.append(line[:])

        # arrange line by rule
        anses = []
        for idx, line in enumerate(lines):
            if idx == len(lines) - 1 or len(line) == 1:
                ans = ""
                for word in line:
                    ans += word + " "
                ans = ans[:-1]
                ans += " " * (maxWidth - len(ans))
                anses.append(ans)
            else:
                div = space[idx] // (len(line) - 1)
                mod = space[idx] % (len(line) - 1)
                spaces = [" " * div] * (len(line) - 1) + [""]
                for x in range(mod):
                    spaces[x] += " "
                ans = ""
                for idx2, word in enumerate(line):
                    ans += word + spaces[idx2]
                anses.append(ans)
        return anses


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

#words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
#maxWidth = 16

solution = Solution()
print(solution.fullJustify(words, maxWidth))
