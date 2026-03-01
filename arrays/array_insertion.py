def insertion(arr, index, value):
    if index <0 or index > len(arr):
        print("index is out of bounds")
    else:
        arr. append(0)
        for i in range(len(arr) - 1, index, -1):
            arr [i] = arr[i - 1]
        arr[index] = value
        return arr
    
    
arr = [2, 4, 6, 8, 10]
print(insertion(arr, 2, 5))