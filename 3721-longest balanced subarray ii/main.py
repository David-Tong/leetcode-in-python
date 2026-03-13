class Node(object):
    __slots__ = ['min', 'max', 'todo']

    def __init__(self):
        self.min = 0
        self.max = 0
        self.todo = 0


class LazySegmentTree(object):
    def __init__(self, n):
        self.N = n + 1
        self.nodes = [Node() for _ in range(self.N * 4)]

    # apply lazy update the node
    def __apply(self, node, todo):
        curr = self.nodes[node]
        curr.min += todo
        curr.max += todo
        curr.todo += todo

    # spread lazy update, update downside
    def __spread(self, node):
        todo = self.nodes[node].todo
        if todo == 0:
            return
        self.__apply(node * 2, todo)
        self.__apply(node * 2 + 1, todo)
        self.nodes[node].todo = 0

    # merge for update upside
    def __merge(self, node):
        left_node = self.nodes[node * 2]
        right_node = self.nodes[node * 2 + 1]
        self.nodes[node].min = min(left_node.min, right_node.min)
        self.nodes[node].max = max(left_node.max, right_node.max)

    # internal update
    def __update(self, node, left, right, query_left, query_right, value):
        if query_left <= left and query_right >= right:
            self.__apply(node, value)
            return

        self.__spread(node)
        middle = (left + right) // 2
        if query_left <= middle:
            self.__update(node * 2, left, middle, query_left, query_right, value)
        if query_right > middle:
            self.__update(node * 2 + 1, middle + 1, right, query_left, query_right, value)
        self.__merge(node)

    # internal find first
    def __find_first(self, node, left, right, query_left, query_right, target):
        if query_left > right or query_right < left:
            return -1
        if not self.nodes[node].min <= target <= self.nodes[node].max:
            return -1
        if left == right:
            return left

        self.__spread(node)
        middle = (left + right) // 2
        idx = self.__find_first(node * 2, left, middle, query_left, query_right, target)
        if idx < 0:
            idx = self.__find_first(node * 2 + 1, middle + 1, right, query_left, query_right, target)
        return idx

    # update
    def update(self, query_left, query_right, value):
        self.__update(1, 0, self.N - 1, query_left, query_right, value)

    # find first
    def find_first(self, query_left, query_right, target):
        return self.__find_first(1, 0, self.N - 1, query_left, query_right, target)


class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        lst = LazySegmentTree(N + 1)

        from collections import defaultdict
        dicts = defaultdict(int)

        presum = 0
        ans = 0
        for idx, num in enumerate(nums, 1):
            # update lst
            value = 1 if num % 2 else -1
            last = dicts.get(num, 0)
            if last == 0:
                presum += value
                lst.update(idx, N, value)
            else:
                lst.update(last, idx - 1, value * -1)
            dicts[num] = idx

            # search
            idx2 = lst.find_first(0, idx - 1 - ans, presum)
            if idx2 >= 0:
                ans = max(ans, idx - idx2)
        return ans


nums = [2,5,4,3]
nums = [3,2,2,5,4]
nums = [1,2,3,2]

from random import randint
nums = [randint(1, 50) for _ in range(10 ** 5)]
print(nums)

# nums = [9,13,11,10]

solution = Solution()
print(solution.longestBalanced(nums))