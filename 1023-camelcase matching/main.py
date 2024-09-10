class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        import string

        upper_pattern = ""
        for ch in pattern:
            if ch in string.uppercase:
                upper_pattern += ch

        def doMatchUpperCase(query):
            upper_query = ""
            for ch in query:
                if ch in string.uppercase:
                    upper_query += ch

            return upper_query == upper_pattern

        def doMatch(query):
            if not doMatchUpperCase(query):
                return False

            M = len(query)
            N = len(pattern)

            idx = 0
            idx2 = 0
            while idx < M and idx2 < N:
                if query[idx] == pattern[idx2]:
                    idx2 += 1
                idx += 1

            if idx2 == N:
                while idx < M:
                    if query[idx] in string.uppercase:
                        return False
                    idx += 1
                return True
            else:
                return False

        ans = list()
        for query in queries:
            ans.append(doMatch(query))
        return ans


queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBa"

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FoBaT"

solution = Solution()
print(solution.camelMatch(queries, pattern))
