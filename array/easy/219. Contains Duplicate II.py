from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num in d.keys():
                d[num].append(i)
            else:
                d[num] = [i]


        for num in d.keys():
            l = d[num]
            if len(l) <= 1:
                continue
            l.sort()
            for i in range(len(l)-1):
                if l[i+1] - l[i] <= k:
                    return True

        return False