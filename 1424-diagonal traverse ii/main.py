class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        M = len(nums)

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for x in range(M):
            for y in range(len(nums[x])):
                heappush(heap, (x + y, y, x))

        # process
        ans = list()
        while heap:
            _, y, x = heappop(heap)
            ans.append(nums[x][y])
        return ans


nums = [[1,2,3],[4,5,6],[7,8,9]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12]]
nums = [[1,2,3,4,5],[6,7,8,9],[10,11,12],[13,14],[15]]
nums = [[1]]
nums = [[1,2,3,4,5,6]]

solution = Solution()
print(solution.findDiagonalOrder(nums))
