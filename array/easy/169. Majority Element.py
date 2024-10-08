from math import ceil
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        min_appear_times = ceil(n/2)
        cnt = 0
        now = None
        for num in nums:
            if num != now:
                now = num
                cnt = 0
            cnt += 1
            if cnt == min_appear_times:
                return num
