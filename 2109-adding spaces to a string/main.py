class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        tokens = list()
        idx2 = 0
        for idx, ch in enumerate(s):
            if idx2 < len(spaces) and idx == spaces[idx2]:
                tokens.append(" " + ch)
                idx2 += 1
            else:
                tokens.append(ch)

        ans = "".join(tokens)
        return ans


s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

s = "icodeinpython"
spaces = [1,5,7,9]

s = "spacing"
spaces = [0,1,2,3,4,5,6]

solution = Solution()
print(solution.addSpaces(s, spaces))
