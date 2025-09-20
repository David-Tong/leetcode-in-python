class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        # pre-process
        L = len(indices)
        chs = [''] * L

        # process
        for x in range(L):
            chs[indices[x]] = s[x]
        print(chs)
        ans = "".join(chs)
        return ans


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

"""
s = "abc"
indices = [0,1,2]
"""

solution = Solution()
print(solution.restoreString(s, indices))
