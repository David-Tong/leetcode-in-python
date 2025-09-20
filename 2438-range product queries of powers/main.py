class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # pre-process
        MODULO = 10 ** 9 + 7
        powers = list()
        target = n
        idx = 0
        while target:
            if target & 1:
                powers.append(2 ** idx)
            target >>= 1
            idx += 1
        # print(powers)

        products = [1]
        for power in powers:
            products.append(products[-1] * power)
        # print(products)

        # process
        ans = list()
        for query in queries:
            start, end = query
            ans.append(products[end + 1] // products[start] % MODULO)
        return ans


n = 15
queries = [[0,1],[2,2],[0,3]]

n = 2
queries = [[0,0]]

n = 10 ** 9
queries = [[0,1],[2,2],[0,3],[0,8],[9,9],[10,12]]

solution = Solution()
print(solution.productQueries(n, queries))
