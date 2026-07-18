class Solution {
    public int findCelebrity(int[][] graph) {
        int n = graph.length;
        
        int[] known = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                
                if (graph[i][j] == 1) {
                    known[j]++;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            int know = 0;
            
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                
                if (graph[i][j] == 1) {
                    know++;
                }
            }

            if (know == 0 && known[i] == n - 1) {
                return i;
            }
        }

        return -1;
    }
}