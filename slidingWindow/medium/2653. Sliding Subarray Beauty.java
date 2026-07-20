class Solution {
    public int[] getSubarrayBeauty(int[] nums, int k, int x) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        int[] freq = new int[101];

        for (int i = 0; i < k; i++) {
            freq[nums[i] + 50]++;
        }

        res[0] = getBeauty(freq, x);

        for (int r = k; r < n; r++) {
            int l = r - k;

            freq[nums[l] + 50]--;

            freq[nums[r] + 50]++;

            res[l + 1] = getBeauty(freq, x);
        }

        return res;
    }

    private int getBeauty(int[] freq, int x) {
        int cnt = 0;

        for (int num = -50; num < 0; num++) {
            cnt += freq[num + 50];

            if (cnt >= x)
                return num;
        }

        return 0;
    }
}