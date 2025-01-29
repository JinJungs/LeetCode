from typing import List


class Solution:
    def isPalindrome(self, s: str):
        n = len(s)
        for i in range(n):
            if s[i] != s[n-i-1]:
                return False
            if i > n / 2:
                break
        return True

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        if n == 0:
            return [[]]

        if n == 1:
            self.dp[s] = [[s]]
            return [[s]]

        if s in self.dp.keys():
            return self.dp[s]

        for i in range(1, n+1):
            p = s[:i]
            if self.isPalindrome(p):
                w = s[i:]
                li = self.partition(w)
                self.dp[w] = li

                for l in li:
                    result.append([p] + l)

        return result