from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        u = float("inf")
        d = []

        for num in nums:
            # check triplet
            if len(d) == 2 and max(d) < num:
                return True

            # update double
            if len(d) == 2 and d[0] < num < d[1]:
                d = [d[0], num]
            elif u < num and (len(d) == 0 or u < min(d)):
                d = [u, num]

            # update uni
            else:
                u = min(u, num)

        return False
