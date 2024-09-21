from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []
        for interval in intervals:
            if len(result) ==0:
                result.append(interval)
                continue
            r = result[-1]
            if interval[0] <= r[1]:
                result.pop()
                result.append([r[0], max(r[1], interval[1])])
            else:
                result.append(interval)

        return result