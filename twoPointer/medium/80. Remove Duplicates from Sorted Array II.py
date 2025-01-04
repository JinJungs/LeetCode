from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = -1
        cnt = 0
        target = nums[0]
        n = len(nums)

        # if available, update target, cnt, p
        # if not available (cnt >= 2 and num == target), do nothing
        # when switch? => i diff p >= 2

        for i in range(n):
            num = nums[i]

            if cnt < 2 or num != target:
                cnt = 1 if num != target else cnt + 1
                target = num

                # switch
                nums[i], nums[p+1] = nums[p+1], nums[i]
                p = p+1

        return p+1

    def removeDuplicates2(self, nums: List[int]) -> int:
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k

