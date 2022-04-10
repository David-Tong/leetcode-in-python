class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        citations = sorted(citations, reverse=True)
        for x in range(N):
            if citations[x] < x + 1:
                return x
        return N


citations = [3,0,6,1,5]
citations = [1,3,1]

solution = Solution()
print(solution.hIndex(citations))
