from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def in_range(x, y) -> bool:
            return x>=0 and y>=0 and x<m and y<n

        def near(x, y):
            result = []
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if in_range(nx,ny):
                    result.append((nx,ny))
            return result

        def dfs(grid, x, y, visited):
            visited[x][y] = True

            # search near points
            for nx,ny in near(x,y):
                if not visited[nx][ny] and grid[nx][ny] == '1':
                    dfs(grid, nx, ny, visited)

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(grid, i, j, visited)
                    num_islands += 1

        return num_islands
