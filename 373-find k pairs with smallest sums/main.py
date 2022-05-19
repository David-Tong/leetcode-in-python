class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        M = len(nums1)
        N = len(nums2)

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        visited = set()
        pair = (nums1[0] + nums2[0], (0, 0))
        heappush(heap, pair)
        visited.add((0, 0))
        anses = list()
        while k > 0:
            if heap:
                _, (idx1, idx2) = heappop(heap)
            else:
                break
            anses.append((nums1[idx1], nums2[idx2]))
            if idx1 + 1 < M and idx2 < N:
                if (idx1 + 1, idx2) not in visited:
                    pair1 = (nums1[idx1 + 1] + nums2[idx2], (idx1 + 1, idx2))
                    heappush(heap, pair1)
                    visited.add((idx1 + 1, idx2))
            if idx1 < M and idx2 + 1 < N:
                if (idx1, idx2 + 1) not in visited:
                    pair2 = (nums1[idx1] + nums2[idx2 + 1], (idx1, idx2 + 1))
                    heappush(heap, pair2)
                    visited.add((idx1, idx2 + 1))
            k -= 1

        return anses


nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2

nums1 = [1,2]
nums2 = [3]
k = 3

nums1 = [1]
nums2 = [3]
k = 3

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10

solution = Solution()
print(solution.kSmallestPairs(nums1, nums2, k))


