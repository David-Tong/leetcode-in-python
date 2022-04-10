class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        from collections import defaultdict
        dict = defaultdict(int)
        for ch in s:
            dict[ch] += 1

        import heapq
        heap = [ord('z') - ord(x) for x in dict.keys()]
        heapq.heapify(heap)

        ans = ""
        while heap:
            ch = chr(ord('z') - heapq.heappop(heap))
            permitLen = repeatLimit
            if len(ans) > 0 and ans[-1] == ch:
                permitLen = repeatLimit - 1

            if dict[ch] >= permitLen:
                ans += ch * permitLen
                dict[ch] -= permitLen
                if heap:
                    next_ch = chr(ord('z') - heapq.heappop(heap))
                    dict[next_ch] -= 1
                    if dict[next_ch] > 0:
                        heapq.heappush(heap, (ord('z') - ord(next_ch)))
                    ans += next_ch
                else:
                    break
                if dict[ch] > 0:
                    heapq.heappush(heap, (ord('z') - ord(ch)))
            else:
                ans += ch * dict[ch]
                dict[ch] = 0
        return ans


s = "cczazcc"
repeatLimit = 3

#s = "aababab"
#repeatLimit = 2

#s = "a"
#repeatLimit = 1

s = "robnsdvpuxbapuqgopqvxdrchivlifeepy"
repeatLimit = 2

s = "xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt"
repeatLimit = 1

solution = Solution()
print(solution.repeatLimitedString(s, repeatLimit))
