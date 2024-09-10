class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        head2str = [set() for _ in range(26)]
        for idea in ideas:
            head2str[ord(idea[0]) - ord('a')].add(idea[1:])

        ans = 0
        for x in range(26):
            for y in range(x + 1, 26):
                k = len(head2str[x] & head2str[y])
                ans += (len(head2str[x]) - k) * (len(head2str[y]) - k) * 2
        return ans


ideas = ["coffee","donuts","time","toffee"]
ideas = ["lack","back"]

solution = Solution()
print(solution.distinctNames(ideas))
