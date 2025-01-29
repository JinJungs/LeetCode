# find the min number, and swap
from typing import List


def insertionSort(l: List[int]) -> List[int]:
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

if __name__ == '__main__':
    l = [91,38,71,3,4,1,2,7,9,10,0,64,99,57,60,20,8,0]
    print(insertionSort(l))
