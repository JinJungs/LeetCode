from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        set_days = set(days)
        d = dict()
        c = {0:1, 1:7, 2:30}
        before_day = 0
        d[0] = 0

        for day in range(1, days[-1]+1):
            if day in set_days:
                result = float('inf')
                for j in range(len(costs)):
                    cost = costs[j]
                    interval = c[j]
                    if day >= interval:
                        result = min(result, d[day-interval]+cost)
                    else:
                        result = min(result, cost)
                d[day] = result
                before_day = day
            else:
                d[day] = d.get(before_day)

        return d.get(days[-1])

