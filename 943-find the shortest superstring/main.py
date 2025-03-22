from collections import deque


class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        cache = defaultdict(int)

        def mergeWords(word, word2):
            key = word + "-" + word2
            if key in cache:
                return cache[key]

            M = len(word)
            N = len(word2)

            non_overlaps = N
            start = 0
            while start < M:
                idx, idx2 = start, 0
                while idx < M and idx2 < N:
                    if word[idx] != word2[idx2]:
                        break
                    idx += 1
                    idx2 += 1
                if idx == M:
                    non_overlaps = min(non_overlaps, N - M + start)
                start += 1
            cache[key] = (non_overlaps, word2[N - non_overlaps:])
            #print("key : {}, non_overlaps : {}, overlaps : {}, word_to_append : {}".format(
            #    key, non_overlaps, N - non_overlaps, word2[N - non_overlaps:]))
            return cache[key]

        # dp init
        # dp[state][i] - bitmask of words selected and the last word is words[i]
        L = len(words)
        S = 1 << L
        dp = [[float("inf")] * L for _ in range(S)]
        ss = [[""] * L for _ in range(S)]

        for x in range(L):
            s = 1 << x
            dp[s][x] = len(words[x])
            ss[s][x] = words[x]
        # print(dp)

        # dp transfer
        # tsp problem
        for s in range(S):
            # from, x must in s bitmask
            for x in range(L):
                if s >> x & 1 == 0:
                    continue
                # to, y must not in s bitmask
                for y in range(L):
                    if s >> y & 1 == 1:
                        continue
                    if x == y:
                        continue
                    ns = s | 1 << y
                    non_overlaps, word_to_append = mergeWords(words[x], words[y])
                    if dp[s][x] + non_overlaps < dp[ns][y]:
                        dp[ns][y] = dp[s][x] + non_overlaps
                        ss[ns][y] = ss[s][x] + word_to_append
        # print(dp)

        mini, mini_idx = float("inf"), -1
        for x in range(L):
            if mini > dp[S - 1][x]:
                mini = dp[S - 1][x]
                mini_idx = x
        ans = ss[S - 1][mini_idx]
        return ans


words = ["alex","loves","leetcode"]
words = ["catg", "ttca"]
words = ["catg","ctaagt","gcta","ttca","atgcatc"]
words = ["yeeiebcz","qbqhdytk","ygueikth","thqzyeei","gyygueikt","ikthqzyee"]
words = ["ygueikth","thqzyeei","gyygueikt"]

solution = Solution()
print(solution.shortestSuperstring(words))
