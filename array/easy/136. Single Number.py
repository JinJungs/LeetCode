from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if d.get(num) == None:
                d[num] = 1
            else:
                d[num] = 2

        for k in d.keys():
            if d[k] == 1:
                return k

        # a better way with sorting, comparing neighbors