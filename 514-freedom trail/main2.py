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
        self.anses = list()

        # cache
        from collections import defaultdict
        self.cache = defaultdict(bool)

        def doFind(idx, idx2, steps):
            # check cache
            cache_key = str(idx) + "-" + str(idx2) + "-" + str(steps)
            if cache_key in self.cache:
                return
            else:
                self.cache[cache_key] = True
            # check end condition
            if idx2 == N:
                self.anses.append(steps)
                return

            # search
            if ring[idx] == key[idx2]:
                doFind(idx, idx2 + 1, steps + 1)
            else:
                # search anticlockwise
                for x in range(1, M):
                    new_idx = idx - x
                    if new_idx < 0:
                        new_idx += M
                    if ring[new_idx] == key[idx2]:
                        doFind(new_idx, idx2 + 1, steps + x + 1)
                        break
                # search clockwise
                for x in range(1, M):
                    new_idx = (idx + x) % M
                    if ring[new_idx] == key[idx2]:
                        doFind(new_idx, idx2 + 1, steps + x + 1)
                        break
        # process
        doFind(0, 0, 0)
        return min(self.anses)


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
