class SegmentTree(object):
    def __init__(self, baskets):
        self.N = len(baskets)
        self.baskets = [0] + baskets
        self.f = [0 for _ in range(4 * self.N)]
        self.__build__(1, 1, self.N)

    def __build__(self, pivot, left, right):
        # leaf node
        if left == right:
            self.f[pivot] = self.baskets[left]
            return

        # divide and conquer
        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2
        self.__build__(left_child, left, middle)
        self.__build__(right_child, middle + 1, right)
        self.f[pivot] = max(self.f[left_child], self.f[right_child])

    def update(self, idx, x):
        self.__update__(1, 1, self.N, idx, x)

    def __update__(self, pivot, left, right, idx, x):
        # leaf node
        if left == right:
            self.f[pivot] = x
            return

        # divide and conquer
        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2
        if idx <= middle:
            self.__update__(left_child, left, middle, idx, x)
        else:
            self.__update__(right_child, middle + 1, right, idx, x)
        self.f[pivot] = max(self.f[left_child], self.f[right_child])

    def query(self, start, end):
        return self.__query__(1, 1, self.N, start, end)

    def __query__(self, pivot, left, right, start, end):
        # leaf node
        if left == start and right == end:
            return self.f[pivot]

        # divide and conquer
        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2

        # only consider either left or right child
        if end <= middle:
            return self.__query__(left_child, left, middle, start, end)
        if start > middle:
            return self.__query__(right_child, middle + 1, right, start ,end)

        # otherwise, need to consider both children
        left_part = self.__query__(left_child, left, middle, start, middle)
        right_part = self.__query__(right_child, middle + 1, right, middle + 1, end)
        return max(left_part, right_part)


class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        # pre-process
        N = len(baskets)
        st = SegmentTree(baskets)

        # helper function
        def canPlace(fruit):
            left, right = 1, N
            while left + 1 < right:
                middle = (left + right) // 2
                if st.query(1, middle) >= fruit:
                    right = middle
                else:
                    left = middle + 1
            if st.query(1, left) >= fruit:
                st.update(left, 0)
                return True
            elif st.query(1, right) >= fruit:
                st.update(right, 0)
                return True
            else:
                return False

        # process
        ans = 0
        for fruit in fruits:
            if not canPlace(fruit):
                ans += 1
        return ans


fruits = [4,2,5]
baskets = [3,5,4]

fruits = [3,6,1]
baskets = [6,4,7]

fruits = [3,5,2,2,8,9]
baskets = [1,2,10,4,8,10]

solution = Solution()
print(solution.numOfUnplacedFruits(fruits, baskets))
