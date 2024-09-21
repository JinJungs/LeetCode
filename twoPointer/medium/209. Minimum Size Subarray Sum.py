from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_nums = sum(nums)
        if sum_nums < target:
            return 0

        if sum_nums == target:
            return len(nums)

        # O(N3)
        # for j in range(1, sum_nums):
        #     for i in range(sum_nums - j + 1):
        #         arr = nums[i:i+j]
        #         if sum(arr) >= target:
        #             return j

        start = 0
        end = 1
        n = len(nums)
        min_length = n

        # current
        sum_of_arr = nums[0]

        while start < n:
            if sum_of_arr >= target:
                min_length = min(min_length, end-start)
                sum_of_arr -= nums[start]
                start += 1
            else:
                if end < n:
                    sum_of_arr += nums[end]
                    end += 1
                else:
                    sum_of_arr -= nums[start]
                    start += 1

        return min_length