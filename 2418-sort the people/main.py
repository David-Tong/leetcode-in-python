class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # pre-process
        pairs = zip(names, heights)
        pairs = sorted(pairs, key=lambda x: -x[1])

        # process
        ans = list()
        for pair in pairs:
            ans.append(pair[0])
        return ans


names = ["Mary","John","Emma"]
heights = [180,165,170]

names = ["Alice","Bob","Bob"]
heights = [155,185,150]

solution = Solution()
print(solution.sortPeople(names, heights))
