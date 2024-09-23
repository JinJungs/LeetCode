from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ''

        min_len = 201
        for s in strs:
            min_len = min(min_len, len(s))
        if min_len == 0:
            return ''

        result = ''
        for i in range(min_len):
            temp = None
            for s in strs:
                p = s[i]
                if temp == None:
                    temp = p
                elif temp != p:
                    return result
            result += temp

        return result