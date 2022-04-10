class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        def isValid(citations, index):
            if N - index <= citations[index]:
                return True
            else:
                return False

        left = 0
        right = N - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if isValid(citations, middle):
                right = middle
            else:
                left = middle

        if isValid(citations, left):
            return N - left
        elif isValid(citations, right):
            return N - right
        else:
            return 0


citations = [0,1,3,5,6]
citations = [1,2,100]
#citations = [0,0,0,0,0]
#citations = [5,5,5,5,5]
#citations = [100]

solution = Solution()
print(solution.hIndex(citations))
