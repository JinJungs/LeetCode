from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(start, end):
            # out of range
            if target <= nums[start]:
                return start
            if target > nums[end]:
                return end+1

            # divide into two
            mid = (start + end + 1) // 2

            if nums[start] <= target < nums[mid]:
                return binary_search(start, mid-1)
            else:
                return binary_search(mid, end)

        return binary_search(0, len(nums)-1)