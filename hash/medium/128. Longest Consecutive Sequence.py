from typing import List


class Solution:
    # Union & Find
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # key: num, value: next
        d = dict()

        # init: put self
        for num in nums:
            d[num] = num

        # union
        for num in d.keys():
            nxt = num + 1
            prev = num -1
            if d.get(prev) is not None:
                d[prev] = num
            if d.get(nxt) is not None:
                d[num] = nxt

        # find
        def find(d, now) -> int:
            if d.get(now) == now:
                return now

            d[now] = find(d, d.get(now))
            return d[now]

        # find all
        longest_seq = 0
        for now in d.keys():
            if d.get(now) is None:
                continue
            nxt = find(d, now)
            longest_seq = max(longest_seq, nxt-now+1)

        return longest_seq


# Easier Solution
    def longestConsecutive2(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest