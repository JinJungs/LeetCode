from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            num = nums[i]
            if target - num in temp.keys():
                return [temp[target-num], i]
            else:
                temp[num] = i