class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        from heapq import heapify, heappush, heappop
        s = sum(target)
        heap = [-1 * _ for _ in target]
        heapify(heap)

        while True:
            m = -1 * heappop(heap)
            s -= m
            # m == 1 : all 1s
            # s == 1 : [1, x] case
            if m == 1 or s == 1:
                return True
            # s = 0 : [x] and x != 1 case
            # s > m : sum of rest larger than max item case
            # m % s == 0 : the max item is a multiple of sum of rest
            if s == 0 or s > m or m % s == 0:
                return False
            r = m % s
            heappush(heap, r * -1)
            s += r
        return False


target = [9,3,5]
#target = [1,1,1,2]
#target = [8,5]
target = [9,9,9]
target = [1,1000000000]

solution = Solution()
print(solution.isPossible(target))
