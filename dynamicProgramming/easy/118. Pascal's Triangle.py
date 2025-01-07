from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # 0    1
        # 1    1 1
        # 2    1 2 1        d[n][m] = d[n-1][m-1] + d[n-1]d[m]
        # 3    1 3 3 1
        # 4    1 4 6 4 1

        n = numRows
        d = [[] for _ in range(n)]
        d[0] = [1]

        for i in range(1,n):
            p = []
            for j in range(i+1):
                s = 0
                if j > 0:
                    s += d[i-1][j-1]
                if j < i:
                    s += d[i-1][j]
                p.append(s)
            d[i] = p

        return d


