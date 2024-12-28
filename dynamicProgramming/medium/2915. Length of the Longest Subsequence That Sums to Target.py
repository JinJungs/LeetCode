from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        # key: sum, value: length
        d = dict()
        d[0] = 0

        for num in nums:
            # for all combinations in d
            dc = d.copy()
            for k in d.keys():
                if k+num <= target:
                    dc[k+num] = d.get(k) + 1 if k+num not in d else max(d.get(k+num), d.get(k) + 1)
            d = dc

        return -1 if target not in d else d.get(target)

