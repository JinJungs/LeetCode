from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = dict()

        # put in dictionary
        for i in range(len(values)):
            a, b = equations[i]
            value = values[i]

            if a not in d.keys():
                d[a] = [(b,value)]
            else:
                d[a].append((b,value))

            if b not in d.keys():
                d[b] = [(a,1/value)]
            else:
                d[b].append((a,1/value))

        def dfs(head,under,result,visited):
            if head not in d.keys() or under not in d.keys():
                return -1.0

            if head == under:
                return 1

            visited.add(head)

            for next_head, value in d[head]:
                if next_head == under:
                    return result * value

                if next_head not in visited:
                    dfs_result = dfs(next_head,under,result * value, visited)
                    if dfs_result != -1.0:
                        return dfs_result
            return -1.0

        # main
        answers = []
        for head, under in queries:
            answers.append(dfs(head,under,1,set()))

        return answers