class Solution {
    public int minimumIndex(List<Integer> nums) {
        int n = nums.size();

        // find dominent element
        int[] frontDom = new int[n];
        int maxCnt = 0;
        int maxNum = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int num = nums.get(i);
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            int cnt = freq.get(num);
            if (maxCnt < cnt) {
                maxCnt = cnt;
                maxNum = num;
            }
            frontDom[i] = maxCnt > (i+1) / 2 ? maxNum : 0;
        }

        int[] backDom = new int[n];
        maxCnt = 0;
        maxNum = 0;
        freq = new HashMap<>();
        for (int i = n-1; i > 0; i--) {
            int num = nums.get(i);
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            int cnt = freq.get(num);
            if (maxCnt < cnt) {
                maxCnt = cnt;
                maxNum = num;
            }
            backDom[i] = maxCnt > (n-i) / 2 ? maxNum : 0;
        }

        for (int i = 0; i < n-1; i++) {
            if (frontDom[i] == backDom[i+1]) return i;
        }

        return -1;
    }
}   