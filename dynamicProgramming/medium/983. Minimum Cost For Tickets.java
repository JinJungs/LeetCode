class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int lastDay = days[days.length-1];

        boolean[] travel = new boolean[lastDay + 1];
        for (int day : days) {
            travel[day] = true;
        }

        int[] dp = new int[lastDay + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i <= lastDay; i++) {
            if (!travel[i]) {
                dp[i] = dp[i-1];
                continue;
            }
            dp[i] = Math.min(dp[i], dp[i-1] + costs[0]);
            dp[i] = Math.min(dp[i], (i >= 7 ? dp[i-7] : 0) + costs[1]);
            dp[i] = Math.min(dp[i], (i >= 30 ? dp[i-30] : 0)  + costs[2]);
        }

        return dp[lastDay];
    }
}