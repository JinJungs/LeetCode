from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        """
        should be equal
        # sorted list
        """
        d = dict()
        for s in strs:
            t = str(sorted(s))
            if t in d.keys():
                d[t].append(s)
            else:
                d[t] = [s]

        return [x for x in d.values()]