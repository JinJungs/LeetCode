from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        q = deque([start])

        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True

            if not visited[i]:
                if i + arr[i] < n:
                    q.append(i + arr[i])
                if i - arr[i] >= 0:
                    q.append(i - arr[i])
                visited[i] = True

        return False