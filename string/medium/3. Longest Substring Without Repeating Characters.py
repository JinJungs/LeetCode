class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        max_count = 0
        l = []
        for i in range(len(s)):
            ch = s[i]
            if ch in l:
                max_count = max(max_count, len(l))
                ri = l.index(ch)
                l = l[ri+1:]

            l.append(ch)

        return max_count if max_count > len(l) else len(l)
