# find union and intersection of two sorted arrays


def union(list1, list2):
    new_arr = []
    for i in list1:
        if i not in new_arr:
            new_arr.append(i)
    for i in list2:
        if i not in new_arr:
            new_arr.append(i)
    new_arr.sort()
    print(new_arr)

def intersection(list1, list2):
    new_arr = []
    for i in list1:
        if (i not in new_arr) and (i in list2):
            new_arr.append(i)
            
    new_arr.sort()
    print(new_arr)
    

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [11, 21, 31, 41, 5, 6,9]

union(list1, list2)
intersection(list1, list2)