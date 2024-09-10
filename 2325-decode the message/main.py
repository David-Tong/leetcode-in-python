class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        # pre-process
        table = list()
        for c in key:
            if c not in table:
                if c != " ":
                    table.append(c)
            if len(table) == 26:
                break

        from collections import defaultdict
        cipher = defaultdict(str)
        for idx, c in enumerate(table):
            cipher[c] = chr(ord('a') + idx)

        # process
        ans = ""
        for c in message:
            if c == " ":
                ans += " "
            else:
                ans += cipher[c]
        return ans


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

solution = Solution()
print(solution.decodeMessage(key, message))
