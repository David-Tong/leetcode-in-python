class Solution(object):
    def generateTag(self, caption):
        """
        :type caption: str
        :rtype: str
        """
        # process
        caption = caption.title().lstrip()
        if caption == "":
            return ""
        caption = caption[0].lower() + caption[1:]
        processed = "#"

        # rule 1
        for cap in caption:
            processed += cap

        # rule 2
        import string
        ans = "#"
        for c in processed:
            if c in string.ascii_letters:
                ans += c

        # rule 3
        ans = ans[:100]
        return ans


caption = "Leetcode daily streak achieved"
caption = "can I Go There"

solution = Solution()
print(solution.generateTag(caption))
