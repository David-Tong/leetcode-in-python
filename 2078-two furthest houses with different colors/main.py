class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        # pre-process
        L = len(colors)
        from collections import defaultdict
        dicts = defaultdict(list)
        for idx, color in enumerate(colors):
            dicts[color].append(idx)

        # process
        ans = 0
        for color in dicts:
            mini, maxi = dicts[color][0], 0
            for other in dicts:
                if color != other:
                    maxi = max(maxi, dicts[other][-1])
            ans = max(ans, maxi - mini)
        return ans


colors = [1,1,1,6,1,1,1]
colors = [1,8,3,8,3]
colors = [0,1]
colors = [1,2,1,1,1,1,1]
colors = [1,2,1,1,1,1,2]

solution = Solution()
print(solution.maxDistance(colors))
