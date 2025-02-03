# find the min number, and swap
from typing import List


def selection_sort(l: List[int]) -> List[int]:
    n = len(l)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if l[m] > l[j]:
                m = j
        if m != i:
            l[i], l[m] = l[m], l[i]
    return l

if __name__ == '__main__':
    l = [91,38,71,3,4,1,2,7,9,10,0,64,99,57,60,20,8,0]
    print(selection_sort(l))
