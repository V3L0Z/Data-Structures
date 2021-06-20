# selection sort, iterative

def selection_sort(list):
    for i in range(len(list)):
        index = i
        for j in range(i + 1, len(list)):
            if list[index] > list[j]:
                index = j
        list[i], list[index] = list[index], list[i]
    return list