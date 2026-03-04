def remove_duplicate(arr):
    """
    Remove duplicate elements from an array.

    Args:
        arr (list): The input array. 

    Returns:
        list: The array with duplicate elements removed.
    """
    dup = set()
    result = []
    for item in arr:
        if item not in dup:
            dup.add(item)
            result.append(item)
    return result

# Rotate array by k positions.
# Find missing number in array.

def rotate_array(arr, k):
    """
    Rotate an array to the right by k positions.

    Args:
        arr (list): The input array.
        k (int): The number of positions to rotate.

    Returns:
        list: The rotated array.
    """
    n = len(arr)
    k = k % n  # Handle cases where k is greater than n
    return arr[-k:] + arr[:-k]


def find_missing_number(arr):
    """
    Find the missing number in an array of consecutive integers.

    Args:
        arr (list): The input array.

    Returns:
        int: The missing number.
    """
    n = len(arr)
    total = (n + 1) * (n + 2) // 2  # Sum of first (n+2) natural numbers
    return total - sum(arr)


# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 2, 4, 1, 5]
    print(remove_duplicate(arr))  # Output: [1, 2, 3, 4, 5]
    print(rotate_array(arr, 2))    # Output: [1, 5, 1, 2, 3, 2, 4]
    arr = [1, 2, 3, 4, 5, 7]
    print(find_missing_number(arr)) # Output: 6