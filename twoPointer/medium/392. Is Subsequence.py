class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # find character in sequencly
        index = 0
        max_index = len(s) -1
        for text in t:
            if index > max_index:
                return True
            if s[index] == text:
                index += 1

        return index > max_index