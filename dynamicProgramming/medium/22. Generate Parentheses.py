from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # d[n] = u[n] + u[n-1] * d[1] + u[n-2] * d[2] + .... + d[]
        # d[n] = u[k] * d[n-k]

        u = [[] for _ in range(n+1)]
        d = [[] for _ in range(n+1)]
        d[0] = ['']
        d[1] = ['()']
        u[0] = ['']
        u[1] = ['()']

        for i in range(2,n+1):
            next_u = []
            for p in d[i-1]:
                next_u.append('(' + p + ')')
            u[i] = next_u

            next_d = []
            for j in range(i+1):
                for p1 in u[j]:
                    for p2 in d[i-j]:
                        next_d.append(p1 + p2)
            d[i] = next_d

        return d[n]
