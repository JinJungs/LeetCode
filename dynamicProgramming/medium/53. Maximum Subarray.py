from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return sum(nums)

        current_sum = 0
        min_sum = 0
        result = max(nums)
        for num in nums:
            current_sum += num
            result = max(result, current_sum - min_sum)
            min_sum = min(min_sum , current_sum)

        return result