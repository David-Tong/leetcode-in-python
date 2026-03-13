class SegmentTree(object):
    def __init__(self, n):
        self.N = n
        self.maxis = [-1 for _ in range(self.N * 4)]

    def update(self, idx, val):
        self.__update(1, 0, self.N - 1, idx, val)

    def __update(self, pivot, left, right, idx, val):
        if left == right:
            self.maxis[pivot] = max(self.maxis[pivot], val)
            return

        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2
        if idx <= middle:
            self.__update(left_child, left, middle, idx, val)
        else:
            self.__update(right_child, middle + 1, right, idx, val)
        self.maxis[pivot] = max(val, self.maxis[pivot])

    def query(self, idx):
        return self.__query(1, 0, self.N - 1, idx)

    def __query(self, pivot, left, right, idx):
        if left == idx:
            return self.maxis[pivot]

        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2
        if idx <= middle:
            return max(self.__query(left_child, left, middle, idx), self.maxis[right_child])
        else:
            return self.__query(right_child, middle + 1, right, idx)


class Solution(object):
    def maximumSumQueries(self, nums1, nums2, queries):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        N = len(nums1)
        Q = len(queries)

        nums = list()
        idx = 0
        while idx < N:
            nums.append((nums1[idx], nums2[idx], nums1[idx] + nums2[idx], idx))
            idx += 1
        nums = sorted(nums, key=lambda x: x[0], reverse=True)
        nums1 = list(zip(*nums))[0]
        nums2 = list(zip(*nums))[1]
        maxis = list(zip(*nums))[2]

        """
        print(nums1)
        print(nums2)
        print(maxis)
        """

        # renormalize nums2
        processed_nums2 = sorted(list(set(nums2)))
        M = len(processed_nums2)
        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, num2 in enumerate(processed_nums2):
            dicts[num2] = idx

        for idx, query in enumerate(queries):
            query.append(idx)
        queries = sorted(queries, key=lambda x:x[0], reverse=True)
        # print(queries)

        # process
        from bisect import bisect_left
        st = SegmentTree(M)

        idx = 0
        idx2 = 0
        ans = [0] * Q
        while idx < Q:
            while idx2 < N and nums1[idx2] >= queries[idx][0]:
                num2 = nums2[idx2]
                num2_idx = dicts[num2]
                st.update(num2_idx, maxis[idx2])
                idx2 += 1
            # print(st.maxis)
            target = bisect_left(processed_nums2, queries[idx][1])
            # print(target)
            if target == M:
                ans[queries[idx][2]] = -1
            else:
                ans[queries[idx][2]] = st.query(target)
            idx += 1
        return ans


nums1 = [4,3,1,2]
nums2 = [2,4,9,5]
queries = [[4,1],[1,3],[2,5]]

nums1 = [3,2,5]
nums2 = [2,3,4]
queries = [[4,4],[3,2],[1,1]]

nums1 = [2,1]
nums2 = [2,3]
queries = [[3,3]]

from random import randint
nums1 = [randint(1,10 ** 5) for _ in range(10 ** 2)]
nums2 = [randint(1,10 ** 5) for _ in range(10 ** 2)]
queries = [[randint(1,10 ** 5), randint(1, 10 ** 5)] for _ in range(10 ** 2)]
print(nums1)
print(nums2)
print(queries)

solution = Solution()
print(solution.maximumSumQueries(nums1, nums2, queries))
