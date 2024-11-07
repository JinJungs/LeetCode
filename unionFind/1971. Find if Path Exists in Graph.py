from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True

        # disjoin set 찾기!
        # parent 가 같지 않다면 disjoin set

        # initialize
        parent = dict()
        def makeSet(x):
            parent[x] = x

        # find
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # union
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            # if in the same set, do nothing
            if rootX == rootY:
                return
            # put in the same set
            parent[rootX] = rootY


        for i in range(n):
            makeSet(i)

        for edge in edges:
            union(edge[0], edge[1])

        return find(source) == find(destination)