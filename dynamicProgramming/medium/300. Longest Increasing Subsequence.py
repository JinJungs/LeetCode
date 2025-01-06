from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #  start with the last index, and put result to dp.
        n = len(nums)
        dp = [0 for _ in range(n)]

        for i in range(n-1, -1, -1):
            result = 0
            for j in range(i, n):
                if nums[i] < nums[j]:
                    result = max(result, dp[j])
            dp[i] = result + 1

        return max(dp)