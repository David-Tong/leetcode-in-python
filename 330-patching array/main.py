class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        heap = [0] + nums[:]
        heapify(heap)

        subsum = 0
        item = 0
        count = 0
        while True:
            num = heappop(heap)
            subsum += num
            if subsum >= n:
                return count

            item = subsum + 1
            if heap:
                if item < heap[0]:
                    heappush(heap, item)
                    count += 1
            else:
                heappush(heap, item)
                count += 1


#nums = [1, 3]
#n = 6

#nums = [1,5,10]
#n = 20

#nums = [1,2,2]
#n = 5

nums = [1,17,64]
n = 300

nums = [1,1,2]
n = 300

nums = [1,1,1]
n = 300

nums = [2,4,14,18,20,25,25,35,73,94]
n = 42

#nums = [1,2,2,3,4,4,4,5,6,7,7,7,7,7,7,8,9,9,10,10,10,11,11,11,12,13,13,13,15,16,16,16,17,17,18,18,19,19,19,19,19,19,20,20,20,21,21,22,22,22,22,23,24,25,26,26,26,26,27,28,28,29,29,29,30,31,32,32,32,32,33,33,34,35,35,35,36,36,37,37,37,37,37,38,38,38,39,39,40,41,41,42,43,43,43,43,44,45,46,46,47,48,48,49,50,51,52,52,52,52,53,54,54,54,55,55,56,56,59,60,60,62,62,62,63,63,63,64,64,65,67,67,67,67,67,67,68,68,68,68,69,69,70,70,70,70,70,70,71,71,71,72,72,74,75,76,76,77,77,78,78,78,78,79,81,81,82,83,83,83,83,83,84,84,84,85,85,86,87,87,88,88,88,88,90,90,90,90,91,91,91,91,94,96,98,98,98,99,99,100]
#n = 10394

solution = Solution()
print(solution.minPatches(nums, n))
