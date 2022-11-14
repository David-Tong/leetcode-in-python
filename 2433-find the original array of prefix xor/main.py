class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        ans = list()
        for idx, x in enumerate(pref):
            if idx == 0:
                ans.append(x)
            else:
                ans.append(pref[idx - 1] ^ pref[idx])
        return ans


pref = [5,2,0,3,1]
pref = [13]
pref = [15000, 200, 1, 2, 4, 54667, 28]

solution = Solution()
print(solution.findArray(pref))
