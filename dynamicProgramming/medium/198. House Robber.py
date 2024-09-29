from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        d = [-1] * (l+1)
        def recursive(start: int):
            if start > l-1:
                return 0
            if start == l-1:
                return nums[start]
            if start == l-2:
                return max(nums[start], nums[-1])
            if d[start] == -1:
                d[start] = max(nums[start] + recursive(start+2), nums[start+1] + recursive(start+3))
            return d[start]

        return max(recursive(0), recursive(1))


    # Solution From LeetCode
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # dp start index with 0
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]