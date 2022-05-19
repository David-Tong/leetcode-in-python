class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        N = len(start)
        GENES = "ACGT"
        from collections import deque
        bfs = deque()
        bfs.append((start,1))
        visited = list()
        visited.append(start)
        while bfs:
            genes, mutations = bfs.popleft()
            for x in range(N):
                for gene in GENES:
                    mutated_gene = genes[:x] + gene + genes[x+1:]
                    if mutated_gene in bank:
                        if mutated_gene == end:
                            return mutations
                        if mutated_gene not in visited:
                            bfs.append((mutated_gene, mutations + 1))
                            visited.append(mutated_gene)
        return -1


start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]

solution = Solution()
print(solution.minMutation(start, end, bank))
