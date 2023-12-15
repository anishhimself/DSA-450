arr = [11, -22, 33, 0, -1, 8, -2, -3, 77, 55, -44]

n = len(arr)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    # If no swaps were made, the array is already sorted
    if not swapped:
        break

print(arr)