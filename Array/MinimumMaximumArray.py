# find maximum and minimum element in an array

def getMinMax(arr):
    arr.sort()
    minmax = {"min":arr[0], "max":arr[-1]}
    return minmax

arr =[9,8,3,-2,6,0]
minmax = getMinMax(arr) 

print("minimin element", minmax["min"])
print("maximum element", minmax["max"])
