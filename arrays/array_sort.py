def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

def second_largest(arr):
    sorted_arr = sort(arr)
    return sorted_arr[-2]

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    print(sort(arr))
    print(second_largest(arr))