from typing import List


class Solution:
    # original solution
    def jump(self, nums: List[int]) -> int:
        canReach = [(False, len(nums)-1) for _ in range(len(nums))]
        canReach[0] = (True, 0)

        for i in range(len(nums)):
            if not canReach[i][0]:
                continue
            for j in range(1, nums[i]+1):
                if i+j < len(nums):
                    canReach[i+j] = (True, min(canReach[i+j][1], canReach[i][1] + 1))

        return canReach[-1][1]

    # use less memory solution
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        result = 0
        i = 0
        currMax = nextMax = nums[0]

        while i < len(nums):
            while i <= nextMax and i < len(nums):
                currMax = max(currMax, i + nums[i])
                i += 1
            nextMax = currMax
            result += 1

        return result

