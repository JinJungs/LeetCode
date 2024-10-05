class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()
        for i in range(len(s)):
            if s[i] in d1.keys() and d1[s[i]] != t[i]:
                return False
            elif t[i] in d2.keys() and d2[t[i]] != s[i]:
                return False
            else:
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]

        return True
