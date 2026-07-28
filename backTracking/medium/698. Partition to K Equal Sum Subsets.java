class Solution {
    int n;
    int[] nums;
    int target;
    int k;
    boolean[] visited;

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        if (sum % k != 0) return false;
        
        Arrays.sort(nums);
        this.n = nums.length;
        this.nums = nums;
        this.k = k;
        this.target = sum / k;
        this.visited = new boolean[n];

        if (nums[n - 1] > target) return false;
        return dfs(n - 1, 0, 0);
    }

    public boolean dfs(int start, int curr, int bucket) {
        if (bucket == k-1) return true;
        if (curr > target) return false;
        if (curr == target) return dfs(n - 1, 0, bucket + 1);

        for (int i = start; i >= 0; i--) {
            if (visited[i]) continue;
            if (i < start && nums[i] == nums[i + 1] && !visited[i + 1]) continue;
            visited[i] = true;
            if (dfs(i - 1, curr + nums[i], bucket)) return true;
            visited[i] = false;
        }

        return false;
    }
}