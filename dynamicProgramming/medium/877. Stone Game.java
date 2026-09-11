class Solution {
    public boolean stoneGame(int[] piles) {
        int n = piles.length;
        int[][] dp = new int[n][n];

        for (int l = n-1; l >= 0; l--) {
            for (int r = l; r < n; r++) {
                if (l == r) {
                    dp[l][r] = piles[l];
                    continue;
                }
                
                dp[l][r] = Math.max(
                    piles[l] - dp[l+1][r],
                    piles[r] - dp[l][r-1]
                );
            }
        }

        return dp[0][n-1] > 0;
    }
}