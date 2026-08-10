class Solution {
    public int partitionArray(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);

        int res = 0;
        int start = 0;

        while (start < n) {
            int curr = start;
            int endNum = nums[start] + k;
            while (curr < n && nums[curr] <= endNum) {
                curr++;
            }
            res++;
            start = curr;
        }

        return res;
        
    }
}