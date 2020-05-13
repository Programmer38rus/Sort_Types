def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        print(i)
        no_swap = True
        for j in range(0, i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False
        if no_swap:
            return

def bubble_sort2(alist):
    for i in range(len(alist)):
        for j in range(i, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]




alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
bubble_sort(alist)
# bubble_sort2(alist)
print('Sorted list: ', end='')
print(alist)