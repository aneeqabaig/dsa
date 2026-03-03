def update(arr, index, value):
    if index < 0 or index >= len(arr):
        print("index is out of bounds")
    else:
        arr[index] = value
        return arr
arr = [2, 4, 6, 8, 10]
print(update(arr, 2, 5))