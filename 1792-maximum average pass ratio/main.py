class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        # pre-process
        L = len(classes)
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for cls in classes:
            pas, total = cls
            inc = pas * 1.0 / total - (pas + 1) * 1.0 / (total + 1)
            heappush(heap, (inc, pas, total))
        # print(heap)

        # process
        for _ in range(extraStudents):
            inc, pas, total = heappop(heap)
            pas, total = pas + 1, total + 1
            inc = pas * 1.0 / total - (pas + 1) * 1.0 / (total + 1)
            heappush(heap, (inc, pas, total))
        # print(heap)

        total_ratio = 0
        while heap:
            _, pas, total = heappop(heap)
            total_ratio += (pas * 1.0) / total
        ans = (total_ratio * 1.0) / L
        return ans


classes = [[1,2],[3,5],[2,2]]
extraStudents = 2

classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4

solution = Solution()
print(solution.maxAverageRatio(classes, extraStudents))
