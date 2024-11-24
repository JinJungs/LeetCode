from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        intervals = []
        for point in points:
            if len(intervals) == 0:
                intervals.append(point)
                continue

            interval = intervals.pop()
            if interval[0] <= point[0] and point[1] <= interval[1]:
                intervals.append(point)
            elif interval[0] <= point[0] <= interval[1]:
                intervals.append([point[0], interval[1]])
            elif point[0] <= interval[0] and interval[1] <= point[1]:
                intervals.append(interval)
            elif point[0] <= interval[0] <= point[1]:
                intervals.append([interval[0], point[1]])
            else:
                intervals.append(interval)
                intervals.append(point)

        return len(intervals)