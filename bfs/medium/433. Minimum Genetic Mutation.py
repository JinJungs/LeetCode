from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if not bank:
            return -1

        options = ['A', 'C', 'G', 'T']

        q = deque([startGene])
        visited = set()
        cnt = 0

        while q:
            size = len(q)
            for i in range(size):
                gene = q.popleft()
                if gene == endGene:
                    return cnt

                for j in range(8):
                    for option in options:
                        newGene = gene[:j] + option + gene[j+1:]
                        # print(newGene)
                        if newGene in bank and newGene not in visited:
                            visited.add(newGene)
                            q.append(newGene)
            cnt += 1

        return -1