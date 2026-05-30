class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        # pre-process
        L = len(queries[0])

        # helper function
        def canEdit(source, target):
            idx = 0
            diff = 0
            while idx < L:
                if source[idx] != target[idx]:
                    diff += 1
                    if diff > 2:
                        return False
                idx += 1
            return True

        # process
        ans = list()
        for query in queries:
            for word in dictionary:
                if canEdit(query, word):
                    ans.append(query)
                    break
        return ans


queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]

queries = ["yes"]
dictionary = ["not"]

solution = Solution()
print(solution.twoEditWords(queries, dictionary))
