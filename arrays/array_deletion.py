def deletion(arr, value):
    if value not in arr:
        print("value not present in array")
    else:
        for i in range(len(arr)):
            if arr[i] == value:
                for j in range(i, len(arr) - 1):
                    arr[j] = arr[j+1]
        size = len(arr) - 1
        arr = arr[:size]
        return arr
        
        
        
arr = [2, 4, 6, 8, 10]
print(deletion(arr, 6))
        