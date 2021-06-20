# bubble sort algorithm using recursion

def bubble_sort(list):
    for i in range(len(list)-1):
        if list[i + 1] is not None:
            if list[i] > list[i + 1]:
                list[i], list[ i + 1] = list[i + 1], list[i]
                bubble_sort(list)
    return list
