from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph to store the adjacency list of courses
        graph = defaultdict(list)

        # Build the graph from prerequisites
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # States: 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses

        # Helper function to perform DFS
        def dfs(course):
            if visit[course] == 1:  # Cycle detected
                return False
            if visit[course] == 2:  # Already visited, no need to process again
                return True

            # Mark as visiting
            visit[course] = 1

            # Visit all the neighbors (prerequisite courses)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Mark as visited
            visit[course] = 2
            return True

        # Check each course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
