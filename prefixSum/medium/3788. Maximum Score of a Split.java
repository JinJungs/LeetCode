class Solution {
    public long maximumScore(int[] nums) {
        int n = nums.length;
        
        long[] prefixSum = new long[n];
        prefixSum[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i-1] + nums[i];
        }

        long[] suffixMin = new long[n-1];
        suffixMin[n-2] = nums[n-1];
        for (int i = n-3; i >=0; i--) {
            suffixMin[i] = Math.min(suffixMin[i+1], nums[i+1]);
        }

        long res = Long.MIN_VALUE;
        for (int i = 0; i < n-1; i++) {
            res = Math.max(res, (prefixSum[i] - suffixMin[i]));
        }

        return res;

    }
}