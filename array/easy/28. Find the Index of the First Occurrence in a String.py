class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        if len(needle) > len(haystack):
            return result
        for i in range(len(haystack)):
            # if haystack[i] == needle[0] and i+len(needle) <= len(haystack):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i

        return result