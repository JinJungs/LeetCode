def quickSort(l, start, end):
    if end - start < 2:
        return

    left = start
    low = start+1
    high = end
    pivot = l[left]

    while low <= high:
        move = False
        if l[low] < pivot:
            low += 1
            move = True
        if l[high] > pivot:
            high -= 1
            move = True

        if not move:
            l[high], l[low] = l[low], l[high]

    l[left], l[high] = l[high], l[left]

    quickSort(l, start, high-1)
    quickSort(l, high+1, end)

if __name__ == '__main__':
    l = [91,38,71,3,4,1,2,7,9,10,0,64,99,57,60,20,8,0]
    quickSort(l, 0, len(l)-1)
    print(l)