class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        L = len(colors)

        segments = list()
        for idx, color in enumerate(colors):
            if idx == 0:
                curr = (idx, color)
                segment = list()
                segment.append(idx)
            else:
                prev = curr
                curr = (idx, color)
                if prev[1] != curr[1]:
                    segments.append(segment)
                    segment = list()
                    segment.append(idx)
                else:
                    segment.append(idx)
        segments.append(segment)

        ans = 0
        for segment in segments:
            maxi = 0
            for idx in segment:
                maxi = max(maxi, neededTime[idx])
            ans += maxi
        ans = sum(neededTime) - ans
        return ans


colors = "abaac"
neededTime = [1,2,3,4,5]

colors = "abc"
neededTime = [1,2,3]

colors = "aabaa"
neededTime = [1,2,3,4,1]


colors = "aaaaa"
neededTime = [1,2,3,4,1]

colors = "a"
neededTime = [2]

solution = Solution()
print(solution.minCost(colors, neededTime))
