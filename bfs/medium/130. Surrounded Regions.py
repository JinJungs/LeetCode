from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ############################################################
        # IDEA 2. BFS edges with 'O' -> mark as '#'
        ############################################################
        if not board:
            return

        m, n = len(board), len(board[0])

        def in_range(x,y):
            return 0 <= x < m and 0 <= y < n

        def is_edge(x,y) -> bool:
            return x == 0 or y == 0 or x == m-1 or y == n-1

        def bfs(x, y):
            q = deque([(x, y)])
            board[x][y] = '#'

            while q:
                cx, cy = q.popleft()

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = cx + dx, cy + dy

                    if not in_range(nx, ny):
                        continue

                    if board[nx][ny] == 'O':
                        board[nx][ny] = '#'
                        q.append((nx, ny))

        # Mark all 'O' connected to edges with '#'
        for i in range(m):
            for j in range(n):
                if is_edge(i,j) and board[i][j] == 'O':
                    bfs(i, j)

        # Flip the remaining 'O' to 'X' and '#' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'