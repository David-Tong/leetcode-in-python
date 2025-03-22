class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        # pre-process
        L = len(boxes)
        balls = list()
        for idx, box in enumerate(boxes):
            if box == "1":
                balls.append(idx)

        # process
        ans = list()
        for x in range(L):
            moves = 0
            for ball in balls:
                moves += abs(ball - x)
            ans.append(moves)
        return ans


boxes = "110"
boxes = "001011"
boxes = "111111111"
boxes = "1" * 2000

solution = Solution()
print(solution.minOperations(boxes))
