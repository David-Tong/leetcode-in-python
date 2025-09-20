from idlelib.ColorDelegator import idprog


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
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        L = len(nums)
        pairs = zip(nums, [_ for _ in range(L)])
        # print(pairs)
        pairs = sorted(pairs, key=lambda x:x[0])
        # print(pairs)
        idxes = zip([pair[1] for pair in pairs], [_ for _ in range(L)])
        # print(idxes)
        idxes = [idx[0] for idx in idxes]
        # print(idxes)

        # process
        # suppose we have A, B, C for the three smallest numbers
        # X X A X X C X X B X X
        # remove A
        # X X C X X B X X, X X sum(0: a - 1)
        # remove B
        # X X, X X, X X C X X sum(a + 1: b - 1)
        # remove C
        # X X, X X, X X, X X sum(0 : c - 1) + sum(b + 1, n - 1)

        bit = BinaryIndexTree(L)
        # initialize binary index tree
        for x in range(L):
            bit.add(x + 1, 1)

        ans = L
        last_idx = -1
        for idx in idxes:
            if last_idx == -1:
                ans += bit.query(1, idx)
            else:
                if last_idx < idx:
                    ans += bit.query(last_idx + 2, idx)
                else:
                    ans += bit.query(1, idx) + bit.query(last_idx + 1, L)
            last_idx = idx
            bit.add(idx + 1, -1)
        return ans


# nums = [3,4,-1]
# nums = [1,2,4,3]
# nums = [1,2,3]
# nums = [3,4,2,1]
# nums = [5,4,3,2,1]

from random import randint
nums = set()
while len(nums) < 50000:
    num = randint(-10 ** 9 , 10 ** 9)
    nums.add(num)
print(nums)

# nums = [-15,-19,5]
# nums = [1,0,2]

solution = Solution()
print(solution.countOperationsToEmptyArray(nums))
