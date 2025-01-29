from typing import List


def bubbleSort(l: List[int]) -> List[int]:
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

if __name__ == '__main__':
    l = [91,38,71,3,4,1,2,7,9,10,0,64,99,57,60,20,8,0]
    bubbleSort(l)
    print(l)