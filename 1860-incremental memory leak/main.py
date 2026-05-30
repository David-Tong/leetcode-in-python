class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        # pre-process
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        heappush(heap, (memory1 * -1, 1))
        heappush(heap, (memory2 * -1, 2))

        # process
        request = 1
        head = heap[0][0] * -1
        while request <= head:
            memory, idx = heappop(heap)
            heappush(heap, (memory + request, idx))
            request += 1
            head = heap[0][0] * -1

        # post-process
        ans = [0] * 3
        ans[0] = request
        while heap:
            memory, idx = heappop(heap)
            ans[idx] = memory * -1
        return ans


memory1 = 2
memory2 = 2

memory1 = 8
memory2 = 11

memory1 = 2 ** 31 - 3
memory2 = 2 ** 31 - 1

print(memory1, memory2)

solution = Solution()
print(solution.memLeak(memory1, memory2))
