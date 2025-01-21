class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        "" -> "ros" : n
        "horse" -> "" -> m

        i-1, j-1 index

        1) stay
        hors / ros
        i = 4, j = 3
        hor / ro
        i = 3, j = 2

        2) insert
        horse / ros
        i = 5, j = 3
        horses / ros
        horse / ro
        i = 5, j = 2

        3) delete
        horse / ros
        i = 5, j = 3
        hors / ros
        i = 4, j = 3

        4) replace
        horse / ros
        i = 5, j = 3
        horss / ros
        hors / ro
        i = 4, j = 2

        dp(m,n) = dp(m-1,n-1) if word1[m] == word2[n] else min(dp(m, n-1), dp(m-1, n), dp(m-1, n-1)) + 1
        '''

        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

        return dp[-1][-1]
