from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if not nums or k == 0 or k % l == 0:
            return

        k = k % l
        nums.reverse()

        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        for i in range(k, (k+l)//2):
            nums[i], nums[k+l-1-i] = nums[k+l-1-i], nums[i]