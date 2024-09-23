from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums or len(nums) == 0:
            return []

        result = []
        start = None
        before = None

        # before + 1 == num
        for num in nums:
            if start == None:
                start = num
                before = num
            elif before != None and num == before + 1:
                before = num
            else:
                if start == before:
                    result.append(str(start))
                else:
                    result.append(str(start) + '->' + str(before))
                start = num
                before = num

        if start == before:
            result.append(str(start))
        else:
            result.append(str(start) + '->' + str(before))

        return result