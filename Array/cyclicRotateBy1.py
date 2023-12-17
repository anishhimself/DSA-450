def rotate( arr, n):
    
    if n<=1:
        return arr
    temp= arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

my_array = [11,23,45,67,8]

rotated_array = rotate(my_array, 5)
print(rotated_array)