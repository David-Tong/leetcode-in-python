class SegmentTree(object):
    def __init__(self, s):
        self.N = len(s)
        self.s = [''] + list(s)
        self.prefix = [0] * 4 * self.N
        self.suffix = [0] * 4 * self.N
        self.scores = [0] * 4 * self.N

        # build segment tree
        self.__build__(1, 1, self.N)

    def __build__(self, pivot, left, right):
        # leaf node
        if left == right:
           self.prefix[pivot] = 1
           self.suffix[pivot] = 1
           self.scores[pivot] = 1
           return

        if left == 76 and right == 77:
            pass

        # divide and conquer
        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2
        self.__build__(left_child, left, middle)
        self.__build__(right_child, middle + 1, right)

        # merge
        self.scores[pivot] = max(self.scores[left_child], self.scores[right_child])
        self.prefix[pivot] = self.prefix[left_child]
        self.suffix[pivot] = self.suffix[right_child]
        if self.s[middle] == self.s[middle + 1]:
            self.scores[pivot] = max(self.scores[pivot], self.suffix[left_child] + self.prefix[right_child])
            if self.suffix[left_child] == middle + 1 - left_child:
                self.prefix[pivot] = self.suffix[left_child] + self.prefix[right_child]
            if self.suffix[right_child] == right - middle:
                self.suffix[pivot] = self.suffix[right_child] + self.suffix[left_child]
            """
            if self.prefix[left_child] == middle + 1 - left_child:
                self.prefix[pivot] = self.prefix[left_child] + self.prefix[right_child]
            if self.prefix[right_child] == right - middle:
                self.suffix[pivot] = self.suffix[left_child] + self.prefix[right_child]
            """

    def update(self, idx, ch):
        self.__update__(1, 1, self.N, idx + 1, ch)

    def __update__(self, pivot, left, right, idx, ch):
        # leaf node
        if left == right:
           self.s[idx] = ch
           return

        # divide and conquer
        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2
        if idx <= middle:
           self.__update__(left_child, left, middle, idx, ch)
        else:
           self.__update__(right_child, middle + 1, right, idx, ch)

        # merge
        self.scores[pivot] = max(self.scores[left_child], self.scores[right_child])
        self.prefix[pivot] = self.prefix[left_child]
        self.suffix[pivot] = self.suffix[right_child]
        if self.s[middle] == self.s[middle + 1]:
            self.scores[pivot] = max(self.scores[pivot], self.suffix[left_child] + self.prefix[right_child])
            if self.suffix[left_child] == middle + 1 - left_child:
                self.prefix[pivot] = self.suffix[left_child] + self.prefix[right_child]
            if self.suffix[right_child] == right - middle:
                self.suffix[pivot] = self.suffix[right_child] + self.suffix[left_child]
            """
            if self.prefix[left_child] == middle + 1 - left_child:
                self.prefix[pivot] = self.prefix[left_child] + self.prefix[right_child]
            if self.prefix[right_child] == right - middle:
                self.suffix[pivot] = self.suffix[left_child] + self.prefix[right_child]
            """

    def query(self):
        return self.scores[1]

    def display(self):
        self.cache = [[0] * (self.N + 1) for _ in range(self.N + 1)]
        self.cache2 = [0] * (self.N * 4)
        self.p(1, 1, self.N)

    def p(self, pivot, left, right):
        # print(pivot, left, right, self.scores[pivot])
        self.cache[left][right] = (self.scores[pivot], pivot)
        self.cache2[pivot] = (self.scores[pivot], left, right)

        # leaf
        if left == right:
            return

        # divide and conquer
        left_child = 2 * pivot
        right_child = 2 * pivot + 1
        middle = (left + right) // 2
        self.p(left_child, left, middle)
        self.p(right_child, middle + 1, right)


class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        # process
        L = len(queryCharacters)
        st = SegmentTree(s)
        print(st.scores)
        print(3 in st.scores)
        st.display()
        # 75 - 77
        print(st.cache[75][75])
        print(st.cache[76][76])
        print(st.cache[77][77])
        print(st.cache[75][76])
        print(st.cache[75][77])
        print(st.cache[76][77])
        print(st.cache2[63])
        print(st.cache2[62])
        ans = list()
        for x in range(L):
            st.update(queryIndices[x], queryCharacters[x])
            # print(st.scores)
            # print(st.prefix)
            # print(st.suffix)
            ans.append(st.query())
        return ans


s = "babacc"
queryCharacters = "bcb"
queryIndices = [1,3,3]

s = "abyzz"
queryCharacters = "aa"
queryIndices = [2,1]

s = "mqvivodnwlqkblnacpvqkonwaemvglhkkhcpxohmntoqhyeyvvjowcdhodujtujjooeddxvjfhpppgiw"
queryCharacters = "owwjnooweqoutilhpnajyjiaqvxcokqpeziczagypahzssiweedeot"
queryIndices = [29,21,0,2,21,61,0,63,9,9,60,13,68,16,57,42,69,26,32,28,73,8,51,29,33,2,44,53,7,19,21,1,0,73,19,53,50,65,31,21,65,29,19,73,18,31,12,34,77,44,22,11,44,21]

print(len(s))
print(s[74:77])

solution = Solution()
print(solution.longestRepeating(s, queryCharacters, queryIndices))
