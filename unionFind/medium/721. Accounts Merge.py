from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # initialize
        parent = dict()
        names = dict()
        children = dict()

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                parent[email] = email
                names[email] = name

        def union(e1, e2):
            p1 = find(e1)
            p2 = find(e2)
            # if in the same key, do nothing
            if p1 == p2:
                return
            parent[p1] = p2

        '''
        johnsmith -> john_newyork
        john_newyork -> john_newyork

        john_newyork -> john00
        john00 -> john00

        johnsmith22 -> john00
        john00 -> john00

        johnsmith -> john_newyork
        john_newyork -> john00
        john00 -> john00
        '''


        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for account in accounts:
            emails = account[1:]
            if len(emails) <= 1:
                continue
            for i in range(len(emails)-1):
                union(emails[i], emails[i+1])

        # main
        k = list(parent.keys())
        for i in range(len(k)):
            # make children
            p1 = find(k[i])
            if p1 not in children.keys():
                children[p1] = set()
            children[p1].add(k[i])

        result = []
        for represent in children.keys():
            r = [names[represent]]
            r.extend(sorted(children[represent]))
            result.append(r)

        return result
