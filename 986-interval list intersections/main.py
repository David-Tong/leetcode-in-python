class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        idx = 0
        idx2 = 0
        anses = []
        while idx < len(firstList) and idx2 < len(secondList):
            if firstList[idx][1] <= secondList[idx2][1]:
                if firstList[idx][1] >= secondList[idx2][0]:
                    anses.append([max(firstList[idx][0], secondList[idx2][0]), firstList[idx][1]])
                idx += 1
            else:
                if firstList[idx][0] <= secondList[idx2][1]:
                    anses.append([max(firstList[idx][0], secondList[idx2][0]), secondList[idx2][1]])
                idx2 += 1
        return anses


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

firstList = [[1,3],[5,9]]
secondList = []

firstList = [[0,2],[5,10],[13,23],[24,26]]
secondList = [[1,24],[25,26]]

solution = Solution()
print(solution.intervalIntersection(firstList, secondList))
