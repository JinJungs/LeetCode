# find the min number, and swap
from typing import List


def insertion_sort(l: List[int]) -> List[int]:
    n = len(l)
    for i in range(1, n):
        j = i
        while l[j-1] > l[j] and j > 0:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
    return l

if __name__ == '__main__':
    l = [91,38,71,3,4,1,2,7,9,10,0,64,99,57,60,20,8,0]
    print(insertion_sort(l))
