class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        # pre-process
        M = len(ring)
        N = len(key)

        # cache
        from collections import defaultdict
        self.cache = defaultdict(int)

        def doFind(idx, idx2):
            # check cache
            cache_key = str(idx) + "-" + str(idx2)
            if cache_key in self.cache:
                return self.cache[cache_key]
            # check end condition
            if idx2 == N:
                return 0

            # search
            steps = float("inf")
            if ring[idx] == key[idx2]:
                steps = min(steps, 1 + doFind(idx, idx2 + 1))
            else:
                # search anticlockwise
                for x in range(1, M):
                    new_idx = idx - x
                    if new_idx < 0:
                        new_idx += M
                    if ring[new_idx] == key[idx2]:
                        steps = min(steps, x + 1 + doFind(new_idx, idx2 + 1))
                        break
                # search clockwise
                for x in range(1, M):
                    new_idx = (idx + x) % M
                    if ring[new_idx] == key[idx2]:
                        steps = min(steps, x + 1 + doFind(new_idx, idx2 + 1))
                        break
            self.cache[cache_key] = steps
            return steps
        # process
        return doFind(0, 0)


ring = "godding"
key = "gd"

ring = "godding"
key = "godding"

ring = "xrrakuulnczywjs"
key = "jrlucwzakzussrlckyjjsuwkuarnaluxnyzcnrxxwruyr"

ring = "phttxdfyxhzcbvlatwotitjtgfxaytdtqqtgwjsclgvjlcxxngermlfspnshfsdqkecqmvoapkktnbztmutcesghvzvjhuxmsajs"
key = "pmsjlfttndscwlxxshztmdwknqkrzotznvtgxceitsffacjyjbpthpgsxvavqmthugqhkvtotsvtqdycjsjualtggbfeeachxlxm"

ring = "zewkukpwkndkhhxhtrshraruihgwsnkjsbwtosyozhbpnoficcshmihhjckwkpeavmprmfmtrmjdcqfagrcqxwydvzverjrvjxkt"
key = "cthkqohskvhximenjgmacrkhtvyiwmvkbfjcdshzrhswrprzckjhzxkdhurtkqjsixrwavpeosmmprgwyrfofhtujkbwwapndnec"

solution = Solution()
print(solution.findRotateSteps(ring, key))
