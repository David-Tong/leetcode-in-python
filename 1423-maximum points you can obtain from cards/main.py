class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        L = len(cardPoints)
        M = L - k
        sumi = sum(cardPoints)

        if k >= L:
            return sumi

        ans = 0
        total = sum(cardPoints[:M])
        for x in range(L):
            if x + M > L:
                break
            if x > 0:
                total = total - cardPoints[x - 1] + cardPoints[x + M - 1]
            ans = max(ans, sumi - total)
        return ans


cardPoints = [1,2,3,4,5,6,1]
k = 3

#cardPoints = [2,2,2]
#k = 2

cardPoints = [9,7,7,9,7,7,9]
k = 7

cardPoints = [9,7,7,9,7,7,9]
k = 1

solution = Solution()
print(solution.maxScore(cardPoints, k))
