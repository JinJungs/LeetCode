from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        ba = None
        for i in range(len(nums)):
            a = nums[i]
            if ba != None and ba == a:
                continue

            start = i+1
            end = len(nums) -1
            bs = None
            be = None
            temp = []
            while start < end:
                b = nums[start]
                c = nums[end]
                s = a + b + c
                if s == 0 and bs != b and be != c:
                    temp.append([a,b,c])
                    bs = b
                    be = c
                elif s > 0:
                    end -= 1
                else:
                    start += 1

            if len(temp) > 0 and ba != a:
                result += temp
                ba = a

        return result