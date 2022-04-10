class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)

        point = 0
        point2 = 0

        ans = 0
        while point < len(g) and point2 < len(s):
            if s[point2] >= g[point]:
                point2 += 1
                point += 1
                ans += 1
            else:
                point2 += 1
        return ans


g = [1,2,3]
s = [1,1]

g = [1,2]
s = [1,2,3]

solution = Solution()
print(solution.findContentChildren(g, s))
