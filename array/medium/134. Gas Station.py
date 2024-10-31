from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start point matters
        # O(n)
        """
        index 0  1  2  3  4
        gas   1  2  3  4  5
        cost  3  4  5  1  2
        """

        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        start_index = 0
        i = 0
        tank = 0
        while i < n:
            tank += gas[i]
            next_index = i + 1 if i + 1 < n else 0

            if tank - cost[i] < 0:
                tank = 0
                start_index = next_index
            else:
                if start_index == next_index:
                    break
                tank -= cost[i]

            i = next_index

        return start_index