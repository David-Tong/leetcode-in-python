class Node(object):
    __slots__ = ['sum', 'leftMaxSum', 'rightMaxSum', 'maxSum']

    def __init__(self, value=0):
        self.sum = value
        self.leftMaxSum = value
        self.rightMaxSum = value
        self.maxSum = value

    def __str__(self):
        return "sum : {}, left max sum : {}, right max sum : {}, max sum : {}".format(
            self.sum, self.leftMaxSum, self.rightMaxSum, self.maxSum
        )


class SegmentTree(object):
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.nodes = [None for _ in range(self.N * 4)]
        self.__build(1, 0, self.N - 1)

    def __build(self, pivot, left, right):
        if left == right:
            self.nodes[pivot] = Node(self.nums[left])
            return

        left_child = pivot * 2
        right_child = pivot * 2 + 1
        middle = (left + right) // 2
        self.__build(left_child, left, middle)
        self.__build(right_child, middle + 1, right)
        self.__merge(pivot, left_child, right_child)

    def __merge(self, pivot, left_child, right_child):
        self.nodes[pivot] = Node()
        self.nodes[pivot].sum = self.nodes[left_child].sum + self.nodes[right_child].sum
        self.nodes[pivot].leftMaxSum = max(self.nodes[left_child].leftMaxSum,
                                           self.nodes[left_child].sum + self.nodes[right_child].leftMaxSum)
        self.nodes[pivot].rightMaxSum = max(self.nodes[right_child].rightMaxSum,
                                             self.nodes[right_child].sum + self.nodes[left_child].rightMaxSum)
        self.nodes[pivot].maxSum = max(self.nodes[left_child].rightMaxSum + self.nodes[right_child].leftMaxSum,
                                       max(self.nodes[left_child].maxSum, self.nodes[right_child].maxSum))

    def update(self, index, value):
        self.__update(1, 0, self.N - 1, index, value)

    def __update(self, pivot, left, right, index, value):
        if left == right:
            self.nodes[pivot] = Node(value)
            return

        left_child = pivot * 2
        right_child = pivot * 2 + 1
        middle = (left + right) // 2
        if index <= middle:
            self.__update(left_child, left, middle, index, value)
        else:
            self.__update(right_child, middle + 1, right, index, value)
        self.__merge(pivot, left_child, right_child)

    def query(self):
        return self.nodes[1].maxSum


class Solution(object):
    def maxSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        all_negative = True
        for idx, num in enumerate(nums):
            if num >= 0:
                all_negative = False
            dicts[num].append(idx)

        # conner case
        # if all negative, just keep the smallest one
        if all_negative:
            ans = max(nums)
            return ans

        # process
        st = SegmentTree(nums)
        ans = st.query()
        for num in dicts:
            if num < 0:
                for idx in dicts[num]:
                    st.update(idx, 0)
                ans = max(ans, st.query())
                for idx in dicts[num]:
                    st.update(idx, num)
        return ans


nums = [-3,2,-2,-1,3,-2,3]
nums = [1,2,3,4]

from random import randint
nums = [randint(-1 * 10 ** 6, 10 ** 6) for _ in range(10 ** 5)]
print(nums)

nums = [-31,-23,-47]
nums = [-2,-2,-2]
nums = [-2,1,1]

solution = Solution()
print(solution.maxSubarraySum(nums))
