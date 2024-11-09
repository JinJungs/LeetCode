from typing import List


class Solution:
    # UNION FIND
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


    # DFS
    def validPath2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True

        # make dictionary with key: node , value: linked node list
        d = dict()
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]

            if v1 in d.keys():
                d[v1].append(v2)
            else:
                d[v1] = [v2]

            if v2 in d.keys():
                d[v2].append(v1)
            else:
                d[v2] = [v1]

        visited = [False] * n
        def dfs(s):
            visited[s] = True

            for v in d[s]:
                if v == destination:
                    return True
                if not visited[v] and dfs(v):
                    return True
            return False

        return dfs(source)