from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 0
            else:
                k += 1

        nums.sort(reverse=True)
        return k


        # best solution
        # k = 0
        # for num in nums:
        #     if num != val:
        #         nums[k] = num
        #         k += 1
        # return k