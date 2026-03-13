class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        # pre-process
        KEYS = ["&quot;", "&apos;", "&gt;", "&lt;", "&frasl;", "&amp;"]
        REPLACEMENTS = {
            "&quot;" : '"',
            "&apos;" : "'",
            "&gt;" : ">",
            "&lt;" : "<",
            "&frasl;" : "/",
            "&amp;": "&"
        }

        # process
        ans = text
        for key in KEYS:
            # print(key)
            ans = ans.replace(key, REPLACEMENTS[key])
            # print(ans)
        return ans


text = "&amp; is an HTML entity but &ambassador; is not."
text = "and I quote: &quot;...&quot;"
text = "&amp;quot;&amp;apos;&amp;amp;&amp;gt;&amp;lt;&amp;frasl;"

solution = Solution()
print(solution.entityParser(text))
