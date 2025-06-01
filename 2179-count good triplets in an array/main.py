class BinaryIndexTree(object):
    def __init__(self, N):
        self.N = N
        self.t = [0] * (N + 1)

    def lowbit(self, idx):
        return idx & -idx

    def add(self, idx, value):
        while idx <= self.N:
            self.t[idx] += value
            idx += self.lowbit(idx)

    def prefix_sum(self, idx):
        psum = 0
        while idx > 0:
            psum += self.t[idx]
            idx -= self.lowbit(idx)
        return psum

    def query(self, start, end):
        return self.prefix_sum(end) - self.prefix_sum(start - 1)


class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # pre-process
        # rearrange two arrays
        L = len(nums1)
        from collections import defaultdict
        dicts = defaultdict(int)
        for idx, num in enumerate(nums1):
            dicts[num] = idx + 1
            nums1[idx] = idx + 1
        for idx in range(L):
            nums2[idx] = dicts[nums2[idx]]

        print(nums1)
        print(nums2)

        # process
        smaller_before = [0] * L
        bit = BinaryIndexTree(L)
        for idx in range(L):
            smaller_before[idx] = bit.prefix_sum(nums2[idx])
            bit.add(nums2[idx], 1)

        larger_after = [0] * L
        bit2 = BinaryIndexTree(L)
        for idx in range(L - 1, -1, -1):
            larger_after[idx] = bit2.query(nums2[idx], L)
            bit2.add(nums2[idx], 1)

        print(smaller_before)
        print(larger_after)

        ans = 0
        for idx in range(L):
            ans += smaller_before[idx] * larger_after[idx]
        return ans


nums1 = [2,0,1,3]
nums2 = [0,1,2,3]

nums1 = [4,0,1,3,2]
nums2 = [4,1,0,2,3]

solution = Solution()
print(solution.goodTriplets(nums1, nums2))
