class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        # pre-process
        L = len(maxHeights) + 1

        # helper function
        def searchScores(heights):
            stack = list()
            scores = list()
            for idx, height in enumerate(heights):
                score = scores[-1] if scores else 0
                while stack and stack[-1][1] > height:
                    remove = stack[-1][1]
                    end = stack[-1][0]
                    stack.pop()
                    start = stack[-1][0] if stack else -1
                    score -= remove * (end - start)
                    score += height * (end - start)
                score += height
                scores.append(score)
                stack.append((idx, height))
            return scores

        # search from left to right
        lefts = [0] + searchScores(maxHeights)

        # search from right to left
        rights = searchScores(maxHeights[::-1])[::-1] + [0]

        # process
        ans = 0
        for idx in range(L):
            ans = max(ans, lefts[idx] + rights[idx])
        return ans


maxHeights = [5,3,4,1,1]
maxHeights = [6,5,3,9,2,7]
maxHeights = [3,2,5,5,2,3]
maxHeights = [3,2,5,3,5,2,3]
maxHeights = [3,2,5,3,4,5,2,3]
maxHeights = [5,2,4,4]

solution = Solution()
print(solution.maximumSumOfHeights(maxHeights))
