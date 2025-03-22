class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        # pre-process
        L = len(boxes)
        lefts = [0]
        total = 0
        balls = 0
        for x in range(1, L):
            total += balls
            if boxes[x - 1] == "1":
                total += 1
                balls += 1
            lefts.append(total)

        rights = [0]
        total = 0
        balls = 0
        for x in range(L - 2, -1, -1):
            total += balls
            if boxes[x + 1] == "1":
                total += 1
                balls += 1
            rights.append(total)
        rights = rights[::-1]

        # print(lefts)
        # print(rights)

        # process
        ans = []
        for x in range(L):
            ans.append(lefts[x] + rights[x])
        return ans


boxes = "110"
boxes = "001011"

solution = Solution()
print(solution.minOperations(boxes))
