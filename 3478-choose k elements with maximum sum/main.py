class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # pre-process
        L = len(nums1)
        from collections import defaultdict
        dicts = defaultdict(list)
        idxes = defaultdict(list)
        for x in range(L):
            dicts[nums1[x]].append(nums2[x])
            idxes[nums1[x]].append(x)

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        maxis = list()
        total = 0
        for num in sorted(dicts):
            for num2 in dicts[num]:
                heappush(heap, num2)
                total += num2
                while len(heap) > k:
                    sub = heappop(heap)
                    total -= sub
            maxis.append(total)

        # process
        ans = [0] * L
        for id, num in enumerate(sorted(dicts)):
            if id > 0:
                for idx in idxes[num]:
                    ans[idx] = maxis[id - 1]
        return ans


nums1 = [4,2,1,5,3]
nums2 = [10,20,30,40,50]
k = 2

nums1 = [4,2,1,5,3,2]
nums2 = [10,20,30,40,50,70]
k = 2

nums1 = [2,2,2,2]
nums2 = [3,1,2,3]
k = 1

nums1 = [_ for _ in range(10 ** 5)]
nums2 = [_ for _ in range(10 ** 5)]
k = 85001

solution = Solution()
print(solution.findMaxSum(nums1, nums2, k))
