class Solution {
    public int findMaxFish(int[][] grid) {
        int res = 0;

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] > 0) {
                    res = Math.max(res, dfs(r, c, grid));
                }
            }
        }

        return res;
    }

    int[] dx = new int[] {1, 0, -1, 0};
    int[] dy = new int[] {0, 1, 0, -1};

    public int dfs(int x, int y, int[][] grid) {
        int sum = grid[x][y];
        grid[x][y] = -1;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && grid[nx][ny] > 0) {
                sum += dfs(nx, ny, grid);
            }
        }
        return sum;
    }
}